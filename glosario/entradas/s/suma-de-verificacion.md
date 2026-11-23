# Suma de verificación

[↑ Glosario](../../README.md) · [← Sujeto](./sujeto.md) · [Suma de verificación por rango →](./suma-de-verificacion-por-rango.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Huella criptográfica del contenido de un archivo, usada para detectar alteraciones.

Definición de trabajo de [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md).

## Por qué importa

La clase donde se define, [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), existe con este propósito: la clase existe para que retires un sistema sin romper a quien aún lo usa, sin guardar datos que ya no deberías tener y sin perder los que debes conservar.

## Cómo funciona

Según [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md):

Un archivo almacenado durante años puede alterarse por un fallo de soporte, un error de copia o un cambio malintencionado. Una **suma de verificación** (una huella criptográfica del contenido) permite detectar cualquier alteración: se calcula al archivar, se guarda aparte y se recalcula al leer. Dos precisiones. Un lector que interpreta el archivo no es un verificador de integridad: un bit cambiado dentro de un número deja un archivo válido con otro valor, y el lector lo acepta sin queja. Y una suma no sirve si se guarda junto al archivo y puede alterarse a la vez. Además de la huella, hace falta una **prueba de restauración**: restaurar el archivo en un entorno limpio, leerlo con las instrucciones documentadas y comparar contenido.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el inventario de consumidores del módulo: 11 aplicaciones, 3 informes programados y, tras preguntar a las áreas, dos consultas manuales (una anual de finanzas y otra trimestral de la coordinación académica). Fija una ventana de observación de 400 días, desactiva la lectura por etapas con aviso y mantiene el sistema apagado pero restaurable durante noventa días.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un valor cambió y nadie lo vio** — causa: solo se comprobó que el lector leía. Corrección: suma de verificación guardada aparte y recalculada. ([SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con cifras idénticas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](../h/huella.md), [Disposición](../d/disposicion.md), [Periodicidad](../p/periodicidad.md), [Retención](../r/retencion.md), [Retención legal](../r/retencion-legal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-88 Rev. 1](https://csrc.nist.gov/pubs/sp/800/88/r1/final) — saneamiento de medios; autoridad: NIST.
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — limitación del plazo de conservación; autoridad: Unión Europea (no es asesoría legal).
- [CCSDS 650.0-B-2, OAIS](https://public.ccsds.org/Pubs/650x0m2.pdf) — modelo de referencia de archivo a largo plazo; autoridad: CCSDS.
- [Library of Congress: Recommended Formats Statement](https://www.loc.gov/preservation/resources/rfs/) — criterios de formatos para preservación; autoridad: Library of Congress.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — base embebida usada como formato de archivo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Sujeto](./sujeto.md) · [Suma de verificación por rango →](./suma-de-verificacion-por-rango.md)
