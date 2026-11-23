# Prueba metamórfica

[↑ Glosario](../../README.md) · [← Prueba inestable](./prueba-inestable.md) · [Prueba periódica →](./prueba-periodica.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Prueba que relaciona los resultados de dos entradas relacionadas en lugar de conocer el resultado exacto.

Definición de trabajo de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), existe con este propósito: la clase existe para que describas qué debe cumplirse siempre (una propiedad) o qué debe imitar el sistema (un modelo) y dejes que un generador busque los casos que se te habrían olvidado, y para que sepas qué te cuesta ese método: un generador mal diseñado nunca llega a las fronteras y un fallo sin reducir es un ruido que nadie diagnostica.

## Cómo funciona

[SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md):

El equipo de la plataforma añade propiedades a tres funciones: el reparto de entregas (suma, longitud, equilibrio), la normalización de nombres (idempotencia, sin duplicados) y la cola de correcciones (contra un modelo de lista). El generador del reparto destina un tercio de los casos a valores cerca de las fronteras (`n` entre 0 y `2k`, `n` en los límites del rango), y la semilla de cada ejecución se imprime en el informe de la integración continua.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md)) son:

- **La propiedad pasa y la función tiene un defecto conocido** — causa: generador que no llega a la frontera. Corrección: sesgo hacia vacío, límites y combinaciones.
- **Un fallo aleatorio no se puede reproducir** — causa: no se registró la semilla. Corrección: imprimir la semilla en cada ejecución.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con un motor mínimo, defectos inyectados y datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se usó Hypothesis ni QuickCheck, y una variante de normalización resultó equivalente a la original respecto de las propiedades escritas (no se detecta con ninguna). Las propiedades se ajustaron con los mismos defectos que las evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Generador](../g/generador.md), [Modelo](../m/modelo.md), [Propiedad](./propiedad.md), [Reducción](../r/reduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-425 — Pruebas basadas en propiedades y modelos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claessen y Hughes, «QuickCheck: a lightweight tool for random testing of Haskell programs»](https://doi.org/10.1145/351240.351266) — pruebas por propiedades; autoridad: artículo original de ICFP 2000.
- [Documentación de Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de propiedades para Python; autoridad: documentación oficial.
- [Hypothesis: pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) — comparación con modelos; autoridad: documentación oficial.
- [MacIver et al., «Hypothesis: A new approach to property-based testing»](https://joss.theoj.org/papers/10.21105/joss.01891) — diseño de la biblioteca; autoridad: artículo revisado de JOSS.
- [Hughes, «How to Specify It!»](https://doi.org/10.1007/978-3-030-47147-7_4) — estrategias para escribir propiedades; autoridad: capítulo del autor.

---

[↑ Glosario](../../README.md) · [← Prueba inestable](./prueba-inestable.md) · [Prueba periódica →](./prueba-periodica.md)
