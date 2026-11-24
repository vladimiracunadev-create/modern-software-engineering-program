# Exploración

[↑ Glosario](../../README.md) · [← Explicación fiel](./explicacion-fiel.md) · [Exploración con semilla →](./exploracion-con-semilla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

La **exploración** (pruebas exploratorias) es la actividad simultánea de aprendizaje, diseño y ejecución de pruebas con una misión ([SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)).

## Por qué importa

Encuentra lo que nadie previó y que un guion escrito no puede encontrar. Pero solo es profesional si deja rastro: sin misión ni registro, «exploramos» no significa nada.

## Cómo funciona

Una sesión de exploración es un bloque de tiempo acotado (por ejemplo, 60 a 90 minutos) con una misión: «explorar la subida de archivos buscando pérdidas de datos». La misión limita el alcance sin escribir los pasos; el registro anota qué se hizo, qué se encontró y qué dudas surgieron. Lo que la distingue de «jugar» es que existe una misión y un registro; lo que la distingue de una prueba escrita es que los pasos se deciden sobre la marcha. Se prepara con una lista de sondas, que no la sustituye.

## Ejemplo

[SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md): un guion aleatorio de 60 acciones no halla ninguno de los 12 defectos y el equipo concluye que la aplicación «está bien»; ejecutar 480 acciones o dirigirse con sondas cambia la conclusión. La falta de hallazgos no prueba ausencia de defectos.

## Errores y confusiones comunes

- **«Exploramos» y nadie sabe qué se hizo.** Sin misión ni registro; misión acotada y notas de sesión.
- **La herramienta de accesibilidad pasa y una persona no puede usar la página.** Solo se probó lo que una regla decide; revisión manual con tecnologías de apoyo.

## Límites y cuándo no aplica

Depende de la habilidad de quien explora y no es repetible como una prueba automática; los defectos encontrados deben convertirse en pruebas de regresión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actividad](../a/actividad.md), [Misión](../m/mision.md), [Heurística de prueba](../h/heuristica-de-prueba.md), [Relación de contraste](../r/relacion-de-contraste.md), [Sonda](../s/sonda.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bach, «Exploratory Testing»](https://www.satisfice.com/exploratory-testing) — exploración como disciplina; autoridad: autor del texto.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — criterios de accesibilidad; autoridad: Recomendación del W3C.
- [Understanding SC 1.4.3: contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — umbrales de contraste; autoridad: W3C WAI.
- [W3C WAI: evaluar la accesibilidad web](https://www.w3.org/WAI/test-evaluate/) — herramientas y revisión manual; autoridad: W3C WAI.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — pruebas de seguridad web; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Explicación fiel](./explicacion-fiel.md) · [Exploración con semilla →](./exploracion-con-semilla.md)
