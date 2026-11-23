# Solo lectura

[↑ Glosario](../../README.md) · [← Solicitud de cobertura](./solicitud-de-cobertura.md) · [Solución contrastable →](./solucion-contrastable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Modo que observa sin cambiar deliberadamente el estado inspeccionado.

Definición de trabajo de [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Por qué importa

En [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), el tema «Solo lectura» importa porque limita efectos predeterminados

## Cómo funciona

Según [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md):

**Cómo leer la figura.** Las flechas muestran quién llama a quién: una persona o automatización invoca un adaptador y este delega en el núcleo. La caja inferior resume los límites de seguridad que el núcleo impone sin importar el adaptador. **Dónde deja de valer:** un adaptador mal escrito puede violar el contrato (por ejemplo, pasando mal un argumento); por eso las pruebas ejercitan el núcleo y los adaptadores se verifican por separado en su plataforma. Y «solo lectura por defecto» no es riesgo cero: la propia lectura de un directorio puede exponer información, y el kit lo limita al workspace.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md):

Un equipo de soporte recibe un paquete diagnóstico de otra plataforma. La versión del esquema, procedencia de campos y límites le permiten revisar sin pedir el entorno completo. La matriz indica que macOS fue diseñado pero no ejecutado, evitando una promesa falsa.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La herramienta “repara” por defecto** — causa: se amplió el riesgo sin necesidad. Corrección: mantener solo lectura y plan explícito. ([SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y «solo lectura por defecto» no es riesgo cero: la propia lectura de un directorio puede exponer información, y el kit lo limita al workspace. ([SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Adaptador](../a/adaptador.md), [Capacidad](../c/capacidad.md), [Contrato versionado](../c/contrato-versionado.md), [Degradación explícita](../d/degradacion-explicita.md), [Hallazgo](../h/hallazgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (38 clases más lo mencionan; las que más):

[SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — PowerShell documentation](https://learn.microsoft.com/powershell/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — delimita el contrato técnico que debe cumplirse al entregar un kit de diagnóstico multiplataforma que observe sin alterar innecesariamente.

---

[↑ Glosario](../../README.md) · [← Solicitud de cobertura](./solicitud-de-cobertura.md) · [Solución contrastable →](./solucion-contrastable.md)
