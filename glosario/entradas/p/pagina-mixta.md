# Página mixta

[↑ Glosario](../../README.md) · [← Página huérfana](./pagina-huerfana.md) · [Paquete →](./paquete.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Página cuyo contenido pertenece a más de un tipo sin separación ni enlaces entre ellos.

Definición de trabajo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).

## Por qué importa

La clase donde se define, [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), existe con este propósito: la clase existe para que puedas decir de una página si es un tutorial, una guía práctica, una referencia o una explicación, y para que sepas qué se rompe cuando una misma página intenta ser dos cosas a la vez.

## Cómo funciona

Según [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md):

Dos preguntas bastan para clasificar: ¿el contenido guía una acción o informa al pensamiento? y ¿sirve a quien estudia o a quien trabaja? Las cuatro combinaciones dan los cuatro tipos. Mezclar tipos no es un pecado, es un coste: cada tipo exige un tono distinto (imperativo y alentador, imperativo y seco, neutral y completo, reflexivo) y un orden distinto. Una página mixta obliga a cambiar de registro sin aviso, esconde los pasos entre párrafos de contexto y complica las pruebas, porque lo que se puede ejecutar queda enterrado. La solución no es borrar lo que sobra, es enlazarlo: una frase y un enlace conservan el vínculo sin interrumpir.

## Ejemplo

Ejemplo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sección «Caso conductor»):

La penalización de la plataforma de entregas pasa de una página mixta a cuatro páginas por tipo. Esta clase deja el tutorial ejecutable, que se reutilizará como prueba en `SE-212` (documentación como código) y `SE-216` (portal versionado), y la distinción entre referencia y explicación, que `SE-210` aplica a la API y `SE-208` a las decisiones.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md)) son:

- **El tutorial tiene una sección «Notas avanzadas» a mitad de los pasos** — causa: se mezcló explicación con guía de aprendizaje. Corrección: mover las notas a una explicación y dejar un enlace de una línea.
- **La guía práctica empieza con la historia de la política** — causa: se mezcló contexto con procedimiento. Corrección: mover la historia a la explicación y enlazarla desde el primer párrafo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una página mixta obliga a cambiar de registro sin aviso, esconde los pasos entre párrafos de contexto y complica las pruebas, porque lo que se puede ejecutar queda enterrado. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](./pagina.md), [Tipo](../t/tipo.md), [Explicación](../e/explicacion.md), [Guía práctica](../g/guia-practica.md), [Referencia](../r/referencia.md), [Tutorial](../t/tutorial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.
- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.
- [Diátaxis: explicación](https://diataxis.fr/explanation/) — contexto y alternativas; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Página huérfana](./pagina-huerfana.md) · [Paquete →](./paquete.md)
