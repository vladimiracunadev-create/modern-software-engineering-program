# Mutación

[↑ Glosario](../../README.md) · [← Mutabilidad](./mutabilidad.md) · [Mutante del silencio →](./mutante-del-silencio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Una **mutación** es un cambio malo inyectado deliberadamente para probar un control ([SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md)). El programa usa el término con el mismo núcleo en varios contextos: copia de un árbol de métricas con un defecto conocido para evaluar un validador ([SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)), cambio deliberado de un defecto en una especificación válida para medir qué detecta el validador ([SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)), cambio deliberado de una respuesta para comprobar si una comprobación lo detecta ([SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)). Es la unidad de la prueba de mutación.

## Por qué importa

Un control que nunca ha fallado no se sabe si funciona. Un validador que siempre da verde puede estar ciego. La mutación lo comprueba introduciendo defectos conocidos y viendo si el control los detecta. Cambia la confianza que se puede tener: de «el validador pasa» a «el validador detecta estos N tipos de defecto».

## Cómo funciona

[SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) prueba un control como se prueba un detector: **con incidentes sembrados**. Las diez mutaciones del proyecto de la clase son defectos concretos sobre un registro de metadatos de datos: quitar el dueño; añadir una columna al mart sin actualizar el contrato; exponer una columna de correo en el mart (actualizando el contrato, para que otra regla no la vea); declarar una retención de 10 días sin purga; quitar todas las comprobaciones de un conjunto; hacer que el mart lea de la capa cruda sin pasar por la capa intermedia; entre otras. Para cada mutación, se ejecuta el control y se anota si la detecta.

El resultado es una **tabla de cobertura**: qué defectos ve el control y cuáles no. Las mutaciones no detectadas señalan huecos del control o mutantes equivalentes (que no cambian nada observable). En la práctica, el equipo de la clase ejecuta las diez mutaciones cada trimestre como prueba del propio control: si un cambio de reglas deja de detectar alguna, la prueba falla y el cambio no entra. Cuando ocurre un incidente real que el control no vio, se añade una mutación inspirada en él.

El mismo mecanismo sirve para validadores de especificaciones ([SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md): 16 mutaciones sobre una especificación base) y de árboles de métricas ([SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)). En todos los casos la mutación es **un cambio pequeño, conocido y malo**, y la medida es cuántos detecta el control.

## Ejemplo

Una especificación base válida se copia 16 veces; en cada copia se introduce un defecto distinto (un requisito sin dueño, una referencia a un requisito inexistente, un ciclo de dependencias, etc.). El validador se ejecuta sobre cada copia: detecta 13 de 16. Los 3 que no detecta son huecos documentados que se cubren con revisión humana. (Escenario construido con el método de [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).)

## Errores y confusiones comunes

- **Creer que un validador verde significa especificación sana**: solo comprueba lo que sabe comprobar.
- **Elegir mutaciones fáciles** que el control detecta de sobra.
- **Contar equivalentes como fallos del control.**
- **No ejecutarlas de forma periódica**: el control se degrada con los cambios.

## Límites y cuándo no aplica

Las mutaciones las elige el autor, de modo que la cobertura medida es sobre ese conjunto, no sobre todos los defectos posibles. Su valor depende de que representen defectos reales. No reemplazan la revisión humana ni las pruebas con datos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](../a/arbol.md), [Control](../c/control.md), [Especificación](../e/especificacion.md), [Evidencia](../e/evidencia.md), [Árbol de métricas](../a/arbol-de-metricas.md), [Caso de viabilidad](../c/caso-de-viabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-372 — Proyecto: plataforma de datos mínima gobernada](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (80 clases más lo mencionan; las que más):

[SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Mutaciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `copy.deepcopy`](https://docs.python.org/3/library/copy.html) — copias del caso para las mutaciones.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir indicadores con su cálculo, fuente y uso; autoridad: Government Digital Service (Reino Unido).
- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — de objetivos a señales y métricas; autoridad: Google Research.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas con contrapesos; autoridad: DORA (Google Cloud).
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — por qué cada nodo necesita un contrapeso; autoridad: investigación publicada en arXiv.

---

[↑ Glosario](../../README.md) · [← Mutabilidad](./mutabilidad.md) · [Mutante del silencio →](./mutante-del-silencio.md)
