# Cobertura de pares

[↑ Glosario](../../README.md) · [← Cobertura de parejas](./cobertura-de-parejas.md) · [Cobertura de un nivel →](./cobertura-de-un-nivel.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

La **cobertura de pares** (*pairwise*) es la propiedad de un conjunto de pruebas en el que cada combinación de valores de cada par de factores aparece al menos una vez ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md)). Es el caso t = 2 de la cobertura combinatoria. Es una métrica de una suite, no de código.

## Por qué importa

Reduce el número de casos sin renunciar a casi nada de lo que importa. El producto completo de factores crece de forma multiplicativa; una tabla de ejemplos con 243 filas nadie la lee ni la ejecuta. Con pares se mantiene una suite pequeña que encuentra la mayoría de los defectos que dependen de una o dos condiciones.

## Cómo funciona

Dados varios factores con sus valores, se construye un conjunto de filas tal que, para cualquier par de factores, todas las combinaciones de sus valores aparezcan en alguna fila. Un algoritmo voraz elige filas que cubran el mayor número de pares aún no cubiertos. [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) da un caso: cinco preferencias binarias de la interfaz (movimiento reducido, esquema oscuro, contraste más alto, colores forzados y zoom del 200 %) dan 32 combinaciones; los 40 pares (10 pares de factores × 4 valores) se cubren con solo 6 filas.

La clase mide qué pierde la reducción con una inyección de defectos: 60 defectos que se disparan con una, dos o tres preferencias a la vez (20, 28 y 12). Las 32 combinaciones encuentran los 60; las 6 filas de pares, 55; y 6 filas al azar, 50,4 de media en 200 sorteos. Los 5 defectos que los pares no encuentran son los que exigen tres factores a la vez. La conclusión: la cobertura de pares es un acuerdo económico que encuentra casi todo lo de uno o dos factores y deja lo de tres sin cubrir, y decide según el riesgo del proceso. Además, supera al azar con el mismo número de filas.

## Ejemplo

Con las cinco preferencias de [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), 6 filas bastan para cubrir todos los pares: en alguna fila aparece «esquema oscuro + zoom 200 %», en otra «contraste alto + colores forzados», etc. Si hay un defecto que solo aparece cuando están activas las tres a la vez (esquema oscuro, zoom y colores forzados), puede escapar; para esas combinaciones de riesgo se añaden casos a mano.

## Errores y confusiones comunes

- **Tabla de ejemplos de 243 filas que nadie lee**: producto completo de factores; corrección: reducir con cobertura de pares y añadir a mano las combinaciones de riesgo ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)).
- **La suite reducida pasa y una interacción real falla**: la interacción involucra tres factores o más.
- **Combinar valores inválidos** sin declarar restricciones.
- **Creer que pares garantiza todo.**

## Límites y cuándo no aplica

No cubre interacciones de tres o más factores, y los defectos de 3 factores del experimento (12 de 60) muestran que existen. 32 combinaciones se pueden probar enteras; 2¹⁰ no: la decisión depende del número de factores y del riesgo. Los defectos de la simulación son inyectados por el autor, de modo que las proporciones ilustran el mecanismo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Al menos una vez](../a/al-menos-una-vez.md), [Combinación](./combinacion.md), [Conjunto](./conjunto.md), [Propiedad](../p/propiedad.md), [Característica de preferencia](./caracteristica-de-preferencia.md), [Diseño responsive](../d/diseno-responsive.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kuhn, Kacker y Lei, NIST SP 800-142, «Practical Combinatorial Testing»](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de pares; autoridad: NIST.
- [W3C: Media Queries Level 4](https://www.w3.org/TR/mediaqueries-4/) — características de medios y de preferencia del usuario; autoridad: W3C.
- [W3C: CSS Grid Layout Module Level 1](https://www.w3.org/TR/css-grid-1/) — rejillas con mínimos y envoltura; autoridad: W3C.
- [MDN: `prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — preferencia de movimiento reducido; autoridad: Mozilla.
- [MDN: `prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) — preferencia de esquema; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Cobertura de parejas](./cobertura-de-parejas.md) · [Cobertura de un nivel →](./cobertura-de-un-nivel.md)
