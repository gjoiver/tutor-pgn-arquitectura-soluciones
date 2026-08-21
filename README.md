# Tutor Arquitectura de Soluciones para el Estado colombiano — con Claude Code

Repo-tutor personal: Claude Code actúa como tutor de Arquitectura de Soluciones para el Estado colombiano siguiendo el roadmap de `docs/roadmap.md`, con sesiones de ~30 minutos en las que **siempre se produce trabajo verificable**. Todo el estado vive en el repo, así que puedes continuar desde cualquier PC con acceso a él.

## Requisitos

- Git y un repo privado (GitHub/GitLab)
- Claude Code — funciona en la terminal y en VS Code: https://docs.claude.com/en/docs/claude-code/overview
- Docker y Docker Compose
- Python 3.11+ (o Java 17+) y un cliente de PostgreSQL (`psql`)
- Terraform
- Archi (modelado ArchiMate, gratuito): https://www.archimatetool.com
- Cuenta AWS de capa gratuita (solo desde la Fase 4)
- Obsidian para el vault de `material/` (opcional)

## Instalación (una sola vez)

```bash
unzip tutor-pgn-arquitectura-soluciones.zip && cd tutor-pgn-arquitectura-soluciones
claude
> /setup
```

`/setup` inicializa git, te pide crear un repo privado vacío (GitHub/GitLab) y pegarle la URL, hace el primer push y te guía con el troubleshooting si algo falla. Hasta que `/setup` no termine bien, el tutor no ejecuta `/diagnostico` ni `/sesion`.

## Primera vez

```bash
> /diagnostico
```

El tutor te ubica en el roadmap: autoevaluación por fases + verificación con ejercicios reales. Puede tomar 1-3 sesiones; el avance queda guardado. Al terminar, `state/progress.json` refleja tu punto de partida real.

## Flujo de cada sesión

```bash
git pull      # traes el estado más reciente
claude
> /sesion
```

Al cierre, el tutor actualiza el estado, escribe apuntes y bitácora, y hace **commit + push** por ti. En otro PC: clonar, `git pull`, `/sesion`, y sigues exactamente donde ibas.

## Comandos

| Comando | Qué hace |
|---|---|
| `/setup` | Configuración inicial: conectar el repo de progreso (una sola vez) |
| `/diagnostico` | Sesión 0: ubicarte en el roadmap |
| `/sesion` | Sesión de estudio de ~30 min (`/sesion <topic_id>` fuerza un tópico); si hay una sesión pausada, la retoma con recap |
| `/break` | Pausar la sesión en curso guardando el contexto en el remoto |
| `/repaso` | Sesión corta (~15 min) solo de repasos vencidos |
| `/estado` | Resumen de progreso, solo lectura |
| `/fase` | Estado de una fase + fecha tentativa de cierre según tu ritmo |
| `/config` | Ajustar el tutor (commands, roadmap, reglas) y publicar el cambio |

## Estructura

```
tutor-pgn-arquitectura-soluciones/
├── CLAUDE.md              # instrucciones del tutor (se cargan solas)
├── roadmap/roadmap.yaml   # currículo estructurado (59 tópicos, 8 fases)
├── docs/roadmap.md        # versión humana del roadmap, con fuentes
├── state/
│   ├── progress.json      # fuente de verdad de tu avance (lo escribe el tutor)
│   └── sesion_en_curso.md # solo existe si hay una sesión pausada con /break
├── material/              # vault de Obsidian: notas por tópico + notas de sesión
│   ├── .obsidian/         # config del vault (grafo coloreado por estado), versionada
│   ├── fase-N/            # una nota por tópico, con wikilinks y frontmatter
│   └── sesiones/          # una nota-bitácora por sesión (hubs del grafo)
├── ejercicios/            # enunciados, esqueletos, tests y tus soluciones
│   └── _plantilla/        # formato estándar de ejercicio
└── labs/                  # infraestructura local para ejercicios (si aplica)
```

## Visualizar en Obsidian

Abre `material/` como vault ("Open folder as vault"). La vista de grafo muestra
los tópicos coloreados por estado (gris = no visto, ámbar = visto, verde-azulado =
aprendido, morado = dominado) y las sesiones en coral conectando lo que se usó
junto — la config ya viene en `material/.obsidian/` y se comparte entre tus PCs
vía git (solo el estado de ventanas queda fuera). Las mismas notas se leen como
markdown plano desde VS Code.

## Reglas del juego (resumen)

- **Aquí se produce**: cada tópico exige trabajo tuyo; el tutor lo ejecuta o revisa — no acepta "ya lo hice".
- La teoría no llega por el chat: cada tópico nuevo trae su `leccion.md` (contenido + preguntas). La lees en tu editor y respondes las preguntas en el chat.
- `dominado` solo se gana en una sesión **posterior**, superando recuperación activa sin ayuda.
- `state/progress.json` lo escribe únicamente el tutor, al cierre de cada sesión.
- Si pides la solución completa, el tópico no avanza esa sesión: te espera una variante del ejercicio.
