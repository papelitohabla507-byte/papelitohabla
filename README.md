# PapelitoHabla

Sistema web de seguimiento y firma digital de documentos para los ministerios de Panamá.

Proyecto Final de **INF 224 – Metodología de Proyectos Informáticos** (Universidad de Panamá, FIEC). Profesor: Carlos Bruce.

## Funcionalidades

- Registro de documentos entrantes, salientes e internos con **número único** (`MIN-DEP-AÑO-CONSECUTIVO`) y etiqueta QR.
- Derivación entre departamentos, recepción, devolución y fechas límite.
- **Firma digital** con certificado y **sello digital por departamento**.
- Historial completo y bitácora de auditoría de cada documento.
- Consulta pública del estado del trámite, reportes y tablero de indicadores.

## Equipo

| Integrante | Rol |
|---|---|
| Brayan Abrego | Líder de proyecto / Scrum Master |
| Natanael Andrade | Backend (Django) y base de datos |
| Wesley Rivera | Infraestructura, redes y seguridad (DevOps) |
| Carlos Gutiérrez | Frontend / UX y QA |

## Tecnologías

Python 3.12 · Django 5 · PostgreSQL · Docker · GitHub Actions

## Estructura

```
apps/usuarios/     usuarios, roles y 2FA
apps/documentos/   registro, número único y adjuntos
apps/tramite/      derivación, historial y auditoría
apps/firmas/       firma digital y sellos
apps/reportes/     consultas, reportes y tablero
docs/              ADR, requisitos y manuales
tests/             pruebas automatizadas
```

## Ejecutar las pruebas

```bash
pip install -r requirements-dev.txt
pytest
```

## Flujo de trabajo

Ver [CONTRIBUTING.md](CONTRIBUTING.md). Las tareas se gestionan en Jira (proyecto **PH**).
