# Portabilidad

[↑ Glosario](../../README.md) · [← Política metodológica](./politica-metodologica.md) · [Portafolio →](./portafolio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Capacidad de mover una carga entre entornos con un esfuerzo acotado y conocido.

Definición de trabajo de [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md): Capacidad de ejecutar el mismo software en otro entorno con el mismo resultado.
- En [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md): Grado de funcionamiento demostrado dentro de una matriz definida.

## Por qué importa

En [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), el tema «Portabilidad y mínimo común» importa porque lo portable es lo que existe en todos; el resto liga al proveedor.

## Cómo funciona

Según [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md):

Multi-cloud significa usar más de un proveedor de nube; híbrido, combinar una instalación propia con la nube; portabilidad, poder cambiar de entorno sin reescribir. Son cosas distintas y se confunden porque comparten el discurso de «no depender de uno». La guía de Google sobre patrones híbridos y multi-cloud organiza los motivos: aprovechar funciones distintas, cumplir una regulación de ubicación de datos, reducir una dependencia, repartir riesgo, aprovechar inversiones existentes. Cada motivo se evalúa con su propio cálculo, y confundirlos produce arquitecturas caras que no resuelven ninguno.

Según [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md):

La **portabilidad** es la capacidad de ejecutar el mismo software en otro entorno con el mismo resultado. Los valores por defecto del entorno son la fuente habitual de diferencias: la codificación de texto cuando no se especifica, el fin de línea, el separador de ruta, si los nombres distinguen mayúsculas, los caracteres y nombres prohibidos en un archivo, la longitud máxima de una ruta, qué ocurre al renombrar sobre un archivo existente o al borrar un archivo abierto, el rango de fechas que admite el reloj, el método con que se crea un proceso. Python esconde muchas diferencias y expone otras; las expuestas lanzan una excepción (`PermissionError`) y las escondidas cambian el resultado.

## Ejemplo

Ejemplo de [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md). Esta clase deja el noveno artefacto: la estrategia de portabilidad y su costo. `SE-406` pregunta cómo se ofrece todo esto a los equipos sin que cada uno lo reconstruya. Cambia un supuesto, por ejemplo la probabilidad de conmutación, y observa cuánto se mueve la disponibilidad.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)) son:

- **Dos proveedores y la misma caída anual** — causa: un componente compartido en serie. Corrección: dibujar las dependencias y eliminar o duplicar el común.
- **La conmutación falla cuando se necesita** — causa: nunca se ensayó. Corrección: ensayar la conmutación con regularidad y medir su acierto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Multi-cloud significa usar más de un proveedor de nube; híbrido, combinar una instalación propia con la nube; portabilidad, poder cambiar de entorno sin reescribir. ([SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Entorno](../e/entorno.md), [Matriz](../m/matriz.md), [Resultado](../r/resultado.md), [Adaptador](../a/adaptador.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-405 — Multi-cloud, híbrido y portabilidad real](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google Cloud: patrones híbridos y multi-cloud](https://cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices) — motivos y patrones; autoridad: documentación del proveedor.
- [OCI Image Specification](https://github.com/opencontainers/image-spec) — formato común de imágenes; autoridad: Open Container Initiative.
- [Kubernetes: controladores](https://kubernetes.io/docs/concepts/architecture/controller/) — orquestación declarativa; autoridad: documentación oficial de Kubernetes.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — diseño para el fallo de componentes; autoridad: documentación del proveedor.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Política metodológica](./politica-metodologica.md) · [Portafolio →](./portafolio.md)
