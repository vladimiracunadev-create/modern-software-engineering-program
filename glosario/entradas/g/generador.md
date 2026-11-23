# Generador

[↑ Glosario](../../README.md) · [← Generación estática](./generacion-estatica.md) · [Gestor de versiones →](./gestor-de-versiones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Procedimiento que produce entradas de prueba, con semilla si debe ser reproducible.

Definición de trabajo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md).

## Por qué importa

En [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), el tema «Generadores» importa porque un generador pobre no llega a las fronteras.

## Cómo funciona

Según [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), en la sección «Generadores»:

El generador decide qué entradas se prueban. Uno uniforme sobre un rango grande produce valores típicos y casi nunca las fronteras: la probabilidad de que `n < k` con `n` en 0–600 y `k` en 1–12 es de aproximadamente el 1 %. Un buen generador añade sesgo hacia los bordes (vacío, uno, el límite, el límite más uno) y hacia combinaciones raras. La semilla hace reproducible la ejecución y su registro convierte un fallo de «a veces» en un fallo repetible.

## Ejemplo

Ejemplo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma añade propiedades a tres funciones: el reparto de entregas (suma, longitud, equilibrio), la normalización de nombres (idempotencia, sin duplicados) y la cola de correcciones (contra un modelo de lista). El generador del reparto destina un tercio de los casos a valores cerca de las fronteras (`n` entre 0 y `2k`, `n` en los límites del rango), y la semilla de cada ejecución se imprime en el informe de la integración continua. Cuando una propiedad falla, un script reduce el caso y lo guarda como una prueba por ejemplo en `tests/regresion/`, de modo que el defecto queda fijado aunque el generador cambie.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La propiedad pasa y la función tiene un defecto conocido** — causa: generador que no llega a la frontera. Corrección: sesgo hacia vacío, límites y combinaciones. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un buen generador añade sesgo hacia los bordes (vacío, uno, el límite, el límite más uno) y hacia combinaciones raras. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))
- **una propiedad con generador uniforme que no encuentra el defecto de la frontera**. ([SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Semilla](../s/semilla.md), [Modelo](../m/modelo.md), [Propiedad](../p/propiedad.md), [Prueba metamórfica](../p/prueba-metamorfica.md), [Reducción](../r/reduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (153 clases más lo mencionan; las que más):

[SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Generadores».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Documentación del módulo random](https://docs.python.org/3/library/random.html) — semillas y límites del generador; autoridad: documentación oficial de Python.
- [Claessen y Hughes, «QuickCheck: a lightweight tool for random testing of Haskell programs»](https://doi.org/10.1145/351240.351266) — pruebas por propiedades; autoridad: artículo original de ICFP 2000.
- [Documentación de Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de propiedades para Python; autoridad: documentación oficial.
- [Hypothesis: pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) — comparación con modelos; autoridad: documentación oficial.
- [MacIver et al., «Hypothesis: A new approach to property-based testing»](https://joss.theoj.org/papers/10.21105/joss.01891) — diseño de la biblioteca; autoridad: artículo revisado de JOSS.

---

[↑ Glosario](../../README.md) · [← Generación estática](./generacion-estatica.md) · [Gestor de versiones →](./gestor-de-versiones.md)
