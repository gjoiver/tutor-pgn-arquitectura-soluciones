# diagnostico · f4-vpc-debug — Depurar una red pública/privada mal configurada

- Herramienta: Terraform (HCL), AWS provider
- Tipo: debug
- Tiempo objetivo: 15 min
- Directorio de trabajo: `ejercicios/diagnostico/f4-vpc-debug/`

## Objetivo
`network.tf` describe una VPC con una subred pública y una subred privada donde
vive una base de datos RDS. La intención declarada es que la subred privada
**no sea alcanzable desde internet**. El archivo tiene 3 errores que rompen esa
garantía o que simplemente no son válidos en AWS. Encuéntralos y corrígelos.

## Paso a paso

0. **Preparación** — el archivo `network.tf` ya existe en este directorio con
   los 3 errores. No necesitas desplegar nada ni tener credenciales de AWS
   configuradas para este ejercicio.
1. Lee `network.tf` completo. Para cada recurso, pregúntate: ¿esto hace lo que
   dice el comentario o el nombre que le pusieron?
2. Encuentra los 3 errores. Pista de dónde mirar (no de qué está mal): el
   recurso `aws_nat_gateway`, la `aws_route_table` de la subred privada, y el
   `aws_security_group` de la base de datos.
3. Corrige el archivo directamente.
4. Crea `ejercicios/diagnostico/f4-vpc-debug/justificacion.md` explicando, por
   cada error corregido: qué estaba mal, por qué (qué garantía rompía), y qué
   cambiaste.
5. **Verifica** (opcional, si tienes Terraform instalado):
   ```bash
   terraform init && terraform validate
   ```
   Esto solo confirma sintaxis válida — no valida que el diseño sea correcto,
   eso lo reviso yo contra tu `justificacion.md`.

## Cómo se evalúa
Reviso `network.tf` corregido y `justificacion.md` contra estos 3 puntos:
1. La subred privada ya no tiene ruta directa al Internet Gateway.
2. El NAT Gateway ya no referencia un security group (no es un atributo válido
   del recurso).
3. El security group de la base de datos ya no acepta `0.0.0.0/0` en el
   puerto de Postgres.

## Pistas
Pídelas al tutor: son escalonadas y no están escritas aquí a propósito.
