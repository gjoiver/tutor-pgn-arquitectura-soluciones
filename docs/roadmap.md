# Roadmap de Arquitectura de Soluciones para el Estado colombiano (2026 →)
### v2 — 8 fases, con ruta comprimida hacia el examen de octubre/noviembre 2026

Parte de una base de desarrollo de software ya adquirida y llega al nivel exigido por un cargo de **Asesor de Arquitectura de Soluciones** en una entidad pública colombiana (referencia: Convocatoria 50-2026 de la Procuraduría General de la Nación, Oficina de Tecnología, Innovación y Transformación Digital). Cada fase cierra con un criterio de dominio verificable: un entregable o artefacto revisable, no un "entendí el tema".

> **Cambio respecto a la v1:** se eliminó la fase de fundamentos de software y ciclo de vida (conocimiento ya adquirido); las fases se renumeraron de 1 a 8. Se añadió al final la **Ruta comprimida hacia el examen**, que define qué parte de este roadmap entra en la ventana agosto–noviembre 2026 y qué queda para después. Léela antes de empezar: **el orden de estudio para el examen NO es el orden de las fases.**

## Principios de diseño

1. **Profundidad sobre amplitud.** Una herramienta representativa por categoría. Un motor de base de datos, un proveedor de nube como eje y el resto por equivalencia.
2. **Primero lo que no caduca.** Modelado de datos, patrones de diseño, protocolos y marco jurídico colombiano cambian a ritmo de década; los servicios gestionados de nube cambian cada trimestre.
3. **La mitad técnica no basta.** En el sector público colombiano la arquitectura se ejerce dentro del MRAE, el Marco de Interoperabilidad, la Política de Gobierno Digital y el Estatuto de Contratación. Quien domina microservicios pero no sabe estructurar un estudio previo de TI no ejerce el cargo ni pasa la prueba.
4. **Sesgo hacia donde va el campo.** El rol se desplazó de "constructor" a "compositor": el diferencial está en el criterio de diseño y en justificar decisiones ante quien no es técnico.
5. **La IA como copiloto.** Generar código base, documentación y diagramas se automatiza. El roadmap entrena lo que no: qué arquitectura elegir, contra qué restricción legal se estrella y cómo defenderla.
6. **Certificaciones como señal, no como fin.** Dos anclas en todo el recorrido, ambas **después** del examen (ver ruta comprimida).

## Mapa general

| # | Fase | Horas est. | Certificación ancla |
|---|------|-----------|---------------------|
| 1 | Datos: modelado y gestión de bases de datos | 50 h | Ninguna |
| 2 | Sistemas operativos, redes e infraestructura | 45 h | Ninguna |
| 3 | Diseño de software y patrones de arquitectura | 70 h | Ninguna |
| 4 | Nube: diseño de soluciones y equivalencias multinube | 75 h | AWS Solutions Architect Associate (SAA-C03) |
| 5 | Seguridad de la información y del ciclo de vida | 50 h | Ninguna (opcional: ISO 27001 Foundation) |
| 6 | Arquitectura empresarial: TOGAF y MRAE | 65 h | TOGAF EA Foundation (OGEA-101) |
| 7 | Marco jurídico y gestión pública de TI | 70 h | Cursos MinTIC (hito verificable) |
| 8 | Integración: defensa de arquitectura y prueba de conocimientos | 40 h | Ninguna |

Total ≈ **465 horas** efectivas entre estudio y práctica.

---

## Fase 1 — Datos: modelado y gestión de bases de datos (~50 h)

**Objetivo:** Diseñar un modelo de datos desde el requisito de negocio hasta el esquema físico, y operarlo.

**Conceptos**
- Modelo entidad-relación; cardinalidades; los tres niveles: conceptual, lógico, físico
- Normalización 1FN → 3FN y cuándo desnormalizar deliberadamente
- SQL: consultas, joins, agregaciones, subconsultas, vistas, índices
- Transacciones y ACID; niveles de aislamiento; concurrencia
- Relacional vs. NoSQL (documental, clave-valor, columnar): criterios de elección, no preferencias
- Respaldo, restauración y recuperación ante desastres a nivel de datos
- Gobierno de datos: calidad, metadatos, diccionarios, catálogos, ciclo de vida del dato

