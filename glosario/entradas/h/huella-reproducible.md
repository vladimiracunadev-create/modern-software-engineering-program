# Huella reproducible

[↑ Glosario](../../README.md) · [← Huella o digest](./huella-o-digest.md) · [Huérfano →](./huerfano.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Resumen criptográfico del paquete que no depende del sistema operativo ni del orden de lectura.

Definición de trabajo de [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

## Por qué importa

La clase donde se define, [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), existe con este propósito: el proyecto existe para entregar un paquete que otra persona pueda revisar sin pedir contexto: intenciones, requisitos, contratos, ejemplos y pruebas enlazados entre sí, con una comprobación mecánica de que los enlaces existen y no se han movido, una estimación de cuánto alcanza un cambio y una huella reproducible del conjunto.

## Cómo funciona

[SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md):

En la plataforma, el paquete vive en una carpeta con un archivo por artefacto (cabecera con identificador, tipo y enlaces, y cuerpo) y un manifiesto con las huellas. Un validador de integración continua comprueba enlaces, tipos, cobertura, ciclos y huellas, y falla con el identificador y el motivo; un segundo paso calcula el alcance de los artefactos modificados en cada cambio y lo escribe en la descripción de la revisión. Los archivos se escriben con saltos de línea fijos, y un `.gitattributes` evita conversiones.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)) son:

- **Un revisor no sabe qué ejemplo respalda una cláusula** — causa: faltan enlaces entre contrato y ejemplo. Corrección: exigir cobertura en ambos sentidos y comprobarla en integración continua.
- **Al renombrar un artefacto se rompen enlaces** — causa: los identificadores dependen del título. Corrección: identificadores estables y comprobación de enlaces colgantes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): mutaciones y alcance idénticos, huella distinta con el modo de texto por defecto e idéntica con el salto de línea fijo, tiempos distintos. El paquete es sintético, el validador comprueba forma y huellas, y los grafos de alcance son supuestos del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](../s/sistema-operativo.md), [Huella](./huella.md), [Paquete](../p/paquete.md), [Alcance de un cambio](../a/alcance-de-un-cambio.md), [Análisis de impacto](../a/analisis-de-impacto.md), [Manifiesto](../m/manifiesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gotel y Finkelstein, «An analysis of the requirements traceability problem» (ICRE, 1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad de requisitos; autoridad: IEEE International Conference on Requirements Engineering.
- [Cleland-Huang et al., «Software traceability: trends and future directions» (FOSE, 2014)](https://doi.org/10.1145/2593882.2593891) — técnicas de creación y mantenimiento de enlaces; autoridad: ACM Future of Software Engineering.
- [FIPS 180-4: Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — especificación de SHA-256; autoridad: NIST.
- [Git: gitattributes](https://git-scm.com/docs/gitattributes) — control de los saltos de línea y de las conversiones; autoridad: proyecto Git.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — requisitos, configuración y calidad de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Huella o digest](./huella-o-digest.md) · [Huérfano →](./huerfano.md)
