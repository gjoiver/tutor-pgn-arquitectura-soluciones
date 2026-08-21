"""Resilient client: retry + circuit breaker over a flaky external service."""

import time


class ServiceUnavailable(Exception):
    pass


class CircuitOpenError(Exception):
    pass


class FlakyService:
    """Simulates an external service that fails its first `fail_times` calls."""

    def __init__(self, fail_times: int):
        self.fail_times = fail_times
        self.calls = 0

    def call(self):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise ServiceUnavailable(f"call {self.calls} failed")
        return "ok"


class ResilientClient:
    """
    Wraps calls to an external service with retry and a circuit breaker.

    TODO: implement `call()` so that:
      1. If the circuit is open and less than `reset_timeout` seconds have
         passed since it opened, raise CircuitOpenError immediately WITHOUT
         calling `self.service.call()`.
      2. Otherwise, attempt `self.service.call()` up to `max_retries` times
         (a single "call()" invocation may retry internally).
      3. If an attempt succeeds, reset `consecutive_failures` to 0, close the
         circuit (circuit_open_at = None), and return the result.
      4. If all `max_retries` attempts fail, increment `consecutive_failures`
         by 1 for this invocation. If `consecutive_failures` reaches
         `failure_threshold`, open the circuit (set `circuit_open_at` to the
         current time) and raise the last ServiceUnavailable exception.
    """

    def __init__(
        self,
        service,
        max_retries: int,
        failure_threshold: int,
        reset_timeout: float,
    ):
        self.service = service
        self.max_retries = max_retries
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.consecutive_failures = 0
        self.circuit_open_at = None

    def call(self):
        # TODO: implement per the docstring above.
        raise NotImplementedError
