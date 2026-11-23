# Orquestador

[↑ Glosario](../../README.md) · [← Orquestación](./orquestacion.md) · [Orquestador de caos →](./orquestador-de-caos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Componente que divide el trabajo según la entrada y lo asigna a trabajadores.

Definición de trabajo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md): Sistema que arranca, para y reparte tráfico entre instancias de un servicio.

## Por qué importa

La clase donde se define, [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), existe con este propósito: la clase existe para que sepas cuándo un sistema necesita que un componente **decida en tiempo de ejecución cómo dividir el trabajo** (orquestador-trabajadores) y cuándo la calidad se consigue **iterando contra un criterio** (evaluador-optimizador).

## Cómo funciona

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

En una paralelización (`SE-590`) las subtareas se conocen de antemano. En un **orquestador-trabajadores**, un modelo (o una regla) inspecciona la entrada, decide en cuántas partes dividirla, asigna cada una a un trabajador y luego sintetiza los resultados. La documentación de Anthropic lo recomienda cuando no se pueden predecir las subtareas, y pone el ejemplo de cambios de código que tocan un número variable de archivos. Lo que hace especial al patrón es la **decisión de división en tiempo de ejecución**; el resto (trabajadores, síntesis) es infraestructura. Su costo mínimo son dos llamadas: la que divide y la que sintetiza.

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

El equipo implementa el repaso semanal con un orquestador que lee la lista de cursos con su número de entregas y decide los grupos: los tres cursos más grandes van cada uno a un trabajador y el resto se agrupa. Cada trabajador usa tres herramientas de solo lectura y devuelve un JSON con pendientes, vencidos y anomalías. La síntesis redacta el informe y el verificador comprueba que cada curso aparezca una vez y que los totales coincidan con la suma de los JSON. Si falla, el generador de la síntesis recibe las fallas exactas y rehace; con tres intentos sin pasar, el informe se envía a una persona marcado como «incompleto» con la lista de cursos que no cuadran.

## Ejemplo

Ejemplo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sección «Ejemplo profesional»):

El equipo implementa el repaso semanal con un orquestador que lee la lista de cursos con su número de entregas y decide los grupos: los tres cursos más grandes van cada uno a un trabajador y el resto se agrupa. Cada trabajador usa tres herramientas de solo lectura y devuelve un JSON con pendientes, vencidos y anomalías. La síntesis redacta el informe y el verificador comprueba que cada curso aparezca una vez y que los totales coincidan con la suma de los JSON.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un orquestador que conoce o estima los tamaños puede aplicar la regla voraz «asigna el trabajo más grande aún sin asignar al trabajador menos cargado» (la heurística LPT). ([SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Trabajador](../t/trabajador.md), [Trabajo](../t/trabajo.md).
- **Ver también:** [Componente](../c/componente.md), [Instancia](../i/instancia.md), [Servicio](../s/servicio.md), [Calentamiento](../c/calentamiento.md), [Cascada de reinicios](../c/cascada-de-reinicios.md), [Drenaje](../d/drenaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de monitorización; autoridad: Google.
- [Python: http.server](https://docs.python.org/3/library/http.server.html) — servidor local del experimento; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos y su espera al cerrar; autoridad: Python Software Foundation.
- [Python: signal](https://docs.python.org/3/library/signal.html) — señales del sistema en Python; autoridad: Python Software Foundation.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — propagación de la correlación entre servicios; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Orquestación](./orquestacion.md) · [Orquestador de caos →](./orquestador-de-caos.md)
