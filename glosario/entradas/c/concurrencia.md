# Concurrencia

[↑ Glosario](../../README.md) · [← Conciliación](./conciliacion.md) · [Concurrencia estructurada →](./concurrencia-estructurada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Propiedad de un programa en el que varias tareas están en curso y pueden avanzar de forma independiente, haya o no ejecución simultánea.

Definición de trabajo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md): Composición de progresos superpuestos.

## Por qué importa

En [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), el tema «Concurrencia» importa porque leer-modificar-escribir sin exclusión pierde casi todo.

En [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), el tema «Concurrencia» importa porque se escala con más procesos.

## Cómo funciona

Según [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md):

Los doce factores son: una base de código con muchos despliegues; dependencias declaradas explícitamente; configuración en el entorno; servicios de apoyo tratados como recursos adjuntos; separación estricta entre construir, publicar y ejecutar; procesos sin estado; servicios exportados por vinculación de puertos; concurrencia escalando por procesos; desechabilidad (arranque rápido y parada limpia); paridad entre desarrollo y producción; registros como flujo de eventos; y procesos administrativos como tareas puntuales del mismo artefacto. Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). La clase mide los factores de las dos últimas agrupaciones, que son los que se pueden comprobar con un experimento.

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

La **concurrencia** es una propiedad de la estructura de un programa: varias tareas están en curso, cada una puede avanzar sin esperar a que otra termine. El **paralelismo** es una propiedad de la ejecución: dos tareas avanzan en el mismo instante porque hay dos unidades de cálculo. Un programa puede ser concurrente sin ser paralelo (un solo núcleo que alterna entre tareas) y puede ser paralelo sin ser concurrente en sentido interesante (cuatro núcleos que ejecutan cuatro copias independientes de lo mismo). La distinción importa porque cada una tiene un costo distinto: la concurrencia exige razonar sobre intercalaciones y estado compartido (`SE-386`), el paralelismo exige repartir datos y reunir resultados.

## Ejemplo

Ejemplo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) (sección «Ejemplo profesional»):

El equipo del servicio de entregas clasifica sus tareas en una tabla antes de tocar el código: guardar el archivo (espera de disco), consultar el estado del curso (espera de red), calcular la similitud contra entregas anteriores (cálculo de 300 ms) y enviar el acuse (espera de red). Las tres esperas pasan a corrutinas con un límite de 50 conexiones simultáneas. El cálculo de similitud no se trocea dentro del bucle: se envía a un grupo de procesos de tamaño igual al número de núcleos menos uno, y el servicio sigue respondiendo mientras tanto. El latido de salud sale de una tarea propia que no comparte código con el cálculo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **hilos duplican velocidad** — causa: concurrencia = paralelismo. Corrección: identifica carga, núcleos y runtime. ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Agrupados por lo que protegen, cuatro cubren la reproducibilidad (código, dependencias, construir-publicar-ejecutar, procesos administrativos), tres cubren la portabilidad entre entornos (configuración, servicios de apoyo, paridad) y cinco cubren la elasticidad y la recuperación (procesos, concurrencia, desechabilidad, vinculación de puertos, registros). ([SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md))
- La **concurrencia** es una propiedad de la estructura de un programa: varias tareas están en curso, cada una puede avanzar sin esperar a que otra termine. ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Composición](./composicion.md), [Progreso](../p/progreso.md), [Propiedad](../p/propiedad.md), [Tarea](../t/tarea.md), [Bloqueo](../b/bloqueo.md), [Endurecimiento](../e/endurecimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (98 clases más lo mencionan; las que más):

[SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `subprocess` y consideraciones de seguridad](https://docs.python.org/3/library/subprocess.html#security-considerations) — `shell=True` y listas de argumentos; autoridad: documentación de Python.
- [OWASP: Command Injection](https://owasp.org/www-community/attacks/Command_Injection) — inyección de comandos; autoridad: OWASP.
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html) — catalogación de la debilidad; autoridad: MITRE.
- [ShellCheck wiki](https://www.shellcheck.net/wiki/) — errores típicos en guiones de shell; autoridad: proyecto ShellCheck.
- [Python: `os`](https://docs.python.org/3/library/os.html) — `O_EXCL`, `os.replace` y `os.open`; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Conciliación](./conciliacion.md) · [Concurrencia estructurada →](./concurrencia-estructurada.md)
