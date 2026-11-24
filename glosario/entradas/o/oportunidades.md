# Oportunidades

[↑ Glosario](../../README.md) · [← Oportunidad y ranking](./oportunidad-y-ranking.md) · [Opt-in →](./opt-in.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Una **oportunidad** es un problema o necesidad con alcance estimado, consecuencia cuantificable y una ventana en la que actuar tiene sentido ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md)). No todo problema lo es: se vuelve una cuando alcanza a suficientes personas, con suficiente consecuencia y con una posibilidad razonable de actuar. Es el primer artefacto del descubrimiento de producto en la plataforma de entregas.

## Por qué importa

Permite comparar problemas con números en lugar de con voces. Sin tamaño, frecuencia y ventana, una queja ruidosa compite con una necesidad silenciosa y gana la que se oye más. Cambia la decisión de qué investigar o construir primero: se prioriza por tamaño estimado, y el rango señala qué factor conviene afinar antes de invertir.

## Cómo funciona

[SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) estima la oportunidad con tres factores: **cuántas personas** la sufren, **con qué frecuencia** y **qué costo** tiene cada ocurrencia. El resultado se expresa como **rango**, porque cada factor es incierto: un número único (400 horas al mes) transmite una precisión que no existe; un rango (de unas 190 a unas 1.700) muestra cuánto del tamaño es conocimiento y cuánto suposición. Además, el rango indica qué factor es más sensible: es el que conviene investigar primero.

La clase construye el primer artefacto con tickets sintéticos: agrupa por causa (la más frecuente es la expiración de sesión), formula un enunciado de problema y estima el rango. Un detalle importante es contar por **causa**, no por frase: varias redacciones de una misma causa quedan dispersas si se cuenta el texto. La corrección es etiquetar la causa por ticket, con quién y cuándo, y conservar el texto original. Y otro: no aceptar la petición original como requisito; se reformula como necesidad («necesito… para…») antes de proponer opciones, o la reunión discute la solución durante una hora sin acordar el problema.

## Ejemplo

Con los tickets de la plataforma, la causa más frecuente es la expiración de sesión durante la entrega. Si afecta a entre 300 y 1.000 estudiantes al mes, con una a tres ocurrencias por persona y un costo de 10 a 20 minutos cada una, el producto de los extremos da un rango de decenas a cientos de horas: ancho, pero suficiente para decir que merece investigarse frente a un problema de decenas de minutos. (Cifras de ejemplo en la línea del método de [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md); los datos de la clase son sintéticos.)

## Errores y confusiones comunes

- **Priorizar una falla que, al arreglarla, no reduce los tickets**: se contó la frase y no la causa.
- **Discutir la solución sin acordar el problema**: se aceptó la petición como requisito.
- **Dar una cifra única con falsa precisión.**
- **Confundir oportunidad con idea de producto**: la oportunidad es el problema con tamaño; la idea es una respuesta posible.

## Límites y cuándo no aplica

El rango depende de datos de calidad variable (tickets sintéticos en la clase, que ilustran el método y no miden un producto real). Una oportunidad grande puede carecer de ventana de acción (no hay forma razonable de resolverla ahora). Y el tamaño no es el único criterio: riesgos, dependencias y estrategia también cuentan al decidir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Consecuencia](../c/consecuencia.md), [Necesidades](../n/necesidades.md), [Problemas](../p/problemas.md), [Causa y evidencia](../c/causa-y-evidencia.md), [Síntomas y peticiones](../s/sintomas-y-peticiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (34 clases más lo mencionan; las que más):

[SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md), [Quibi](../../../casos/fallo/quibi.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — marco oficial para investigar necesidades antes y durante el desarrollo; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato de necesidad de usuario y criterios para validarla; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — la discovery empieza reformulando una solución dada como problema por resolver; autoridad: Government Digital Service.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — propone observar el trabajo que la persona intenta hacer antes que sus características demográficas; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad al recoger datos de personas; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Oportunidad y ranking](./oportunidad-y-ranking.md) · [Opt-in →](./opt-in.md)
