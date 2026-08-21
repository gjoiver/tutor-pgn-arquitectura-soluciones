# Sesión pausada — 2026-08-20 23:41

## Proceso en curso
`/diagnostico` — sesión 0. No es una sesión de estudio normal: estamos ubicando
al estudiante en el roadmap. Punto exacto: **verificación por fase**, fase
actual **F3 (Diseño de software y patrones)**, en el paso de "concepto ya
respondido, ejercicio de verificación en curso".

## Cubierto hasta ahora
- **Autoevaluación completa** (F1-F8): F1 a F5 parcial, F6 ninguna, F7 no, F8 no.
- **F5 (Seguridad) — verificado y reprobado.** 3 preguntas conceptuales (JWT
  `alg: none`, por qué SHA-256 solo no basta para passwords, STRIDE de un IDOR)
  respondidas todas "no sé". Sin evidencia de conocimiento real. No se marcó
  ningún tópico como `visto` (el diagnóstico no enseña, solo verifica).
- **F4 (Nube/AWS) — verificado, resultado mixto → `visto`.**
  - Conceptual: VPC pública/privada con confusión real entre route tables y
    security groups; RDS gestionado explicado de forma superficial; Lambda vs
    EC2 por patrón de carga, sólido.
  - Ejercicio `ejercicios/diagnostico/f4-vpc-debug/`: corrigió los 3 bugs del
    `network.tf` (NAT Gateway sin SG, ruta de la subred privada, SG de la BD),
    pero necesitó 2 rondas de pistas específicas, incluida una donde señalé
    directamente `nat_gateway_id` vs `gateway_id`. Con ese nivel de ayuda, el
    tópico queda máximo en `visto`, no `aprendido`.
- **F3 (Diseño de software) — conceptual hecho, ejercicio de código pendiente.**
  - Q1 (resiliencia): nombra bien circuit breaker / timeout / retry y qué
    resuelve cada uno, pero el orden de interacción está confundido (dijo
    retry → timeout → circuit breaker).
  - Q2 (monolito modular vs microservicios): respuesta sólida y bien
    justificada.
  - Q3 (ADR: consecuencias vs alternativas descartadas): se desvió — respondió
    sobre trade-offs de atributos de calidad (correcto en sí, pero no es lo
    que se preguntó). No demostró entender la diferencia real entre esas dos
    secciones de un ADR. Pendiente de retomar o registrar como debilidad.

## Ejercicio en curso
`ejercicios/diagnostico/f3-resiliencia/` (tipo completar, Python).
- `starter.py`: método `ResilientClient.call()` **sin implementar**
  (`raise NotImplementedError`). El estudiante aún no ha empezado a escribirlo.
- `test_starter.py`: 4 tests ya validados por mí contra una implementación de
  referencia (pasan en verde) — no se han corrido todavía con el código del
  estudiante.
- Comando de verificación: `uv run --with pytest python -m pytest test_starter.py -q`
  (correr desde `ejercicios/diagnostico/f3-resiliencia/`).
- No se ha dado ninguna pista todavía para este ejercicio.

## Repasos
No aplica — estamos en `/diagnostico`, no hay `next_review` poblado todavía
(`topicos` sigue vacío en `progress.json`; el status por tópico se escribe
solo al cierre completo del diagnóstico).

## Siguiente paso concreto al retomar
Pedir al estudiante que implemente `ResilientClient.call()` en
`ejercicios/diagnostico/f3-resiliencia/starter.py` y corra los tests; si pasan,
cerrar F3 con el resultado combinado (conceptual + ejercicio) y seguir la
verificación descendente con **F2** y luego **F1** (las fases restantes
marcadas "parcial").
