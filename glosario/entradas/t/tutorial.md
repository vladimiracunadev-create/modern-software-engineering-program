# Tutorial

[↑ Glosario](../../README.md) · [← Túnel](./tunel.md) · [ULP →](../u/ulp.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Un **tutorial** es, en [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), una página que guía a quien aprende por pasos hacia un resultado seguro, sin ramificar ni explicar. Es uno de los cuatro tipos de documentación (tutorial, guía práctica, referencia, explicación) y el orientado al aprendizaje.

## Por qué importa

Lleva a quien aprende a un éxito garantizado; no debe explicar ni ramificar. Su propósito es dar confianza a una persona principiante: si falla o se llena de opciones, la persona cree que el error es suyo. Cambia cómo se escribe: no es un resumen del sistema sino una lección con un camino único.

## Cómo funciona

Un tutorial es **una lección**: quien lo escribe asume la responsabilidad de que quien lo sigue **llegue a un resultado y gane confianza**. De ahí sus reglas. Los pasos son **pocos, concretos y verificables**; cada uno **muestra lo que se debe ver** («verás un mensaje de confirmación»). **Nada ramifica**: «si usas otra versión, haz esto» pertenece a otra página. **No explica por qué** las cosas son así; a lo sumo dice «ahora verás» y da una frase de contexto, y enlaza a una explicación para quien quiera saber más.

En la plataforma, el tutorial «Tu primera entrega con retraso» lleva a una persona nueva a hacer una entrega tardía y ver el descuento aplicado. Se distingue de la guía práctica, que supone competencia previa y admite bifurcaciones.

El riesgo que [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) destaca: **un tutorial se rompe en silencio cuando el entorno cambia** y deja a quien aprende creyendo que el error es suyo. Por eso es el tipo que **más gana si se ejecuta en cada cambio**: un script ejecuta los pasos contra la biblioteca o el sistema y reporta cuáles pasan. El fragmento de la clase ejecuta los pasos de un tutorial y pide predecir qué pasos fallan si se renombra `entregar` a `enviar`. Tres fallos y sus correcciones: notas avanzadas a mitad de los pasos (se mueven a una explicación con un enlace de una línea), tutorial que funciona en la máquina de quien lo escribió y no en otra (depende de un estado previo no declarado: se ejecuta desde un entorno limpio en integración continua) y explicación que nadie encuentra (se enlaza desde el tutorial, la guía y la referencia).

## Ejemplo

Paso 3 del tutorial: «Ejecuta `entregar --archivo mi-tarea.pdf --tarde`. Verás: `Entrega recibida. Descuento: 10 %`». Si tras renombrar el comando a `enviar` el paso falla, la integración continua lo detecta y el tutorial se corrige antes de que alguien lo siga. (Ejemplo ilustrativo del mecanismo de [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).)

## Errores y confusiones comunes

- **Mezclar explicación con aprendizaje** («Notas avanzadas» a mitad).
- **Depender de un estado previo no declarado.**
- **Ramificar** según versiones o preferencias.
- **No ejecutarlo nunca**: se rompe en silencio.

## Límites y cuándo no aplica

No sirve a quien ya sabe y busca resolver una tarea (necesita una guía práctica) ni a quien quiere entender las razones (necesita una explicación). Un tutorial largo pierde a quien aprende; se divide en lecciones. Su mantenimiento tiene costo, que se reduce al automatizar su ejecución.

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
