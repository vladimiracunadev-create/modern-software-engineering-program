# Revisión por muestreo

[↑ Glosario](../../README.md) · [← Revisión independiente](./revision-independiente.md) · [Revisión por pares →](./revision-por-pares.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Comprobación de un subconjunto de las afirmaciones elegidas al azar o por criterio.

Definición de trabajo de [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md).

## Por qué importa

En [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), el tema «Revisión por muestreo» importa porque la revisora no lee todo; el diseño decide qué encuentra.

## Cómo funciona

Según [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), en la sección «Revisión por muestreo»:

Quien revisa no lee todo. Si un dossier tiene n afirmaciones, m de ellas sin respaldo, y la revisora inspecciona k elegidas al azar, la probabilidad de ver al menos una sin respaldo es 1 − C(n−m, k) / C(n, k), una distribución hipergeométrica que se calcula con `math.comb`. Con n = 30 y m = 3, inspeccionar 5 da el 43,3 % y 12 el 79,9 %. Dos consecuencias de diseño. Primera: pocas afirmaciones sin respaldo se esconden muy bien en una muestra, así que el autor no debe contar con que «nadie las verá» ni con que «seguro las encuentran»; el verificador es la forma de no depender del azar. Segunda: la velocidad de comprobación cambia la muestra.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo arma el dossier de la decisión de la exportación con los siete archivos requeridos: el índice con ocho afirmaciones, la decisión revisada con el expediente de `SE-539`, los riesgos con el valor esperado de `SE-534`, los costos con el análisis de `SE-537` y la matriz de `SE-535`, la retroalimentación con el acuerdo de mentoría de `SE-532` y el mensaje de decisión de `SE-531`, y los límites.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md)) son:

- **La revisora no encuentra la evidencia** — causa: sin tabla afirmación–evidencia. Corrección: construir `claims.csv` con ruta y huella.
- **La evidencia no coincide con la huella** — causa: se modificó después de calcularla. Corrección: recalcular y registrar el cambio, o restaurar el original.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos y un verificador sobre seis dossiers construidos por el autor en un directorio temporal, en Windows y Ubuntu (WSL2), con resultados idénticos. No se revisó ningún dossier ni persona reales; los dossiers de prueba, los tiempos de revisión y la elección uniforme de la muestra son construcciones del autor, y el verificador comprueba forma, integridad y coherencia etiquetada, no veracidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Cifra etiquetada](../c/cifra-etiquetada.md), [Dossier defendible](../d/dossier-defendible.md), [Huella (resumen) SHA-256](../h/huella-resumen-sha-256.md), [Límite declarado](../l/limite-declarado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python, módulo `hashlib`](https://docs.python.org/3/library/hashlib.html) — resúmenes criptográficos; autoridad: Python Software Foundation.
- [Python, módulo `csv`](https://docs.python.org/3/library/csv.html) — lectura y escritura de CSV; autoridad: Python Software Foundation.
- [Python, módulo `tempfile`](https://docs.python.org/3/library/tempfile.html) — directorios temporales; autoridad: Python Software Foundation.
- [Python, módulo `math`](https://docs.python.org/3/library/math.html) — combinaciones; autoridad: Python Software Foundation.
- [Diátaxis](https://diataxis.fr/) — tipos de documentación; autoridad: autor del marco.

---

[↑ Glosario](../../README.md) · [← Revisión independiente](./revision-independiente.md) · [Revisión por pares →](./revision-por-pares.md)
