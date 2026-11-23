# Paquete de capa de datos

[↑ Glosario](../../README.md) · [← Paquete de aseguramiento](./paquete-de-aseguramiento.md) · [Paquete de evidencia →](./paquete-de-evidencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Conjunto de artefactos y pruebas que permiten operar, cambiar y recuperar la capa de datos de un sistema.

Definición de trabajo de [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

## Por qué importa

En [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), el tema «Paquete de capa de datos» importa porque reúne decisiones dispersas en algo operable.

## Cómo funciona

Según [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), en la sección «Paquete de capa de datos»:

El paquete es el conjunto de artefactos que permiten operar la capa de datos: el esquema con su catálogo de invariantes (restricciones y pruebas), las migraciones en fases con sus invariantes de datos, el catálogo de índices con la consulta que justifica cada uno, la política de distribución y de caché (qué se replica, qué se cachea, con qué frescura), el manifiesto de respaldo (método, intervalo, retención, destino, verificación, objetivos medidos) y el inventario de datos personales con su ciclo de vida. Lo que lo distingue de una carpeta de documentos es que cada afirmación tiene una prueba que se puede ejecutar y que las piezas son coherentes entre sí.

## Ejemplo

Ejemplo de [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) (sección «Caso conductor»):

La capa de datos de la plataforma de entregas es el caso conductor de la [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), y esta clase deja el artefacto final: el paquete de capa de datos recuperable. Sirve de base a la [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), donde los datos que esta parte protege empiezan a circular entre servicios por mensajes y eventos. Cambia después una sola decisión, la retención de las copias, y observa qué cambia en el costo, en la cadena de restauración y en lo que se puede recuperar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) son:

- **El paquete pasa el validador y la restauración falla** — causa: evidencia que no es de este entorno. Corrección: restauración automática con evidencia identificada.
- **Un invariante figura en el catálogo y no se ejecuta** — causa: lista sin prueba asociada. Corrección: una prueba por invariante que intenta violarla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) son: Las definiciones son operativas para el proyecto. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos y semillas fijas en Windows y Ubuntu (WSL2); las cifras fueron idénticas salvo los bytes comprimidos, que difirieron menos de un 1 % por la versión de zlib.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Capa](../c/capa.md), [Conjunto](../c/conjunto.md), [Bitácora de cambios](../b/bitacora-de-cambios.md), [Límite declarado](../l/limite-declarado.md), [Manifiesto de respaldo](../m/manifiesto-de-respaldo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planes de contingencia, objetivos y pruebas; autoridad: NIST.
- [SQLite: API de copia en línea](https://www.sqlite.org/backup.html) — copia consistente; autoridad: documentación oficial de SQLite.
- [SQLite: PRAGMA](https://www.sqlite.org/pragma.html) — comprobaciones de integridad; autoridad: documentación oficial de SQLite.
- [Python: zlib](https://docs.python.org/3/library/zlib.html) — compresión usada para medir el costo de las copias; autoridad: documentación de Python.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — compromisos de diseño de sistemas de datos; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Paquete de aseguramiento](./paquete-de-aseguramiento.md) · [Paquete de evidencia →](./paquete-de-evidencia.md)
