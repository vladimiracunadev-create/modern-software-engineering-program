# Grafo de ataque

[↑ Glosario](../../README.md) · [← Grafo](./grafo.md) · [Grafo de dependencias →](./grafo-de-dependencias.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Representación de estados del atacante y técnicas con costo que permite calcular el camino de menor esfuerzo hacia un objetivo.

Definición de trabajo de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md).

## Por qué importa

En [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), el tema «Grafos de ataque y priorización» importa porque el camino más barato decide el riesgo, no el defecto más grave.

## Cómo funciona

Según [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

Una lista de amenazas no dice cuáles importan. Un **grafo de ataque** conecta estados del atacante (tener internet, tener una cuenta de estudiante, tener un rol de docente, tener lectura directa a la base) con aristas que representan una técnica y llevan un costo de esfuerzo; el objetivo es un nodo (alterar una nota). El camino de menor costo desde el nodo inicial es la estimación del riesgo más relevante porque un atacante racional lo elige. La consecuencia contraintuitiva es que **arreglar el defecto más grave no cambia el mínimo si no está en el camino más barato**. Cerrar una vía no la elimina de la lista de pendientes sino que sube su costo; el siguiente camino pasa a ser el mínimo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

El equipo de la plataforma dibuja el diagrama con cuatro procesos (API, servicio de calificación, trabajador de archivos y notificador), dos almacenes, tres actores y cinco fronteras. En el cruce navegador-API enumera por STRIDE nueve amenazas, descarta tres con razón escrita y deja seis; al ponerles costo descubre que la más barata es la elevación de privilegios por el campo de rol del registro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)) son:

- **Se arregla lo grave y nada mejora** — causa: se prioriza por gravedad, no por camino. Corrección: calcular el camino más barato y recalcularlo tras cada decisión.
- **El modelo es una lista de 80 amenazas sin dueño** — causa: se enumera sin descartar ni decidir. Corrección: una fila por amenaza con elemento, respuesta y supuesto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se modeló un atacante real, ningún sistema en producción ni ningún incidente; los costos de las aristas, el ruido de los revisores, las tasas de cambio y la sensibilidad de la regla son construcciones del autor, y el análisis de la plataforma de entregas es un ejercicio sobre un diseño ficticio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Estado](../e/estado.md), [Representación](../r/representacion.md), [Activo](../a/activo.md), [Frontera de confianza](../f/frontera-de-confianza.md), [Modelo de amenazas](../m/modelo-de-amenazas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — principios de diseño de la protección; autoridad: Proceedings of the IEEE.
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) — valores y principios del modelado de amenazas; autoridad: comunidad de profesionales de seguridad.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — proceso práctico de modelado; autoridad: OWASP.
- [Microsoft: amenazas STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — categorías por elemento; autoridad: documentación de Microsoft.
- [Schneier, «Attack Trees»](https://www.schneier.com/academic/archives/1999/12/attack_trees/) — árboles de ataque con costos; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Grafo](./grafo.md) · [Grafo de dependencias →](./grafo-de-dependencias.md)