**Tecnologías:** PostgreSQL como motor principal, un motor documental para contraste, una herramienta de modelado (dbdiagram, DBeaver o pgModeler).

**Criterio de dominio:** Entregar el modelo de datos de un sistema de trámites con al menos 12 entidades en sus tres niveles, con el script DDL ejecutable, 5 consultas SQL no triviales que respondan preguntas de negocio, y una prueba documentada de respaldo y restauración completa.

**Certificación:** ninguna necesaria en esta fase.

---

## Fase 2 — Sistemas operativos, redes e infraestructura (~45 h)

**Objetivo:** Entender qué pasa por debajo de una aplicación desplegada y poder diagnosticar dónde falla.

**Conceptos**
- Linux: sistema de archivos, permisos, procesos, servicios, logs, shell scripting básico
- Modelo TCP/IP y OSI; DNS, HTTP/HTTPS, TLS; puertos y sockets
- Direccionamiento IP, subredes, enrutamiento, NAT, firewalls; IPv6 (adopción obligatoria en entidades públicas colombianas)
- Balanceo de carga, proxy inverso, alta disponibilidad, tolerancia a fallos
- Virtualización vs. contenedores; imágenes, registries, orquestación como concepto
- Modelos de servicio (IaaS, PaaS, SaaS) y de despliegue (on-premise, nube, híbrido)
- Centro de datos: cómputo, almacenamiento, respaldo, energía, RTO y RPO

**Tecnologías:** Linux (Ubuntu o similar), Docker, Nginx, herramientas de diagnóstico (dig, curl, ss, tcpdump).

**Criterio de dominio:** Desplegar una API en contenedores detrás de un proxy inverso con HTTPS, en una red con segmentación pública/privada, y entregar un diagrama de red del montaje más un documento de 1 página que defina RTO y RPO objetivo y justifique cómo el diseño los sostiene.

**Certificación:** ninguna necesaria en esta fase.

---

## Fase 3 — Diseño de software y patrones de arquitectura (~70 h)

**Objetivo:** Elegir un estilo arquitectónico con argumentos de trade-off y documentarlo de forma que otro equipo pueda construirlo.

**Conceptos**
- Atributos de calidad: disponibilidad, escalabilidad, mantenibilidad, seguridad, desempeño, portabilidad — y por qué siempre compiten entre sí
- Estilos: monolito, monolito modular, n-capas, cliente-servidor, SOA, microservicios, event-driven, serverless
- Diseño de APIs: REST, contract-first, versionado, OpenAPI, idempotencia, paginación; API Gateway; GraphQL y gRPC como alternativas y cuándo
- Integración asíncrona: colas, tópicos, publicación-suscripción, entrega al menos una vez, patrones de reintento
- Patrones de diseño esenciales (fábrica, estrategia, repositorio, adaptador) y patrones de resiliencia (circuit breaker, bulkhead, timeout, retry con backoff)
- Arquitectura limpia / hexagonal: separación de dominio e infraestructura
- Documentación de arquitectura: vistas C4, ADR (Architecture Decision Records), diagramas de secuencia y despliegue
- Los cuatro tipos de mantenimiento (correctivo, adaptativo, perfectivo, evolutivo) y estrategias de modernización de sistemas legados — el escenario real de casi toda entidad pública

**Tecnologías:** OpenAPI/Swagger, un broker de mensajes (RabbitMQ o Kafka), Structurizr o PlantUML/Mermaid para C4, plantilla de ADR.

**Criterio de dominio:** Producir el documento de arquitectura de una solución con al menos 3 componentes integrados: diagramas C4 de contexto, contenedores y componentes; especificación OpenAPI de las interfaces; y 5 ADR que registren decisiones reales con sus alternativas descartadas y el trade-off aceptado. Debe incluir un ADR que elija explícitamente **no** usar microservicios y sustente por qué.

**Certificación:** ninguna necesaria en esta fase.

---

