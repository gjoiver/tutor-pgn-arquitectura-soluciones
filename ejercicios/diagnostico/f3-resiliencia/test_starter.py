import time

import pytest

from starter import CircuitOpenError, FlakyService, ResilientClient, ServiceUnavailable


def test_success_no_retry_needed():
    service = FlakyService(fail_times=0)
    client = ResilientClient(service, max_retries=3, failure_threshold=2, reset_timeout=0.05)

    assert client.call() == "ok"
    assert service.calls == 1
    assert client.consecutive_failures == 0


def test_retry_recovers_within_a_single_call():
    service = FlakyService(fail_times=2)
    client = ResilientClient(service, max_retries=3, failure_threshold=2, reset_timeout=0.05)

    assert client.call() == "ok"
    assert service.calls == 3
    assert client.consecutive_failures == 0
    assert client.circuit_open_at is None


def test_circuit_opens_after_threshold_and_fails_fast():
    service = FlakyService(fail_times=100)
    client = ResilientClient(service, max_retries=1, failure_threshold=2, reset_timeout=0.05)

    with pytest.raises(ServiceUnavailable):
        client.call()
    with pytest.raises(ServiceUnavailable):
        client.call()

    calls_before_open = service.calls

    with pytest.raises(CircuitOpenError):
        client.call()

    assert service.calls == calls_before_open


def test_circuit_recovers_after_reset_timeout():
    service = FlakyService(fail_times=100)
    client = ResilientClient(service, max_retries=1, failure_threshold=1, reset_timeout=0.05)

    with pytest.raises(ServiceUnavailable):
        client.call()

    with pytest.raises(CircuitOpenError):
        client.call()

    service.fail_times = 0
    time.sleep(0.06)

    assert client.call() == "ok"
