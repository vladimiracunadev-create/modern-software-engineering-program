# Tutorial

[↑ Glosario](../../README.md) · [← Túnel](./tunel.md) · [ULP →](../u/ulp.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Página que guía a quien aprende por pasos hacia un resultado seguro, sin ramificar ni explicar.

Definición de trabajo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).

## Por qué importa

En [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), el tema «Tutorial» importa porque lleva a quien aprende a un éxito garantizado; no debe explicar ni ramificar.

## Cómo funciona

Según [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), en la sección «Tutorial»:

Un tutorial es una lección: quien la escribe asume la responsabilidad de que quien la sigue llegue a un resultado y gane confianza. Por eso los pasos son pocos, concretos y verificables, cada uno muestra lo que se debe ver, y nada ramifica: «si usas otra versión, haz esto» pertenece a otra página. No explica por qué las cosas son así; a lo sumo dice «ahora verás» y da una frase de contexto que lo enlaza a la explicación. Un tutorial se rompe en silencio cuando el entorno cambia y deja a quien aprende creyendo que el error es suyo, de modo que el tutorial es el tipo que más gana si se ejecuta en cada cambio.

## Ejemplo

Ejemplo de [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sección «Ejemplo mínimo»):

El fragmento ejecuta los pasos de un tutorial contra una biblioteca y reporta cuáles pasan. Antes de ejecutarlo, predice qué pasos fallan si renombras `entregar` a `enviar`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El tutorial tiene una sección «Notas avanzadas» a mitad de los pasos** — causa: se mezcló explicación con guía de aprendizaje. Corrección: mover las notas a una explicación y dejar un enlace de una línea. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- **El tutorial funciona en la máquina de quien lo escribió y no en otra** — causa: depende de un estado previo no declarado. Corrección: ejecutarlo desde un entorno limpio en la integración continua. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- **Hay explicación pero nadie la encuentra** — causa: no está enlazada desde ninguna página de acción. Corrección: enlazar la explicación desde el tutorial, la guía y la referencia. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un tutorial se rompe en silencio cuando el entorno cambia y deja a quien aprende creyendo que el error es suyo, de modo que el tutorial es el tipo que más gana si se ejecuta en cada cambio. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))
- **un tutorial que deja de funcionar sin que nadie lo sepa**. ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](../p/pagina.md), [Resultado](../r/resultado.md), [Explicación](../e/explicacion.md), [Guía práctica](../g/guia-practica.md), [Página mixta](../p/pagina-mixta.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), [SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.
- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.
- [Diátaxis: explicación](https://diataxis.fr/explanation/) — contexto y alternativas; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Túnel](./tunel.md) · [ULP →](../u/ulp.md)
