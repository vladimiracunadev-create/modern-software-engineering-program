# Licencias y procedencia de datos

Inventario revisado el **2026-10-05**. El repositorio no contiene telemetría
productiva ni datasets con datos personales reales. Sus catálogos describen el
programa o soportan ejercicios educativos.

| Familia | Naturaleza | Licencia o condición |
| --- | --- | --- |
| `curriculum.yaml`, `catalog.json` | Arquitectura curricular y catálogo generado de 480 clases | Selección, organización y texto original bajo CC BY-NC-SA 4.0 |
| `classes/**/lesson.json` | Metadatos educativos generados por clase | CC BY-NC-SA 4.0 |
| `classes/**/activity.yaml`, `classes/**/rubric.json` | Contratos de práctica y evaluación | CC BY-NC-SA 4.0 |
| `sources/*.json`, `sources/pedagogical/*.json` | Registro factual y editorial de fuentes y relaciones | Selección y estructura originales bajo CC BY-NC-SA 4.0; hechos, identificadores y obras enlazadas conservan su condición propia |
| `manifest/repositories.json` | Fronteras y propietarios dentro de la suite | CC BY-NC-SA 4.0 para la organización editorial; nombres y repositorios externos conservan sus derechos |
| `schemas/*.json`, `blueprints/**/*.yaml` | Esquemas y contratos ejecutables | Apache-2.0 |
| `site/assets/catalog.json`, `site/schemas/*.json` | Copias generadas de los catálogos y esquemas anteriores | La misma licencia que su fuente |

Las cifras, títulos, identificadores públicos y demás hechos no adquieren una nueva
protección por aparecer en un registro. La licencia sólo cubre los derechos que el
licenciante pueda conceder sobre la selección, estructura y contenido original.

## Regla para nuevos datos

Una contribución que agregue datos debe documentar fuente, autorización, finalidad,
licencia, minimización, tratamiento de privacidad y método de generación o
anonimización. No deben publicarse credenciales, registros de producción, datos
personales, evidencias de incidentes reales ni información de terceros obtenida sin
permiso.

Los datos descargados al ejecutar una práctica no quedan licenciados por este
repositorio. Deben mantenerse fuera de Git y conservar los términos de su proveedor.

