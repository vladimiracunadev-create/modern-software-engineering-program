# Bitácora de cambios

[↑ Glosario](../../README.md) · [← Bit](./bit.md) · [Bitácora encadenada →](./bitacora-encadenada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Registro ordenado de las escrituras que permite recuperar lo ocurrido desde la última copia.

Definición de trabajo de [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

## Por qué importa

La clase donde se define, [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), existe con este propósito: el proyecto existe para que entregues la capa de datos de la plataforma como un paquete que otra persona pueda operar, cambiar y recuperar, con sus invariantes, su plan de migraciones, sus objetivos de recuperación medidos y una lista honesta de lo que ninguna prueba ni validador ve.

## Cómo funciona

Según [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md):

Una base de SQLite recibe 200 entregas por día durante 30 días y mantiene un control con la suma esperada de notas. Se inyectan dos incidentes: el día 10, un `DELETE` accidental que borra el 40 % de las filas existentes (y se descubre al instante), y el día 18, una alteración silenciosa de las notas de 68 filas que se descubre el día 21. Tres estrategias: **A**, copia diaria sin verificar con retención de 3 días; **B**, copia diaria con verificación (la suma de las notas debe coincidir con el control antes de aceptar la copia) y retención de 14 días; **C**, como B más una bitácora de cambios que permite recuperar lo insertado desde la última copia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md):

El equipo entrega `paquete-datos/` con una estructura fija. `esquema/` contiene `schema.sql` con cada restricción comentada con su invariante y la prueba que intenta violarla. `migraciones/` contiene las fases numeradas, con sus invariantes de datos y la marca del punto de no retorno. `acceso/` contiene el catálogo de consultas con su plan y el índice que cada una justifica. `distribucion/` fija que se usa una réplica de lectura con la garantía de leer lo propio y define la política de caché por dato con su frescura máxima.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) son:

- **El paquete pasa el validador y la restauración falla** — causa: evidencia que no es de este entorno. Corrección: restauración automática con evidencia identificada.
- **Un invariante figura en el catálogo y no se ejecuta** — causa: lista sin prueba asociada. Corrección: una prueba por invariante que intenta violarla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md)) son: Las definiciones son operativas para el proyecto. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos y semillas fijas en Windows y Ubuntu (WSL2); las cifras fueron idénticas salvo los bytes comprimidos, que difirieron menos de un 1 % por la versión de zlib.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Límite declarado](../l/limite-declarado.md), [Manifiesto de respaldo](../m/manifiesto-de-respaldo.md), [Paquete de capa de datos](../p/paquete-de-capa-de-datos.md), [Simulacro](../s/simulacro.md).
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

[↑ Glosario](../../README.md) · [← Bit](./bit.md) · [Bitácora encadenada →](./bitacora-encadenada.md)
