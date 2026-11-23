# Muerte por excepción

[↑ Glosario](../../README.md) · [← Muerte por aserción](./muerte-por-asercion.md) · [Muestreo →](./muestreo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Mutante que una prueba detecta solo porque el código lanza una excepción inesperada.

Definición de trabajo de [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md).

## Por qué importa

La clase donde se define, [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), existe con este propósito: la clase es un taller: parte de una suite de catorce pruebas que «pasan» y exige demostrar, para cada una, qué defecto detecta, que falla con él y pasa sin él, y que no se rompe ante un refactor que conserva el comportamiento.

## Cómo funciona

[SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md):

El equipo de la plataforma exige que toda prueba nueva de un módulo crítico llegue con su demostración: una línea en `evidencia.json` con el defecto que detecta (un mutante o un caso histórico), la confirmación de que falla con él y pasa sin él, y el resultado de las refactorizaciones del repositorio. Un trabajo de la integración continua re-ejecuta el paquete en cada cambio del módulo y falla si una prueba deja de matar su defecto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una prueba «mata» mutantes y no afirma ningún valor** — causa: muertes por excepción. Corrección: reforzar con aserciones sobre valores y etiquetar las de humo. ([SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sobre un módulo sintético con 18 mutantes, seis refactorizaciones y catorce pruebas escritas por el autor, en Windows y Ubuntu (WSL2), con salidas idénticas. Los veredictos usan reglas simples, las correlaciones usan 14 observaciones y el validador se ajustó con las mutaciones que lo evalúan. No se usó una herramienta de mutación ni una suite real.

## Relación con otros conceptos

- **Prerrequisito:** [Variante defectuosa](../v/variante-defectuosa.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Ver también:** [Excepción](../e/excepcion.md), [Muerte por aserción](./muerte-por-asercion.md), [Paquete de evidencia](../p/paquete-de-evidencia.md), [Prueba frágil](../p/prueba-fragil.md), [Rojo, verde, refactor](../r/rojo-verde-refactor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DeMillo, Lipton y Sayward, «Hints on test data selection»](https://doi.org/10.1109/C-M.1978.218136) — origen de los mutantes para evaluar pruebas; autoridad: artículo original de 1978.
- [Google Testing Blog: Mutation Testing](https://testing.googleblog.com/2021/04/mutation-testing.html) — mutantes en la revisión de código; autoridad: equipo de pruebas de Google.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.
- [Martin Fowler, «SelfTestingCode»](https://martinfowler.com/bliki/SelfTestingCode.html) — código que se comprueba a sí mismo; autoridad: autor del texto.
- [Martin Fowler, «TestDrivenDevelopment»](https://martinfowler.com/bliki/TestDrivenDevelopment.html) — ciclo rojo-verde; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Muerte por aserción](./muerte-por-asercion.md) · [Muestreo →](./muestreo.md)
