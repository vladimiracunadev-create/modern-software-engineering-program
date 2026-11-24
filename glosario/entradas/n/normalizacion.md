# Normalización

[↑ Glosario](../../README.md) · [← Nonce](./nonce.md) · [Normalización por sintaxis →](./normalizacion-por-sintaxis.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

**Normalización** es la transformación de datos hacia una forma canónica ([SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md)). El programa la usa con dos sentidos distintos:

- **Normalización de texto Unicode** ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)): conversión a una forma definida (NFC, NFD…) para que cadenas que se ven iguales comparen iguales.
- **Normalización de datos relacionales** ([SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md)): organización de los datos de modo que cada hecho se guarde en un único lugar.

Ambos persiguen una sola representación por cosa, pero operan en dominios distintos.

## Por qué importa

Sin normalizar, dos representaciones del mismo valor se tratan como distintas: búsquedas que fallan, duplicados, actualizaciones inconsistentes. [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) lo muestra con texto; [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) con tablas, donde repetir un hecho en varios lugares permite que se contradigan.

## Cómo funciona

**Texto** ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)): `"José"` compuesto y `"José"` (la `e` más un acento combinante) son canónicamente equivalentes; tras NFC comparan iguales. Pero la normalización resuelve solo una parte: `ß` en mayúsculas es `SS`, con lo que `len` cambia; para comparar sin distinguir mayúsculas conviene `casefold()` y no `lower()`; algunos pliegues dependen del idioma (la «i» turca), y ninguna función universal los resuelve sin contexto.

**Datos** ([SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md)): se reorganizan las tablas para que cada hecho viva en un lugar: un dato de curso se guarda una vez y las entregas lo referencian, en lugar de repetirlo en cada fila.

## Ejemplo

```python
import unicodedata
a, b = "José", "José"
a == b                                     # False
unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b)   # True
```

[SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) corre ese fallo controlado: como claves de un diccionario, las dos cadenas se tratan como distintas y una búsqueda falla. Corrección: normalizar con NFC al entrar, comparar con la misma forma y documentar qué campos se normalizan.

## Errores y confusiones comunes

- **Normalización universal.** Causa: no considerar el dominio; corrección: elegir forma y campos con criterio explícito ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)).
- **Creer que NFC unifica caracteres parecidos.** No unifica la `a` latina (U+0061) con la `а` cirílica (U+0430): eso exige una política de repertorio permitido, no de normalización ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)).
- **Confundir los dos sentidos.** Normalizar texto no es normalizar tablas.

## Límites y cuándo no aplica

La normalización de texto no impide la suplantación visual (un nombre de usuario o un dominio puede suplantar a otro sin que una persona lo note). Normalizar tablas al máximo puede costar rendimiento en consultas que unen muchas tablas; a veces se desnormaliza con criterio. Y normalizar es una decisión por campo: aplicarla a contraseñas, identificadores o datos que deben conservarse tal cual puede ser incorrecto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hecho](../h/hecho.md), [Organización](../o/organizacion.md), [Codificación](../c/codificacion.md), [Comprensión](../c/comprension.md), [Conjunto](../c/conjunto.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (44 clases más lo mencionan; las que más):

[SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Codd, «A relational model of data for large shared data banks» (CACM, 1970)](https://doi.org/10.1145/362384.362685) — modelo relacional y fundamento de la normalización; autoridad: Communications of the ACM.
- [OMG: Unified Modeling Language](https://www.omg.org/spec/UML/) — especificación de la notación de modelos estructurales y conductuales; autoridad: Object Management Group.
- [Chen, «The entity-relationship model» (ACM TODS, 1976)](https://doi.org/10.1145/320434.320440) — entidades, relaciones y cardinalidades; autoridad: ACM Transactions on Database Systems.
- [The C4 model](https://c4model.com/) — vistas de la arquitectura por nivel de detalle; autoridad: autor del modelo.
- [Harel, «Statecharts» (Science of Computer Programming, 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — formalismo visual para modelos conductuales; autoridad: Science of Computer Programming.

---

[↑ Glosario](../../README.md) · [← Nonce](./nonce.md) · [Normalización por sintaxis →](./normalizacion-por-sintaxis.md)