## Fase 4 — Nube: diseño de soluciones y equivalencias multinube (~75 h)

**Objetivo:** Diseñar una solución completa en nube optimizando los cinco pilares, y traducir cualquier diseño entre proveedores.

**Conceptos**
- Regiones, zonas de disponibilidad, modelo de responsabilidad compartida
- Identidad y accesos: usuarios, roles, políticas, principio de mínimo privilegio
- Cómputo: máquinas virtuales, contenedores gestionados, funciones sin servidor — criterios de elección por carga
- Almacenamiento: objetos, bloques, archivos; clases de almacenamiento y políticas de ciclo de vida
- Redes en la nube: red virtual, subredes, tablas de ruta, grupos de seguridad, conectividad híbrida
- Bases de datos gestionadas, réplicas de lectura, multi-AZ
- Escalado automático, balanceo, desacoplamiento con colas y notificaciones
- Los cinco pilares del marco de buena arquitectura: excelencia operativa, seguridad, fiabilidad, eficiencia de desempeño, optimización de costos
- **Equivalencias entre proveedores** (las convocatorias públicas colombianas exigen "Azure, AWS, entre otros"): cómputo, almacenamiento de objetos, funciones, red virtual, identidad, base de datos gestionada
- Infraestructura como código; estimación y control de costos

**Tecnologías:** AWS como plataforma principal (capa gratuita), Azure para el ejercicio de equivalencias, Terraform, calculadora de costos del proveedor.

**Criterio de dominio:** Desplegar una solución en la nube mediante infraestructura como código, con red segmentada, base de datos gestionada, escalado automático y almacenamiento de objetos; entregar además una tabla de equivalencias del diseño completo hacia un segundo proveedor y una estimación mensual de costos con dos escenarios de carga.

**Certificación:** **AWS Certified Solutions Architect – Associate (SAA-C03)** — programar **después** del examen del concurso (ver ruta comprimida).

---

## Fase 5 — Seguridad de la información y del ciclo de vida (~50 h)

**Objetivo:** Incorporar controles de seguridad en el diseño desde el inicio, no como capa posterior.

**Conceptos**
- Tríada confidencialidad-integridad-disponibilidad; gestión de activos de información
- Criptografía aplicada: simétrica y asimétrica, hashing, certificados, cifrado en tránsito y en reposo, gestión de llaves
- Autenticación y autorización: OAuth 2.0, OpenID Connect, JWT, MFA, federación de identidad
- OWASP Top 10 y modelado de amenazas (STRIDE)
- Seguridad en el ciclo de vida del desarrollo: análisis estático y dinámico, gestión de dependencias, secretos, DevSecOps
- Análisis de vulnerabilidades, plan de mitigación, gestión de incidentes
- Continuidad del negocio: BIA, plan de recuperación ante desastres, pruebas de continuidad
- Estándares y marcos: ISO/IEC 27001, controles NIST, y el **Modelo de Seguridad y Privacidad de la Información (MSPI)** de MinTIC — la traducción colombiana de todo lo anterior
- Protección de datos personales: Ley 1581 de 2012, tratamiento, autorización, habeas data

**Tecnologías:** OWASP ZAP, un escáner de dependencias (Trivy o Dependabot), un gestor de secretos, herramientas de análisis estático.

**Criterio de dominio:** Entregar un modelo de amenazas STRIDE de la solución construida, con al menos 10 amenazas identificadas, sus controles implementados o planificados y el riesgo residual; más el informe de un análisis de vulnerabilidades ejecutado sobre el despliegue real con su plan de mitigación priorizado.

**Certificación:** ninguna obligatoria. Opcional: ISO/IEC 27001 Foundation.

---

## Fase 6 — Arquitectura empresarial: TOGAF y MRAE (~65 h)

**Objetivo:** Subir del diseño de una solución al gobierno del portafolio: ubicar cualquier proyecto dentro de la arquitectura de una entidad y justificarlo con el marco que rige en Colombia.

