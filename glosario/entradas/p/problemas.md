# Problemas

[↑ Glosario](../../README.md) · [← Problema del oráculo](./problema-del-oraculo.md) · [Procedencia →](./procedencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

En descubrimiento de producto, un **problema** es una brecha entre lo que una persona intenta lograr y lo que logra, con una consecuencia observable y una causa que puede investigarse ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md)). Sin esos tres elementos, dice la clase, es una opinión. No es lo mismo que una solución deseada ni que un estado de ánimo.

## Por qué importa

Cambia el punto de partida de todo el trabajo posterior. Si el equipo parte de una solución («agregar un botón»), solo discute soluciones; si parte de un problema bien enunciado, puede comparar soluciones y comprobar si alguna sirvió. Un enunciado de problema que otras personas pueden confirmar o refutar permite acordar antes de construir.

## Cómo funciona

[SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) propone una estructura de enunciado: **actor** + **lo que intenta lograr** + **lo que se lo impide** + **consecuencia**. Ejemplo de la clase: «los estudiantes pierden su avance cuando la sesión expira y no pueden recuperarlo». Es **investigable** cuando existe una observación que lo confirmaría o lo refutaría (por ejemplo, registros de sesiones expiradas con borrador sin guardar). Esa observación es lo que distingue un problema de una impresión.

En contraste, «los usuarios están insatisfechos» no es un problema sino un estado de ánimo, sin actor concreto ni observable. La diferencia importa porque solo un enunciado investigable permite que otra persona llegue a la misma conclusión desde los mismos datos.

Dos fallos que la clase prevé. Primero, la reunión que discute «la solución» una hora sin acordar el problema: se aceptó la petición original como requisito; la corrección es reformular la petición como necesidad («necesito… para…») antes de proponer opciones. Segundo, el enunciado que pasa el linter pero nadie reconoce como real: la regla comprueba forma, no existencia; la corrección es pedir a una segunda persona que cite un registro o una observación que lo confirme.

## Ejemplo

En la plataforma de entregas ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md)), el análisis de tickets sintéticos muestra que la causa más frecuente es la expiración de sesión. El problema enunciado: «estudiantes que escriben una entrega larga pierden el texto al expirar la sesión y no pueden recuperarlo». La observación que lo confirmaría: registros de sesiones expiradas con borrador no guardado. Las clases siguientes preguntan quiénes son las personas afectadas ([SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md)), qué se sabe de ellas por entrevistas ([SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md)) y qué hipótesis contrastar ([SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)).

## Errores y confusiones comunes

- **Discutir la solución sin acordar el problema.**
- **Enunciado sin actor ni observable**: «es confuso» no sirve.
- **Enunciado que oculta una solución**: «falta un botón de guardar» ya es una solución.
- **Confundir problema con oportunidad**: el problema es la brecha; la oportunidad añade tamaño, frecuencia y ventana.

## Límites y cuándo no aplica

Un buen enunciado no prueba que el problema merezca resolverse: eso lo decide su tamaño y la prioridad. Algunos problemas se descubren al construir y no admiten enunciado previo; entonces el prototipo hace de investigación. Los tickets de [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) son sintéticos: ilustran el método, no la frecuencia real de ninguna causa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Brecha](../b/brecha.md), [Consecuencia](../c/consecuencia.md), [Causa y evidencia](../c/causa-y-evidencia.md), [Necesidades](../n/necesidades.md), [Oportunidades](../o/oportunidades.md), [Síntomas y peticiones](../s/sintomas-y-peticiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — la discovery empieza reformulando una solución dada como problema por resolver; autoridad: Government Digital Service.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — marco oficial para investigar necesidades antes y durante el desarrollo; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato de necesidad de usuario y criterios para validarla; autoridad: Government Digital Service.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — propone observar el trabajo que la persona intenta hacer antes que sus características demográficas; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad al recoger datos de personas; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Problema del oráculo](./problema-del-oraculo.md) · [Procedencia →](./procedencia.md)
