# Referencia

[↑ Glosario](../../README.md) · [← Refactorización](./refactorizacion.md) · [Referencia de API →](./referencia-de-api.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Descripción completa y neutral de los elementos de un producto, estructurada como el producto.

Definición de trabajo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md): Nombre (rama, etiqueta, HEAD) que apunta a un commit o a otra referencia.
- En [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md): Distribución con la que se compara, normalmente la de entrenamiento o la de un periodo sano.

## Por qué importa

En [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), el tema «Referencia» importa porque describe la máquina con completitud y sin opinión; se consulta, no se lee.

En [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), el tema «Referencias» importa porque una rama o una etiqueta son nombres; mover un nombre no borra objetos, pero puede dejarlos inalcanzables.

## Cómo funciona

Según [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), en la sección «Referencia»:

La referencia describe la máquina: los parámetros, sus tipos, sus valores por defecto, los errores que puede devolver. Se consulta de forma puntual y por eso importa más que sea completa, uniforme y exacta que agradable; su estructura imita la del producto, no la de las tareas. Es el único tipo cuya exactitud puede comprobarse por completo con herramientas, porque sus afirmaciones tienen una contraparte en el código: nombres, firmas, límites. Una referencia con opiniones («recomendamos un tope del 50 %») mezcla tipos; la opinión va a una explicación o a una guía.

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), en la sección «Referencias»:

Una rama, una etiqueta y HEAD son archivos pequeños con un identificador (o con el nombre de otra referencia). Mover una rama no borra objetos: solo cambia a qué commit se llega desde ese nombre. Un objeto queda a salvo mientras sea alcanzable desde alguna referencia o desde el registro de movimientos (reflog); si deja de serlo, es candidato a la poda. Esta distinción entre «existe» y «es alcanzable» es la base de toda la recuperación de `SE-194`.

## Ejemplo

Ejemplo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sección «Ejemplo profesional»):

La plataforma separa la penalización en cuatro páginas con nombres propios: un tutorial («Tu primera entrega con retraso»), una guía («Cambiar el tope de penalización de un curso»), una referencia («Parámetros de penalización») y una explicación («Por qué la penalización es diaria y con tope»). Cada una enlaza a las otras tres en una línea al comienzo o al final. El tutorial y la guía se ejecutan en la integración continua; la referencia se genera de la configuración; la explicación se revisa cuando cambia la política. Una persona nueva empieza por el tutorial, una docente va directo a la guía y una auditora lee la explicación.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La referencia dice «se recomienda» en varios parámetros** — causa: se mezcló opinión con descripción. Corrección: trasladar las recomendaciones a una guía o una explicación. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- **Hay explicación pero nadie la encuentra** — causa: no está enlazada desde ninguna página de acción. Corrección: enlazar la explicación desde el tutorial, la guía y la referencia. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Hay componentes que solo necesitan referencia (una opción de configuración) y otros que piden explicación (una decisión de diseño). ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Producto](../p/producto.md), [Árbol](../a/arbol.md), [Blob](../b/blob.md), [Explicación](../e/explicacion.md), [Guía práctica](../g/guia-practica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (190 clases más lo mencionan; las que más):

[SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md).

**Aparece en los casos de estudio:** [Instagram](../../../casos/exito/instagram.md), [TSB Bank](../../../casos/fallo/tsb.md), [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Referencias».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.
- [Python: `inspect`](https://docs.python.org/3/library/inspect.html) — firmas de funciones para comparar con una referencia.
- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Refactorización](./refactorizacion.md) · [Referencia de API →](./referencia-de-api.md)