**Conceptos**
- Qué distingue arquitectura de solución, arquitectura empresarial y arquitectura de sistemas de información
- TOGAF: los cuatro dominios (negocio, datos, aplicaciones, tecnología); el ciclo ADM fase por fase; repositorio, metamodelo de contenido, building blocks; gobierno de arquitectura y comités
- ArchiMate como notación de modelado
- **Marco de Referencia de Arquitectura Empresarial del Estado colombiano (MRAE v3.0)**, adoptado por la Resolución 1978 de 2023: sus tres modelos habilitadores — Modelo de Arquitectura Empresarial (MAE), Modelo de Gestión y Gobierno de TI (MGGTI) y Modelo de Gestión de Proyectos de TI (MGPTI)
- Los cinco dominios del MAE v3.0: arquitectura institucional, de información, de sistemas de información, tecnológica y de seguridad; más uso y apropiación
- PETI (Plan Estratégico de Tecnologías de la Información): qué es, quién lo aprueba, cómo se alinea con el plan estratégico institucional
- **Política de Gobierno Digital**: habilitadores (arquitectura, seguridad y privacidad, servicios ciudadanos digitales), propósitos y estructura
- **Marco de Interoperabilidad para Gobierno Digital**: sus dominios (político-legal, organizacional, semántico y técnico), el modelo de madurez de cinco niveles, el lenguaje común de intercambio y la plataforma de interoperabilidad basada en X-Road
- Gestión de servicios de TI: ITIL — incidentes, problemas, cambios, niveles de servicio, comité de cambios
- Uso y apropiación: gestión del cambio, capacitación, transferencia de conocimiento

**Tecnologías:** ArchiMate (Archi, gratuito), plantillas del MRAE publicadas por MinTIC, herramienta de gestión de servicios.

**Criterio de dominio:** Producir un ejercicio de arquitectura empresarial completo para una entidad pública ficticia: arquitectura actual (AS-IS) y objetivo (TO-BE) modeladas en ArchiMate sobre los cinco dominios del MAE, análisis de brecha, mapa de ruta priorizado, y un anexo que mapee cada decisión contra el lineamiento del MRAE que la sustenta. Debe incluir el diseño de un servicio de intercambio de información conforme al Marco de Interoperabilidad, con su nivel de madurez declarado.

**Certificación:** **TOGAF Enterprise Architecture Foundation (OGEA-101)** — programar **después** del examen del concurso.

---

## Fase 7 — Marco jurídico y gestión pública de TI (~70 h)

**Objetivo:** Operar como arquitecto dentro de las reglas del Estado: contratar tecnología, presupuestarla y responder por ella.

**Conceptos**
- Estructura del Estado colombiano; función administrativa (art. 209 de la Constitución); Ministerio Público y su naturaleza (arts. 275–284)
- Régimen del organismo de control donde se aspira al cargo — para la Procuraduría, el **Decreto Ley 262 de 2000**: estructura, funciones, carrera administrativa, listas de elegibles, reclamaciones
- **Contratación estatal**: Ley 80 de 1993 (principios, tipos de contrato, cláusulas excepcionales, supervisión e interventoría); Ley 1150 de 2007 (modalidades de selección); Decreto 1082 de 2015 (reglamentación); SECOP II y Colombia Compra Eficiente; acuerdos marco de precios para nube y software
- Estructuración de un proceso de TI: estudios previos, análisis del sector, especificaciones técnicas, criterios de evaluación, riesgos, garantías
- **Presupuesto público**: Estatuto Orgánico (Decreto 111 de 1996), principios, ciclo presupuestal, CDP y RP, vigencias futuras
- **Formulación de proyectos**: metodología de marco lógico y MGA del DNP; indicadores de producto y resultado
- **Normatividad TIC**: Ley 1341 de 2009; Decreto 1078 de 2015 (decreto único del sector); Ley 1712 de 2014 (transparencia y datos abiertos)
- Gestión documental: Ley 594 de 2000, tablas de retención documental, expediente electrónico
- Sistemas de gestión: MIPG, MECI, control interno, planes de mejoramiento
- Empleo público: carrera administrativa, concurso de méritos, período de prueba, evaluación del desempeño

**Tecnologías:** SECOP II (consulta pública de procesos reales), portal de datos abiertos, normogramas de entidades.

