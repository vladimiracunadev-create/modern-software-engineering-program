# Modelo

[↑ Glosario](../../README.md) · [← Modalidad de uso](./modalidad-de-uso.md) · [Modelo base →](./modelo-base.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Implementación simple y obviamente correcta contra la que se compara otra más compleja.

Definición de trabajo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md).

## Por qué importa

En [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), el tema «Pruebas contra un modelo» importa porque detectan defectos que dependen de secuencias de operaciones.

## Cómo funciona

Según [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md):

Una propiedad es una afirmación que debe cumplirse para toda entrada del dominio: la suma de las cantidades repartidas es `n`; normalizar dos veces da lo mismo que normalizar una; invertir una lista dos veces devuelve la original. Se escribe sin repetir la implementación (la propiedad «el resultado es lo que calcula la función» no comprueba nada). Hay familias útiles: invariantes que se conservan, idempotencia, relaciones entre entradas (si se añade un elemento, el resultado cambia así), comparación con un modelo más simple y propiedades metamórficas. Una propiedad débil se cumple casi siempre y casi no protege.

Según [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md):

El equipo de la plataforma añade propiedades a tres funciones: el reparto de entregas (suma, longitud, equilibrio), la normalización de nombres (idempotencia, sin duplicados) y la cola de correcciones (contra un modelo de lista). El generador del reparto destina un tercio de los casos a valores cerca de las fronteras (`n` entre 0 y `2k`, `n` en los límites del rango), y la semilla de cada ejecución se imprime en el informe de la integración continua. Cuando una propiedad falla, un script reduce el caso y lo guarda como una prueba por ejemplo en `tests/regresion/`, de modo que el defecto queda fijado aunque el generador cambie. Las propiedades conviven con los ejemplos que documentan la política de negocio («una entrega a las 24 horas exactas aún cuenta como puntual»).

## Ejemplo

Ejemplo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma añade propiedades a tres funciones: el reparto de entregas (suma, longitud, equilibrio), la normalización de nombres (idempotencia, sin duplicados) y la cola de correcciones (contra un modelo de lista). El generador del reparto destina un tercio de los casos a valores cerca de las fronteras (`n` entre 0 y `2k`, `n` en los límites del rango), y la semilla de cada ejecución se imprime en el informe de la integración continua. Cuando una propiedad falla, un script reduce el caso y lo guarda como una prueba por ejemplo en `tests/regresion/`, de modo que el defecto queda fijado aunque el generador cambie.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La propiedad repite la implementación** — causa: se calcula el resultado esperado con la misma fórmula. Corrección: usar invariantes o un modelo distinto. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))
- **El modelo comparte el error de la implementación** — causa: los escribió la misma persona con el mismo malentendido. Corrección: revisión independiente del modelo. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para una implementación con estado (una cola, un carrito, una máquina de estados) se escribe un modelo mínimo, normalmente más simple y obviamente correcto (una lista), y se generan secuencias aleatorias de operaciones que se aplican a ambos; cualquier divergencia es un defecto de uno de los dos. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generador](../g/generador.md), [Propiedad](../p/propiedad.md), [Prueba metamórfica](../p/prueba-metamorfica.md), [Reducción](../r/reduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (508 clases más lo mencionan; las que más):

[SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hypothesis: pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) — comparación con modelos; autoridad: documentación oficial.
- [Claessen y Hughes, «QuickCheck: a lightweight tool for random testing of Haskell programs»](https://doi.org/10.1145/351240.351266) — pruebas por propiedades; autoridad: artículo original de ICFP 2000.
- [Documentación de Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de propiedades para Python; autoridad: documentación oficial.
- [MacIver et al., «Hypothesis: A new approach to property-based testing»](https://joss.theoj.org/papers/10.21105/joss.01891) — diseño de la biblioteca; autoridad: artículo revisado de JOSS.
- [Hughes, «How to Specify It!»](https://doi.org/10.1007/978-3-030-47147-7_4) — estrategias para escribir propiedades; autoridad: capítulo del autor.

---

[↑ Glosario](../../README.md) · [← Modalidad de uso](./modalidad-de-uso.md) · [Modelo base →](./modelo-base.md)
