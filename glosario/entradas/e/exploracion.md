# Exploración

[↑ Glosario](../../README.md) · [← Explicación fiel](./explicacion-fiel.md) · [Exploración con semilla →](./exploracion-con-semilla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Actividad simultánea de aprendizaje, diseño y ejecución de pruebas con una misión.

Definición de trabajo de [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md).

## Por qué importa

En [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md), el tema «Misiones y sesiones» importa porque convierten una exploración vaga en algo acotado y revisable.

## Cómo funciona

Según [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md):

Una sesión de exploración es un bloque de tiempo acotado (por ejemplo 60 a 90 minutos) con una misión: «explorar la subida de archivos buscando pérdidas de datos». La misión limita el alcance sin escribir los pasos, y el registro de la sesión anota qué se hizo, qué se encontró y qué dudas surgieron. Lo que distingue una exploración de «jugar» es que existe una misión y un registro; lo que la distingue de una prueba escrita es que los pasos se deciden sobre la marcha, aprovechando lo que se aprende.

Según [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** el guion pasa 60 acciones sin hallar ninguno de los 12 defectos y el equipo concluye que la aplicación «está bien». **Hipótesis rivales:** (a) la aplicación no tiene defectos; (b) el guion es demasiado corto; (c) el guion no recorre las zonas donde están los defectos. **Prueba:** ejecuta 480 acciones del mismo guion (sigue en 0) y una exploración heurística de 120 acciones (halla 7,9 de media). **Conclusión:** el guion repite siempre las mismas entradas y por eso nunca llega a los límites ni a las secuencias.

## Ejemplo

Ejemplo de [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor. Esta clase deja el noveno artefacto: las tres misiones de exploración, la lista de sondas de entrada y la partición de accesibilidad entre reglas y juicio. `SE-430` aborda lo que más erosiona la confianza en todo lo anterior: las pruebas que fallan a veces. Cambia después una sola decisión, el límite de adjuntos de 10 MB a 25 MB, y observa qué sondas y misiones cambian.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)) son:

- **«Exploramos» y nadie sabe qué se hizo** — causa: sin misión ni registro. Corrección: misión acotada y notas de sesión.
- **La herramienta de accesibilidad pasa y una persona no puede usar la página** — causa: solo se probó lo que una regla decide. Corrección: revisión manual con tecnologías de apoyo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una lista de sondas es una lista de verificación de entradas; no sustituye a la exploración, la prepara. ([SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md))

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