**Criterio de dominio:** Estructurar los estudios previos completos para contratar una solución tecnológica: necesidad, análisis del sector con al menos 3 procesos comparables extraídos de SECOP II, especificaciones técnicas derivadas de la arquitectura diseñada, modalidad de selección elegida y sustentada normativamente, matriz de riesgos, y presupuesto oficial justificado. Complementar con un cuadro que ubique cada norma citada dentro de la jerarquía normativa.

**Certificación:** ninguna paga. Hito verificable: completar los cursos gratuitos de MinTIC sobre MRAE y Política de Gobierno Digital, y el de Colombia Compra Eficiente sobre SECOP II.

---

## Fase 8 — Integración: defensa de arquitectura y prueba de conocimientos (~40 h)

**Objetivo:** Convertir el conocimiento acumulado en respuesta correcta bajo presión de tiempo y en argumento defendible ante un comité.

**Conceptos**
- Resolución de casos de arquitectura con restricciones cruzadas (presupuesto, normativa, legado, plazos)
- Comunicación de arquitectura a audiencias no técnicas: traducir "cinco nueves de disponibilidad" a costo y riesgo institucional
- Técnica de examen de opción múltiple: descarte por eliminación, identificación de la restricción dominante en el enunciado, gestión del tiempo por pregunta
- Diccionario de competencias comportamentales de la entidad; niveles de competencia y cómo se evalúan
- Estructura de la prueba: componente eliminatorio de conocimientos, componente clasificatorio de competencias, análisis de antecedentes

**Tecnologías:** bancos de preguntas de concursos públicos anteriores, simuladores, cronómetro.

**Criterio de dominio:** Sostener tres simulacros completos cronometrados con ≥ 80 % de acierto en cada bloque temático (técnico, arquitectura empresarial, jurídico-administrativo), y presentar una defensa oral de 10 minutos de la arquitectura del proyecto transversal ante audiencia no técnica, respondiendo preguntas sobre costo, riesgo y sustento normativo.

**Certificación:** ninguna.

---

## Certificaciones: orden de prioridad

| Prioridad | Certificación | Fase | Cuándo | Por qué |
|---|---|---|---|---|
| 1 | AWS Solutions Architect – Associate (SAA-C03) | 4 | Después del examen | Señal de mercado más líquida para el rol; cubre los esquemas de almacenamiento cloud del temario. |
| 2 | TOGAF EA Foundation (OGEA-101) | 6 | Después del examen | Da el vocabulario con el que está escrito el MRAE colombiano. |
| 3 | Cursos MinTIC (MRAE, Gobierno Digital) + SECOP II | 6 y 7 | **Antes del examen** | Gratuitos, específicos del contexto colombiano, y son el único material oficial del temario. |
| 4 (opcional) | Azure AZ-900 o TOGAF Practitioner (OGEA-102) | posterior | — | Solo si el empleo objetivo lo exige. |

**Regla:** máximo 2 certificaciones grandes en todo el recorrido, y **ninguna dentro de la ventana del examen** — una certificación exige 60–80 h de preparación específica que competirían justo con los bloques que deciden el concurso.

## Proyecto transversal (capstone evolutivo)

**Sistema de gestión de trámites y expedientes para una entidad pública de control.** Un solo proyecto que crece fase a fase:

- **F1:** Modelo de datos en tres niveles con expedientes, actuaciones, sujetos procesales y trazabilidad; respaldo y restauración probados.
- **F2:** Despliegue en contenedores con red segmentada, HTTPS y objetivos de RTO/RPO declarados.
- **F3:** Documento de arquitectura con vistas C4, contratos OpenAPI, integración asíncrona y bitácora de ADR.
- **F4:** Migración a nube con infraestructura como código, alta disponibilidad, escalado automático, equivalencias multinube y estimación de costos.
- **F5:** Modelo de amenazas, controles, cifrado, gestión de identidad, análisis de vulnerabilidades y plan de continuidad.
- **F6:** El sistema ubicado en una arquitectura empresarial AS-IS/TO-BE de la entidad, con análisis de brecha, mapa de ruta y un servicio de intercambio conforme al Marco de Interoperabilidad.
- **F7:** Estudios previos completos para contratar su construcción, con modalidad de selección, matriz de riesgos y presupuesto sustentado.
- **F8:** Defensa oral de todo lo anterior ante audiencia no técnica, en 10 minutos.

