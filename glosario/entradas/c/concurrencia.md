# Concurrencia

[↑ Glosario](../../README.md) · [← Conciliación](./conciliacion.md) · [Concurrencia estructurada →](./concurrencia-estructurada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

La **concurrencia** es la propiedad de un programa en el que varias tareas están en curso y pueden avanzar de forma independiente, haya o no ejecución simultánea ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md)). [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) la presenta como composición de progresos superpuestos. Se distingue del **paralelismo**, que es una propiedad de la ejecución: dos tareas avanzan en el mismo instante porque hay dos unidades de cálculo.

## Por qué importa

La distinción decide qué problema se resuelve. Un servicio que espera disco y red necesita concurrencia (no bloquearse mientras espera); un cálculo pesado necesita paralelismo (más núcleos). Confundirlos produce lo que [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) señala: creer que más hilos duplican la velocidad. Además, la concurrencia trae un costo propio: razonar sobre intercalaciones y estado compartido ([SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md)). [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) muestra la consecuencia: leer-modificar-escribir sin exclusión pierde casi todas las actualizaciones.

## Cómo funciona

Un programa puede ser concurrente sin ser paralelo (un núcleo que alterna tareas) y paralelo sin ser concurrente en un sentido interesante (cuatro copias independientes) ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md)). Los mecanismos:

- **Hilos y procesos** ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)): el sistema alterna tareas con interrupciones y las reparte entre núcleos.
- **Asincronía**: las esperas pasan a corrutinas que ceden el control mientras aguardan entrada/salida.
- **Procesos múltiples** ([SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), factor de concurrencia de 12-factor): se escala añadiendo procesos, no hilos dentro de uno.

La causa del riesgo es el estado compartido: dos tareas que leen y escriben el mismo dato en orden no determinista pueden producir resultados distintos en cada ejecución.

## Ejemplo

[SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md): un servicio de entregas clasifica sus tareas antes de tocar el código: guardar el archivo (espera de disco), consultar el curso (espera de red), calcular similitud (300 ms de cálculo) y enviar el acuse (espera de red). Las tres esperas pasan a corrutinas con un límite de 50 conexiones; el cálculo va a un grupo de procesos de tamaño igual al número de núcleos menos uno; el latido de salud sale de una tarea propia.

## Errores y confusiones comunes

- **«Los hilos duplican la velocidad».** Causa: concurrencia igualada a paralelismo; corrección: identificar carga, núcleos y runtime ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)).
- **Mutar estado compartido sin exclusión** ([SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md)): actualizaciones perdidas.
- **Pensar que la asincronía acelera el cálculo.** Solo ayuda cuando hay esperas.

## Límites y cuándo no aplica

Una tarea estrictamente secuencial no gana nada con concurrencia, y el costo de coordinar puede superar el beneficio. El número de núcleos y el runtime (por ejemplo, el bloqueo global del intérprete en algunos lenguajes) limitan el paralelismo real. Y la sección de 12-factor sobre concurrencia es una receta de escalado por procesos, no una definición general.

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

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Discord](../../../casos/exito/discord.md), [Therac-25](../../../casos/fallo/therac-25.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

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
