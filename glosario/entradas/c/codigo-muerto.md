# Código muerto

[↑ Glosario](../../README.md) · [← Código de salida](./codigo-de-salida.md) · [Código no previsto →](./codigo-no-previsto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Código que no se ejecuta en ninguna situación de uso real o plausible del sistema.

Definición de trabajo de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md): Código que no puede ejecutarse con ninguna entrada posible.

## Por qué importa

En [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), el tema «Código muerto y sus detectores» importa porque borrar lo que no está muerto rompe producción; no borrar lo muerto suma ruido.

## Cómo funciona

Según [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

El código muerto no se ejecuta nunca, y retirarlo reduce ruido y superficie de ataque. Detectarlo tiene dos enfoques con errores complementarios. El **análisis estático por nombre** recorre el árbol sintáctico y marca las funciones cuyo nombre no aparece referenciado; es exhaustivo en lo que ve y falla con todo lo que se invoca sin nombrar la función: llamadas por cadena (`getattr`, `globals()`), registros que guardan funciones decoradas, configuración que las nombra, reflexión. La **traza de ejecución** registra las funciones que se ejecutan en una ejecución real o de pruebas; ve los usos dinámicos que el análisis estático no resuelve, y falla con todo lo que esa ejecución no recorrió: la rama de fin de año, el caso de error, el cliente que llama una vez al trimestre.

Según [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md):

Traslada el análisis a otro dominio (por ejemplo, el software de gestión de un laboratorio clínico, con datos sintéticos): cambia los archivos y los patrones de uso y conserva el procedimiento de combinar frecuencia, correcciones y tamaño, estimar huérfanos y cruzar dos técnicas de detección de código muerto. La transferencia está lograda cuando puedes decir qué técnica fallaría en el nuevo dominio y por qué, no cuando la tabla se parece a la del módulo de calificaciones.

## Ejemplo

Ejemplo de [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) (sección «Caso conductor»):

El módulo de calificaciones es el caso conductor de la [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md). Esta clase deja el segundo artefacto: el mapa de riesgo (puntos calientes, huérfanos y candidatos a código muerto). `SE-519` preguntará cómo se protegen los comportamientos de esos puntos calientes antes de modificarlos, y `SE-520` cómo se mide el riesgo que acumulan las dependencias. Cambia después un solo dato, la rotación mensual de 2 % a 0,5 %, y observa a partir de qué horizonte los huérfanos dejan de ser un problema.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md)) son:

- **Se prioriza el archivo más grande y no mejora nada** — causa: el tamaño no predice dónde se corrige. Corrección: combinar frecuencia de cambio, correcciones y tamaño.
- **El ranking cambia tras un formateo masivo** — causa: el commit de formato infla la frecuencia. Corrección: excluir commits mecánicos del análisis.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El código muerto no se ejecuta nunca, y retirarlo reduce ruido y superficie de ataque. ([SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Archivo huérfano](../a/archivo-huerfano.md), [Calificación de herramienta](./calificacion-de-herramienta.md), [Churn](./churn.md), [Cobertura estructural](./cobertura-estructural.md), [Código no previsto](./codigo-no-previsto.md), [Condición de fallo](./condicion-de-fallo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-448 — Aviación: DO-178C, DO-254 y ARP4754](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-518 — Arqueología de código y recuperación de conocimiento](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nagappan y Ball, «Use of relative code churn measures to predict system defect density»](https://doi.org/10.1145/1062455.1062514) — churn relativo y densidad de defectos; autoridad: ICSE 2005.
- [Avelino et al., «A novel approach for estimating Truck Factors»](https://doi.org/10.1109/ICPC.2016.7503718) — factor de camión estimado desde la autoría; autoridad: ICPC 2016.
- [Registros de decisión de arquitectura (ADR)](https://adr.github.io/) — formato ligero para dejar por escrito contexto, decisión y consecuencias; autoridad: comunidad ADR.

---

[↑ Glosario](../../README.md) · [← Código de salida](./codigo-de-salida.md) · [Código no previsto →](./codigo-no-previsto.md)