**Qué demuestra el resultado final:** que quien lo hizo puede tomar una necesidad institucional, diseñar la solución, sustentarla técnica y jurídicamente, calcular lo que cuesta y explicarla a quien firma.

## Estimación de tiempo según ritmo

| Ritmo semanal | Duración total aprox. |
|---|---|
| 3.5 h (solo sesiones de 30 min/día) | ~31 meses |
| 6 h (sesiones diarias + 1 bloque de práctica) | ~18 meses |
| 10 h | ~11 meses |
| 15 h | ~7.5 meses |

Las sesiones de 30 minutos sirven para teoría, lectura normativa y repaso; los criterios de dominio exigen bloques de 1 a 2 horas — ningún despliegue en nube ni ejercicio de ArchiMate cabe en media hora.

---

# Ruta comprimida hacia el examen (agosto – noviembre 2026)

## El problema, con números

| | |
|---|---|
| Roadmap completo | 465 h |
| Ventana si el examen cae a mediados de octubre | ~8 semanas → 96–120 h |
| Ventana si el examen cae a finales de noviembre | ~14 semanas → 168–210 h |

Disponible: entre el **21 % y el 45 %** del roadmap. La conclusión no es "estudiar más rápido": es **cambiar el criterio de optimización**. El roadmap completo optimiza *volverse arquitecto de soluciones*. La ruta comprimida optimiza *superar una prueba eliminatoria de 65/100 sobre un temario declarado*. Priorizan distinto y hay que elegir uno.

## Las tres reglas de la compresión

1. **Lo que ya se sabe se verifica, no se estudia.** Para las fases con base previa, el criterio de dominio se usa como *checkpoint*: si se resuelve en una sesión, la fase se cierra y no se toca más. Si no se resuelve, ahí sí hay estudio real y se agenda.
2. **Se estudia por peso en la prueba, no por orden de fases.** Los temas donde un perfil técnico ya llega fuerte tienen retorno marginal bajo por hora invertida. Los temas jurídico-administrativos y de arquitectura empresarial pública tienen retorno alto porque casi ningún candidato técnico los domina — y pesan igual en el examen.
3. **Cero certificaciones dentro de la ventana.** SAA-C03 y TOGAF se posponen. Cada una consume 60–80 h que competirían directamente con los bloques decisivos, y ninguna suma puntos en el examen.

## Plan de 14 semanas (~165 h a 12 h/semana)

Si el examen cae en octubre, se ejecutan los bloques en el mismo orden y se recorta por el final: los bloques A–D son innegociables, E y F se comprimen.

| Bloque | Semanas | Horas | Contenido | Origen |
|---|---|---|---|---|
| **A — Verificación técnica** | 1–2 | 20 h | Checkpoints de datos, redes/infraestructura y patrones de arquitectura. Se resuelven los criterios de dominio en versión reducida; lo que falle entra a la lista de refuerzo | Fases 1, 2, 3 |
| **B — Nube y equivalencias** | 3–4 | 20 h | Conceptos de los cinco pilares + **tabla de equivalencias AWS↔Azure** completa. Sin laboratorios extensos: el examen pregunta criterio de diseño, no consolas | Fase 4 |
| **C — Seguridad y datos personales** | 5–6 | 20 h | OWASP, controles en el SDLC, cifrado, gestión de identidad, **MSPI de MinTIC**, Ley 1581 | Fase 5 |
| **D — Arquitectura empresarial pública** ⭐ | 7–9 | 35 h | MRAE v3.0 y sus cinco dominios, Resolución 1978 de 2023, MGGTI, PETI, Política de Gobierno Digital, **Marco de Interoperabilidad** (dominios, modelo de madurez, X-Road), ITIL, uso y apropiación | Fase 6 |
| **E — Jurídico y gestión pública** ⭐ | 10–12 | 40 h | Decreto Ley 262 de 2000, Constitución arts. 209 y 275–284, contratación estatal (Ley 80, Ley 1150, Decreto 1082, SECOP II), presupuesto público, formulación de proyectos, Ley 1341, gestión documental, MIPG/MECI | Fase 7 |
| **F — Simulacros y comportamentales** | 13–14 | 30 h | 3 simulacros cronometrados + refuerzo dirigido por resultados + Diccionario de Competencias de la entidad | Fase 8 |

