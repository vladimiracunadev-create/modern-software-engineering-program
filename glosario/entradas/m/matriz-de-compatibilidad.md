# Matriz de compatibilidad

[↑ Glosario](../../README.md) · [← Matriz de autorización](./matriz-de-autorizacion.md) · [Matriz de compromisos →](./matriz-de-compromisos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

Se prueba runtime mínimo/máximo, instalación desde wheel/sdist, consumidor anterior con release nuevo y plugin compatible/incompatible.

Definición de trabajo de [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md).

## Por qué importa

En [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), el tema «Matriz de compatibilidad» importa porque se prueba runtime mínimo/máximo, instalación desde wheel/sdist, consumidor anterior con release nuevo y plugin compatible/incompatible.

## Cómo funciona

Según [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), en la sección «Matriz de compatibilidad»:

Se prueba runtime mínimo/máximo, instalación desde wheel/sdist, consumidor anterior con release nuevo y plugin compatible/incompatible. Una matriz verde respalda solo combinaciones ejecutadas; las demás se marcan no verificadas.

Según [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), en la sección «Matriz de compatibilidad»:

Se definen cinco versiones de un mensaje: v1 con identificador, estudiante y nota numérica; v2 añade un comentario opcional; v3 renombra «estudiante» a «alumno»; v4 cambia la nota a texto; v5 añade un estado. Cada versión tiene un productor y un lector. Un lector estricto exige exactamente los campos de su versión y rechaza los desconocidos y los estados que no conoce; uno tolerante exige solo los campos que necesita e ignora los demás. Se ejecutan los 25 pares con mensajes producidos de verdad.

El lector estricto es compatible en 7 pares de 25 y el tolerante en 9. El tolerante gana dos: leer un mensaje v2 con un lector v1 (campo añadido) y leer un v5 con un lector v4. Los cambios v3 (renombrar) y v4 (cambiar el tipo) rompen con los dos tipos de lector: la tolerancia absorbe lo aditivo y no lo destructivo. Para una evolución sin ruptura, un renombrado necesita el patrón expandir-contraer de `SE-354`: durante un periodo el productor emite los dos nombres y los lectores migran antes de quitar el viejo.

**Cómo leer la figura.** Cada grupo es la versión que produce el mensaje y cada barra, cuántos de los cinco lectores lo aceptan: en rojo con lector estricto y en verde con tolerante. Mira primero en qué grupos la barra verde supera a la roja: solo en los cambios aditivos. **Dónde deja de valer:** son cinco versiones sintéticas con cuatro cambios elegidos para ilustrar cada clase; un esquema real tiene campos anidados, valores por defecto, enumeraciones que crecen y consumidores que dependen del orden. Un lector tolerante que ignora un campo requerido en secreto pasaría esta matriz sin avisar.

## Ejemplo

Ejemplo de [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) (sección «Ejemplo profesional»):

El equipo escribe el contrato del mensaje de entrega que consumen el portal, el sistema de calificaciones y un script de los docentes. El contrato fija: identificadores como cadenas, texto en UTF-8 normalizado a NFC en el borde, nota como entero en décimas, fechas en ISO 8601 con zona, `schema_version` en cada mensaje y la política de lectura: los consumidores ignoran campos desconocidos y rechazan estados que no conocen con un valor por defecto «desconocido». El productor emite siempre el campo viejo y el nuevo durante dos versiones.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md)) son:

- **Un cambio «interno» rompe a un consumidor sin que ninguna prueba falle** — causa: la promesa no estaba escrita como prueba de contrato. Corrección: escribir la prueba desde el consumidor y añadirla al conjunto.
- **La comparación de API marca un cambio que no importa** — causa: se compara toda la superficie sin distinguir lo público. Corrección: definir `__all__` o una lista pública y comparar solo eso.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md)) son: Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El proyecto acredita un release candidato dentro de su matriz, no disponibilidad, seguridad o soporte productivo. La [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) cambiará el foco desde construir correctamente hacia descubrir qué problema y resultado de producto justifican la siguiente inversión.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Complemento](../c/complemento.md), [Runtime](../r/runtime.md), [Aceptación desde el consumidor](../a/aceptacion-desde-el-consumidor.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Contrato multicapa](../c/contrato-multicapa.md), [Interoperabilidad](../i/interoperabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-119](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Matriz de autorización](./matriz-de-autorizacion.md) · [Matriz de compromisos →](./matriz-de-compromisos.md)
