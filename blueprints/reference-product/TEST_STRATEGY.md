# Estrategia de pruebas — EduProgress

| Riesgo | Nivel | Evidencia |
| --- | --- | --- |
| cálculo incorrecto | unitarias y propiedades | invariantes para 0, parcial y completo |
| acceso cruzado | integración/API | actor A no obtiene datos de B |
| duplicación por reintento | integración con base | misma clave produce una evidencia |
| contrato roto | contrato | respuestas compatibles |
| migración de datos | integración | versión anterior y nueva conviven |
| flujo inaccesible | componente/E2E | teclado, foco y mensajes |
| dependencia lenta | resiliencia | timeout, señal y recuperación |
| recuperación incompleta | ejercicio | restauración y reconciliación |

Los datos son deterministas y sintéticos. Las E2E se reservan para flujos críticos; las reglas puras se prueban sin UI ni red.
