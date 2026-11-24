# Contención

[↑ Glosario](../../README.md) · [← Contador](./contador.md) · [Contenedor →](./contenedor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

En el sentido principal del programa, **contención** es la fracción del tiempo que las tareas pasan esperando un cerrojo ([SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), memoria compartida, locks y condiciones de carrera). El término es ambiguo y otras clases lo usan de otra manera: en [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) y [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), *contener* es lograr que un comportamiento no alcance lo que no debería (tiempo, memoria, archivos, entorno, red) o no produzca su efecto dañino. Esta entrada desarrolla sobre todo el primer sentido y señala el segundo para no confundirlos.

## Por qué importa

Un cerrojo demasiado grueso serializa el servicio: aunque haya muchos hilos, trabajan de uno en uno. Medir la contención dice si dividir un cerrojo vale la pena antes de hacerlo, porque dividir multiplica cerrojos y riesgo de interbloqueo.

## Cómo funciona

[SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) separa dos ideas:

- **Granularidad:** cuánto dato protege un cerrojo. Uno global es fácil de razonar y serializa todo; uno por curso deja avanzar cursos distintos a la vez, pero multiplica los cerrojos y el riesgo de interbloqueo si una operación toca varios.
- **Contención:** la fracción del tiempo que las tareas pasan esperando. Depende de cuántas tareas compiten y de cómo se reparten las claves.

El matiz importante es el reparto: si unos pocos cursos concentran las entregas del cierre de plazo, dividir por curso ayuda menos de lo que sugiere el número de cerrojos, porque casi toda la espera se concentra en tres.

## Ejemplo

El panel de la docente en [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) no añade un cerrojo global. Primero separa dos casos: el contador de entregas pasa a una operación atómica de la base (`UPDATE curso SET entregas = entregas + 1`), que no necesita cerrojo en el programa; el cupo de la tarea (leer, comprobar, descontar) se protege con una transacción que bloquea esa fila. Para las rutas que tocan curso y estudiante fija un orden, curso antes que estudiante, verificado por una prueba. Mide cuántas peticiones del cierre caen en los tres cursos más populares y decide no partir más por curso.

## Errores y confusiones comunes

- **Pensar que más cerrojos siempre baja la espera:** con claves concentradas no lo hace.
- **Añadir un cerrojo donde basta una operación atómica de la base.**
- **Dividir sin ordenar los cerrojos**, lo que invita al interbloqueo.
- **Confundirlo con el sentido de seguridad** de [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md)/SE-588 (contención de un efecto dañino), que no tiene que ver con cerrojos.

## Límites y cuándo no aplica

La contención se mide, no se supone: sin medición del reparto de claves la decisión es una conjetura. Con poca concurrencia o secciones críticas muy cortas, el costo de la espera no justifica un diseño más fino. Y este sentido no cubre la contención en red o en disco, que son otros recursos compartidos con otras causas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Entorno](../e/entorno.md), [Tarea](../t/tarea.md), [Alcance](../a/alcance.md), [Batería hostil](../b/bateria-hostil.md), [Capacidad](./capacidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: threading](https://docs.python.org/3/library/threading.html) — cerrojos, barreras y tiempos límite; autoridad: documentación de Python.
- [Python: glosario](https://docs.python.org/3/glossary.html) — alcance del GIL; autoridad: documentación de Python.
- [Coffman, Elphick y Shoshani, «System deadlocks»](https://doi.org/10.1145/356586.356588) — condiciones del interbloqueo; autoridad: artículo original (ACM Computing Surveys, 1971).
- [Go: el detector de carreras](https://go.dev/doc/articles/race_detector) — qué ve y qué no ve una detección dinámica; autoridad: documentación oficial de Go.
- [Hoare, «Communicating sequential processes»](https://doi.org/10.1145/359576.359585) — alternativa de paso de mensajes que se retoma en la clase siguiente; autoridad: artículo original (1978).

---

[↑ Glosario](../../README.md) · [← Contador](./contador.md) · [Contenedor →](./contenedor.md)
