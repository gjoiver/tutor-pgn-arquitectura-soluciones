# diagnostico · f3-resiliencia — Cliente con retry y circuit breaker

- Herramienta: Python 3
- Tipo: completar
- Tiempo objetivo: 15 min
- Directorio de trabajo: `ejercicios/diagnostico/f3-resiliencia/`

## Objetivo
Completar `ResilientClient.call()` en `starter.py` para que envuelva las
llamadas a un servicio externo simulado (`FlakyService`) con **retry** y
**circuit breaker**, según el contrato descrito en el docstring de la clase.

## Paso a paso

0. **Preparación** — ya existen `starter.py` (con el método `call()` sin
   implementar) y `test_starter.py` (los tests que deben pasar). No necesitas
   instalar nada de forma persistente: ejecuta los tests con
   ```bash
   uv run --with pytest python -m pytest test_starter.py -q
   ```
1. Lee el docstring de `ResilientClient` en `starter.py` completo antes de
   escribir código — describe exactamente el orden de las 4 reglas.
2. Implementa `call()` en `starter.py`.
3. **Verifica**:
   ```bash
   uv run --with pytest python -m pytest test_starter.py -q
   ```
   Confirma que los 4 tests pasan.

## Convención de código
Variables, funciones, docstrings y comentarios en inglés (ya está así en el
esqueleto — mantenlo).

## Cómo se evalúa
`uv run --with pytest python -m pytest test_starter.py -q` debe pasar en
verde (4 passed). Si algún test falla, leo cuál y por qué antes de dar pistas.

## Pistas
Pídelas al tutor: son escalonadas y no están escritas aquí a propósito.