**Los bloques D y E concentran 75 de las 165 horas (45 %).** Ese es el ajuste central del plan: es donde está la brecha y donde se gana o se pierde el 65/100.

## Reglas de ejecución

- **Regla de asignación:** después de cada simulacro parcial, las horas de la semana siguiente van al bloque con menor porcentaje de acierto, sin excepción. El plan se reasigna con datos, no con preferencia.
- **Trampa a evitar:** repasar arquitectura de microservicios porque es cómodo y se domina. Cada hora ahí es una hora que no está en contratación estatal, que es donde se pierde el examen.
- **Monitoreo semanal:** revisar procuraduria.gov.co y meritoconstruyendoexcelencia.com.co cada lunes. La fecha real del examen se publica por aviso web y define si se ejecuta el plan de 14 semanas o el recorte de 8.
- **Punto de recalibración:** cuando se publique la fecha oficial del examen, recalcular la ventana y recortar desde el final, nunca desde D o E.

## Qué pasa con el resto del roadmap

Las ~300 horas que quedan fuera no se pierden: se retoman después del examen, con o sin resultado favorable. La lista de elegibles tiene vigencia de dos años y el nombramiento puede tardar, así que ese periodo es exactamente la ventana natural para AWS SAA-C03, TOGAF Foundation y el capstone completo — que sirven igual si el destino final es una entidad pública o el sector privado.

## Fuentes principales

- **MinTIC – Marco de Referencia de Arquitectura Empresarial (MRAE):** estructura del MAE v3.0, sus cinco dominios y los modelos MGGTI y MGPTI. https://www.mintic.gov.co/arquitecturaempresarial/portal/ y https://www.mintic.gov.co/arquitecturaempresarial/630/w3-propertyvalue-385293.html
- **MinTIC – Resolución 1978 de 2023:** adopción de la versión 3 del MRAE. https://sidn.ramajudicial.gov.co/SIDN/NORMATIVA/TEXTOS_COMPLETOS/8_RESOLUCIONES/RESOLUCIONES%202023/MTIC%20Resoluci%C3%B3n%2001978%20de%202023%20(Referencia%20de%20Arquitectura%20Empresarial%20para%20el%20Estado%20Colombiano).pdf
- **MinTIC – Marco de Interoperabilidad para Gobierno Digital:** dominios, modelo de madurez, plataforma de interoperabilidad y X-Road. https://lenguaje.mintic.gov.co/marco y https://lenguaje.mintic.gov.co/sites/default/files/archivos/marco_de_interoperabilidad_para_gobierno_digital.pdf
- **MinTIC – Gobierno Digital, cursos oficiales gratuitos.** https://gobiernodigital.mintic.gov.co/portal//426178:Marco-de-Referencia-de-Arquitectura-Empresarial-2026
- **The Open Group – Portafolio de certificación TOGAF:** rutas OGEA-101, OGEA-102, OGEA-103. https://www.opengroup.org/certifications/togaf-certification-portfolio
- **Guía de certificación TOGAF 2026:** estructura de exámenes, costos y carga de estudio. https://certdemand.com/guides/togaf-certification-guide
- **Skills del rol de arquitecto de soluciones en 2026.** https://interviewkickstart.com/skills/solutions-architect
- **Azure Solutions Architect (AZ-305), pesos por dominio 2026:** referencia para equivalencias multinube. https://itknowledgelab.com/blog/azure-solutions-architect-career-path-2026
- **Convocatoria 50-2026, Procuraduría General de la Nación** (documento aportado): conocimientos esenciales específicos que delimitan el alcance.
