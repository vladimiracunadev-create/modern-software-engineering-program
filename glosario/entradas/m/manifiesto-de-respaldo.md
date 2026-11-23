# Manifiesto de respaldo

[↑ Glosario](../../README.md) · [← Manifiesto de operabilidad](./manifiesto-de-operabilidad.md) · [Maniobra inversa de Conway →](./maniobra-inversa-de-conway.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Descripción estructurada del método, el intervalo, la retención, el destino, la verificación y los objetivos medidos de las copias.

Definición de trabajo de [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

## Por qué importa

La clase donde se define, [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), existe con este propósito: el proyecto existe para que entregues la capa de datos de la plataforma como un paquete que otra persona pueda operar, cambiar y recuperar, con sus invariantes, su plan de migraciones, sus objetivos de recuperación medidos y una lista honesta de lo que ninguna prueba ni validador ve.

## Cómo funciona

Según [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md):

El paquete es el conjunto de artefactos que permiten operar la capa de datos: el esquema con su catálogo de invariantes (restricciones y pruebas), las migraciones en fases con sus invariantes de datos, el catálogo de índices con la consulta que justifica cada uno, la política de distribución y de caché (qué se replica, qué se cachea, con qué frescura), el manifiesto de respaldo (método, intervalo, retención, destino, verificación, objetivos medidos) y el inventario de datos personales con su ciclo de vida. Lo que lo distingue de una carpeta de documentos es que cada afirmación tiene una prueba que se puede ejecutar y que las piezas son coherentes entre sí.

Según [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md):

El equipo entrega `paquete-datos/` con una estructura fija. `esquema/` contiene `schema.sql` con cada restricción comentada con su invariante y la prueba que intenta violarla. `migraciones/` contiene las fases numeradas, con sus invariantes de datos y la marca del punto de no retorno. `acceso/` contiene el catálogo de consultas con su plan y el índice que cada una justifica. `distribucion/` fija que se usa una réplica de lectura con la garantía de leer lo propio y define la política de caché por dato con su frescura máxima. `recuperacion/` contiene el manifiesto de respaldo (copia con la API del motor, bitácora cada 5 minutos, retención de 14 días, destino en otra región, clave custodiada aparte), el procedimiento de restauración paso a paso y el informe del último ensayo con el tiempo medido.

## Ejemplo

Ejemplo de [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) (sección «Ejemplo profesional»):

El equipo entrega `paquete-datos/` con una estructura fija. `esquema/` contiene `schema.sql` con cada restricción comentada con su invariante y la prueba que intenta violarla. `migraciones/` contiene las fases numeradas, con sus invariantes de datos y la marca del punto de no retorno. `acceso/` contiene el catálogo de consultas con su plan y el índice que cada una justifica. `distribucion/` fija que se usa una réplica de lectura con la garantía de leer lo propio y define la política de caché por dato con su frescura máxima.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) son:

- **El paquete pasa el validador y la restauración falla** — causa: evidencia que no es de este entorno. Corrección: restauración automática con evidencia identificada.
- **Un invariante figura en el catálogo y no se ejecuta** — causa: lista sin prueba asociada. Corrección: una prueba por invariante que intenta violarla.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) son: Las definiciones son operativas para el proyecto. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos y semillas fijas en Windows y Ubuntu (WSL2); las cifras fueron idénticas salvo los bytes comprimidos, que difirieron menos de un 1 % por la versión de zlib.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo](../i/intervalo.md), [Retención](../r/retencion.md), [Verificación](../v/verificacion.md), [Bitácora de cambios](../b/bitacora-de-cambios.md), [Límite declarado](../l/limite-declarado.md), [Paquete de capa de datos](../p/paquete-de-capa-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

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

[↑ Glosario](../../README.md) · [← Manifiesto de operabilidad](./manifiesto-de-operabilidad.md) · [Maniobra inversa de Conway →](./maniobra-inversa-de-conway.md)
