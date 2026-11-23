# Cobertura de pares

[↑ Glosario](../../README.md) · [← Cobertura de parejas](./cobertura-de-parejas.md) · [Cobertura de un nivel →](./cobertura-de-un-nivel.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Conjunto de combinaciones que incluye todos los pares de valores de dos factores.

Definición de trabajo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md): Suite en la que cada combinación de valores de cada par de factores aparece al menos una vez.
- En [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md): Propiedad de una suite en la que cada par de valores de dos factores aparece en al menos un caso.
- En [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md): Propiedad de un conjunto de pruebas en que cada pareja de factores aparece en todas sus combinaciones de valores.

## Por qué importa

La clase donde se define, [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), existe con este propósito: la clase existe para que adaptes la interfaz a anchos de pantalla, preferencias del usuario y conexiones distintas con un plan de pruebas que cubra las combinaciones que importan, y para que midas qué fallos deja cada estrategia.

## Cómo funciona

Según [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

Cinco preferencias binarias (movimiento reducido, esquema oscuro, contraste más alto, colores forzados y zoom del 200 %) dan 32 combinaciones. Un algoritmo voraz de cobertura de pares cubre los 40 pares (10 pares de preferencias × 4 valores) con 6 filas. Se inyectaron 60 defectos que se disparan con una, dos o tres preferencias a la vez (20, 28 y 12): las 32 combinaciones encuentran los 60, las 6 filas de pares 55 y 6 filas al azar, 50,4 de media en 200 sorteos. Los 5 que se escapan a los pares son defectos de tres preferencias.

Según [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

No siempre: 32 es asumible, 2^10 no. La cobertura de pares es un acuerdo económico que encuentra casi todo lo de uno o dos factores y deja lo de tres sin cubrir; decide según el riesgo del proceso.

## Ejemplo

Ejemplo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) (sección «Preguntas frecuentes»):

No siempre: 32 es asumible, 2^10 no. La cobertura de pares es un acuerdo económico que encuentra casi todo lo de uno o dos factores y deja lo de tres sin cubrir; decide según el riesgo del proceso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La tabla de ejemplos tiene 243 filas y nadie la lee** — causa: producto completo de todos los factores. Corrección: reducir con cobertura de pares y añadir a mano las combinaciones de riesgo. ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md))
- **La suite reducida pasa y una interacción real falla** — causa: cobertura de pares sin los casos de tres factores sospechosos. Corrección: añadir casos manuales y declarar la cobertura de triples. ([SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La cobertura de pares es un acuerdo económico que encuentra casi todo lo de uno o dos factores y deja lo de tres sin cubrir; decide según el riesgo del proceso. ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md))

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
