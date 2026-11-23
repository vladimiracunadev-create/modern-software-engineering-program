# Regresión

[↑ Glosario](../../README.md) · [← Reglas de parada](./reglas-de-parada.md) · [Regresión a la media →](./regresion-a-la-media.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una **regresión** es la pérdida de algo que antes funcionaba. Las clases la definen con el mismo núcleo y distintos objetos: [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) como la pérdida de una propiedad previamente satisfecha, [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) como un defecto corregido que reaparece, [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) como la reaparición de un defecto ya reparado y [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) como un criterio que estaba cumplido y deja de estarlo tras un cambio. No hay que confundirla con el defecto original: la regresión es el retroceso tras un cambio.

## Por qué importa

Cada cambio, incluso una reparación, puede romper algo que no se estaba mirando. [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) formula la regla: la regresión busca que la corrección no haya roto otro contrato. Una reparación que se comprueba solo en el caso que falló no demuestra que el sistema siga bien.

## Cómo funciona

La defensa es conservar y repetir la comprobación. En [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), el kit de diagnóstico multiplataforma conserva versiones y una matriz de plataformas para que otra persona pueda repetir la reparación y verificar contratos vecinos. [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) añade el paso final del procedimiento de diagnóstico de un agente: tras reproducir, leer la traza, formular una hipótesis sobre una sola pieza y cambiarla, se añade el caso a la regresión. En los bucles automáticos de [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), cada pasada debe ejecutar todos los criterios y detenerse ante una regresión; si no, cada pasada arregla algo y rompe otra cosa. [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) pide un auditor que se ejecute en cada cambio y una lista manual periódica.

## Ejemplo

En [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), un bucle de mejora que en cada pasada ejecuta solo el criterio que acaba de arreglar puede romper otro criterio sin notarlo; con una batería completa en cada pasada, la regresión aparece en la pasada en que ocurre y el bucle se detiene. En [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), reparar solo el caso feliz de un entorno deja sin verificar los contratos vecinos; la matriz de regresión adversa los recorre.

## Errores y confusiones comunes

- **Se repara solo el caso feliz.** No se verificaron contratos vecinos; corrección ([SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md)): ejecutar una matriz de regresión adversa.
- **Cada pasada arregla algo y rompe otra cosa.** Regresiones sin batería de criterios completa; corrección ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)): ejecutar todos los criterios en cada pasada y detener ante regresión.
- **Un cambio rompe lo reparado.** No hay regresión comprobada; corrección ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)): auditor en cada cambio y lista manual periódica.
- **El bucle no acaba nunca.** Faltan condiciones de parada; corrección: máximo de pasadas, sin progreso, presupuesto y regresión ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)).

## Límites y cuándo no aplica

Una prueba de regresión solo vigila lo que se escribió: un contrato que nadie convirtió en comprobación puede romperse sin aviso. Las clases sitúan la regresión dentro de contextos concretos (entornos, auditoría de un flujo, bucles de un agente), por lo que lo que cuenta como «lo que antes funcionaba» depende de cada contexto y de qué criterios se conservaron.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Cambio mínimo](../c/cambio-minimo.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Doble](../d/doble.md), [Efecto](../e/efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (441 clases más lo mencionan; las que más):

[SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md).

**Aparece en los casos de estudio:** [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Sysinternals documentation](https://learn.microsoft.com/sysinternals/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [systemd manual pages](https://www.freedesktop.org/software/systemd/man/latest/) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Python documentation — subprocess](https://docs.python.org/3/library/subprocess.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.

---

[↑ Glosario](../../README.md) · [← Reglas de parada](./reglas-de-parada.md) · [Regresión a la media →](./regresion-a-la-media.md)
