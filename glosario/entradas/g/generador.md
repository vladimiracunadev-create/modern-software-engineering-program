# Generador

[↑ Glosario](../../README.md) · [← Generación estática](./generacion-estatica.md) · [Gestor de versiones →](./gestor-de-versiones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

En pruebas basadas en propiedades, un **generador** es el procedimiento que produce las entradas de prueba, con una semilla si la ejecución debe ser reproducible. Es la definición de trabajo de [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md). (No se debe confundir con los generadores de Python, las funciones con `yield`, ni con los generadores de código; aquí el término es el de las pruebas.)

## Por qué importa

Una prueba basada en propiedades afirma algo para *todas* las entradas, pero solo comprueba las que el generador produce. Por tanto, el generador decide qué defectos pueden aparecer. Cambia una decisión cotidiana: dar una propiedad por buena porque «pasó cien casos» es un error si esos cien casos nunca tocaron la frontera donde vive el defecto.

## Cómo funciona

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) da el ejemplo numérico. Un generador **uniforme** sobre un rango grande produce valores típicos y casi nunca las fronteras: con `n` entre 0 y 600 y `k` entre 1 y 12, la probabilidad de que `n < k` es de aproximadamente el 1 %. Por eso un generador útil añade **sesgo**:

- hacia los **bordes**: vacío, uno, el límite, el límite más uno;
- hacia **combinaciones raras** de parámetros.

La otra propiedad es la **semilla**. Una ejecución con generación aleatoria falla «a veces»; registrar la semilla convierte ese fallo en uno repetible: se vuelve a ejecutar con la misma semilla y se obtiene el mismo caso. La causa de la utilidad es práctica: sin semilla, un fallo intermitente no se puede diagnosticar, y con semilla es un caso de prueba más.

## Ejemplo

Función que debería rechazar listas de menos de `k` elementos:

```python
import random

def generar_caso(rng):
    k = rng.randint(1, 12)
    # sesgo: la mitad de los casos cae en la frontera
    if rng.random() < 0.5:
        n = rng.choice([0, 1, k - 1, k, k + 1])
    else:
        n = rng.randint(0, 600)
    return n, k

rng = random.Random(42)   # semilla registrada
casos = [generar_caso(rng) for _ in range(200)]
```

Con generación uniforme sobre 0-600, el defecto de `n == k - 1` casi nunca saldría; con el sesgo, aparece en las primeras decenas de casos. El código es una ilustración, no una cita de la clase.

## Errores y confusiones comunes

- **La propiedad pasa y la función tiene un defecto conocido.** Causa señalada en [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md): generador que no llega a la frontera. Corrección: sesgo hacia vacío, límites y combinaciones.
- **Creer que más casos compensan un mal generador.** Un millón de casos uniformes siguen sin tocar un borde que ocupa el 1 %.
- **No registrar la semilla.** El fallo no se puede reproducir.
- **Generar entradas inválidas sin querer.** Si el generador viola precondiciones, la propiedad falla por entradas fuera de dominio.

## Límites y cuándo no aplica

Un generador sesgado a las fronteras que el autor *conoce* no encuentra las que no conoce; conviene una parte uniforme o de otra naturaleza. Para estructuras complejas (árboles, documentos válidos) construir un generador que cubra el dominio es trabajo en sí, y generadores demasiado restrictivos descartan muchos casos. La reproducibilidad por semilla exige que todo el azar de la prueba salga del mismo generador. Y ninguna cantidad de entradas generadas demuestra corrección: reduce la probabilidad de defectos no vistos, no la elimina.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Semilla](../s/semilla.md), [Modelo](../m/modelo.md), [Propiedad](../p/propiedad.md), [Prueba metamórfica](../p/prueba-metamorfica.md), [Reducción](../r/reduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (153 clases más lo mencionan; las que más):

[SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md).

**Aparece en los casos de estudio:** [Cloudflare](../../../casos/exito/cloudflare.md).

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
