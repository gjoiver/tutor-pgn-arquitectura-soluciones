---
description: Sesión de estudio de ~30 minutos siguiendo el roadmap
---
Ejecuta el protocolo /sesion definido en CLAUDE.md, paso a paso: apertura → repasos → concepto → ejercicio → cierre.

Argumentos: $ARGUMENTS
- Si viene un topic_id, úsalo como tema del día SOLO si sus prerequisitos y los tópicos anteriores necesarios están en `aprendido` o mejor; si no, explica por qué y propone el tópico correcto según `posicion_actual`.
- Si viene vacío, continúa desde `posicion_actual`.

La teoría del tópico del día no va en el chat: escríbela en `ejercicios/fase-N/<topic_id>/leccion.md` (formato en `ejercicios/_plantilla/leccion.md`) y en el chat solo pide leerla y responder las preguntas ahí mismo.

Recuerda: el cierre es obligatorio aunque el ejercicio quede a medias — actualizar `state/progress.json`, la nota de cada tópico tocado en `material/` (apuntes, errores, frontmatter de estado, links según la regla), la nota de sesión `material/sesiones/YYYY-MM-DD.md`, commit y push.
