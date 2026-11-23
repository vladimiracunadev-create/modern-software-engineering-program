# Dossier defendible

[↑ Glosario](../../README.md) · [← Dossier de arquitectura](./dossier-de-arquitectura.md) · [Drenado →](./drenado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Conjunto de afirmaciones con evidencia vinculada, cifras coherentes y límites declarados, diseñado para que otra persona lo compruebe.

Definición de trabajo de [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md).

## Por qué importa

La clase donde se define, [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), existe con este propósito: el proyecto existe para que reúnas lo trabajado en la [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) en un dossier que otra persona pueda leer, comprobar y cuestionar sin tu ayuda.

## Cómo funciona

Según [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md):

Un dossier defendible se organiza alrededor de **afirmaciones** (frases que alguien podría cuestionar: «la cola reduce el p95 de 840 ms a 310 ms», «el costo a cinco años es 1 200», «la decisión es reversible durante 30 días»). Cada una lleva un identificador (C1, C2…) y se apoya en una **evidencia**: un archivo, un resultado de ejecución, un registro. Lo que no tiene evidencia se declara como supuesto, y los supuestos se marcan para que nadie los confunda con lo medido. Esta estructura responde la pregunta de quien revisa: «¿cómo sé que esto es cierto?».

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo arma el dossier de la decisión de la exportación con los siete archivos requeridos: el índice con ocho afirmaciones, la decisión revisada con el expediente de `SE-539`, los riesgos con el valor esperado de `SE-534`, los costos con el análisis de `SE-537` y la matriz de `SE-535`, la retroalimentación con el acuerdo de mentoría de `SE-532` y el mensaje de decisión de `SE-531`, y los límites.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md)) son:

- **La revisora no encuentra la evidencia** — causa: sin tabla afirmación–evidencia. Corrección: construir `claims.csv` con ruta y huella.
- **La evidencia no coincide con la huella** — causa: se modificó después de calcularla. Corrección: recalcular y registrar el cambio, o restaurar el original.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos y un verificador sobre seis dossiers construidos por el autor en un directorio temporal, en Windows y Ubuntu (WSL2), con resultados idénticos. No se revisó ningún dossier ni persona reales; los dossiers de prueba, los tiempos de revisión y la elección uniforme de la muestra son construcciones del autor, y el verificador comprueba forma, integridad y coherencia etiquetada, no veracidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite declarado](../l/limite-declarado.md), [Afirmación](../a/afirmacion.md), [Conjunto](../c/conjunto.md), [Evidencia](../e/evidencia.md), [Cifra etiquetada](../c/cifra-etiquetada.md), [Huella (resumen) SHA-256](../h/huella-resumen-sha-256.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-540 — Proyecto: dossier profesional defendible](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md).

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

[↑ Glosario](../../README.md) · [← Dossier de arquitectura](./dossier-de-arquitectura.md) · [Drenado →](./drenado.md)
