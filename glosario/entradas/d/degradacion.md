# Degradación

[↑ Glosario](../../README.md) · [← Definición de terminado](./definicion-de-terminado.md) · [Degradación elegante →](./degradacion-elegante.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

**Degradación** (en el sentido del programa, *degradación controlada*) es el paso deliberado a un nivel con menos capacidad y más previsibilidad ([SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md)) cuando algo falta o falla. [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) la usa en su versión mínima: un resultado parcial explícito cuando una capacidad opcional no está disponible. No es «el sistema empeora con el tiempo» ni un fallo: es una respuesta diseñada.

## Por qué importa

Convierte la pregunta binaria «¿funciona?» en «¿qué parte del valor se conserva?» ([SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md)). Un sistema que solo conoce «todo o nada» cae entero cuando cae una dependencia secundaria. La decisión profesional que cambia es qué funciones son esenciales y cuáles pueden entregarse parciales, antiguas o ausentes, y quién lo decide: [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) subraya que son decisiones de producto, no solo técnicas.

## Cómo funciona

Cuando una dependencia no responde, el sistema devuelve una respuesta **parcial o antigua** en lugar de fallar ([SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md)). Requiere tres condiciones:

1. detectar el fallo rápido (límites de tiempo, rechazo cuando un grupo se llena);
2. tener un respaldo (caché, datos del día anterior, funcionalidad reducida);
3. **declarar** el estado degradado, para que el consumidor no confunda «desconocido» con «cero» ([SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)).

En [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), el aislamiento por dependencia (mamparas) evita que la lentitud de una agote los recursos de las demás, y el rechazo rápido evita acumular peticiones. En [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), la degradación aparece como nivel previsible hacia el que un sistema con LLM retrocede cuando falla un componente.

## Ejemplo

Experimento de [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md): 2000 peticiones con una dependencia caída el 40 % del tiempo. Sin degradación, el 60,0 % de las respuestas son útiles; con una caché de 70 % de aciertos como respaldo, el 87,5 %. Corrección aplicada: separar el grupo de recursos por dependencia, limitarlo, rechazar rápido, servir reportes con datos del día anterior y escribir la prueba que simula la lentitud.

## Errores y confusiones comunes

- **Servir datos antiguos sin avisarlo.** El usuario toma decisiones con información obsoleta; la degradación debe ser visible.
- **Degradar sin haber probado el camino degradado.** Solo se descubre que no funciona durante el incidente; [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) exige simular la lentitud en una prueba.
- **Confundir degradación con reintento.** El reintento insiste; la degradación cambia de nivel de servicio.
- **Tratar «desconocido» como cero** ([SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)).

## Límites y cuándo no aplica

Las cifras de [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) son de una simulación con parámetros del autor, no una predicción. No toda función admite versión parcial: una transferencia de dinero a medias es peor que un error. Y un respaldo caduco puede ser inaceptable cuando la frescura es el requisito.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad opcional](../c/capacidad-opcional.md), [Capacidad](../c/capacidad.md), [Resultado](../r/resultado.md), [Adaptador](../a/adaptador.md), [Ambassador](../a/ambassador.md), [Bulkhead](../b/bulkhead.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-599 — Taller: elegir y degradar un patrón agéntico](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (58 clases más lo mencionan; las que más):

[SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — About PowerShell](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — about_Automatic_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group — Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Definición de terminado](./definicion-de-terminado.md) · [Degradación elegante →](./degradacion-elegante.md)
