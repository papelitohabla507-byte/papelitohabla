# Guía de contribución

1. Crea tu rama desde `develop`: `feature/PH-xx-descripcion`.
2. Escribe los commits con la clave de Jira: `PH-xx: descripción del cambio`.
3. Abre un pull request hacia `develop`. GitHub Actions ejecuta flake8, Bandit y pytest con cobertura.
4. Otro integrante revisa y aprueba el pull request antes de fusionarlo.
5. Al cerrar cada sprint, `develop` se fusiona en `main` y se etiqueta la versión (`v0.1`, `v0.2`, ...).

## Definición de Hecho

- Pull request revisado y aprobado.
- Pruebas automatizadas en verde y cobertura de al menos 80 %.
- Bandit sin hallazgos altos.
- Criterios de aceptación verificados por QA y documentación actualizada.
