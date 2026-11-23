# Rojo, verde, refactor

[↑ Glosario](../../README.md) · [← Rojo y verde](./rojo-y-verde.md) · [Rol →](./rol.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Demostración de una prueba: falla con el defecto, pasa sin él y pasa con una reescritura neutra.

Definición de trabajo de [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md).

## Por qué importa

La clase donde se define, [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), existe con este propósito: la clase es un taller: parte de una suite de catorce pruebas que «pasan» y exige demostrar, para cada una, qué defecto detecta, que falla con él y pasa sin él, y que no se rompe ante un refactor que conserva el comportamiento.

## Cómo funciona

[SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md):

El equipo de la plataforma exige que toda prueba nueva de un módulo crítico llegue con su demostración: una línea en `evidencia.json` con el defecto que detecta (un mutante o un caso histórico), la confirmación de que falla con él y pasa sin él, y el resultado de las refactorizaciones del repositorio. Un trabajo de la integración continua re-ejecuta el paquete en cada cambio del módulo y falla si una prueba deja de matar su defecto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md)) son:

- **Una prueba «mata» mutantes y no afirma ningún valor** — causa: muertes por excepción. Corrección: reforzar con aserciones sobre valores y etiquetar las de humo.
- **Una prueba pasa con y sin el defecto** — causa: pasa por una razón distinta de la que declara. Corrección: caso que solo el defecto rompa.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sobre un módulo sintético con 18 mutantes, seis refactorizaciones y catorce pruebas escritas por el autor, en Windows y Ubuntu (WSL2), con salidas idénticas. Los veredictos usan reglas simples, las correlaciones usan 14 observaciones y el validador se ajustó con las mutaciones que lo evalúan. No se usó una herramienta de mutación ni una suite real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Muerte por aserción](../m/muerte-por-asercion.md), [Muerte por excepción](../m/muerte-por-excepcion.md), [Paquete de evidencia](../p/paquete-de-evidencia.md), [Prueba frágil](../p/prueba-fragil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

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

[↑ Glosario](../../README.md) · [← Rojo y verde](./rojo-y-verde.md) · [Rol →](./rol.md)
