# Portabilidad

[↑ Glosario](../../README.md) · [← Política metodológica](./politica-metodologica.md) · [Portafolio →](./portafolio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

La **portabilidad** es la capacidad de ejecutar el mismo software en otro entorno con el mismo resultado ([SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)). [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) la formula para cargas en la nube: poder mover una carga entre entornos con un esfuerzo acotado y conocido. [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) la acota con una cláusula honesta: el grado de funcionamiento demostrado dentro de una matriz definida. La portabilidad es, entonces, algo que se demuestra, no una propiedad declarada.

## Por qué importa

Decide cuánto cuesta cambiar de entorno (sistema operativo, proveedor de nube) y cuánto riesgo hay de que el cambio altere el resultado. [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) advierte que se confunde con multi-cloud (usar más de un proveedor) y con híbrido (instalación propia más nube); comparten el discurso de «no depender de uno» pero son cosas distintas.

## Cómo funciona

Las diferencias entre entornos vienen sobre todo de los **valores por defecto** ([SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)):

- la codificación de texto cuando no se especifica;
- el fin de línea y el separador de ruta;
- si los nombres distinguen mayúsculas;
- caracteres y nombres prohibidos y la longitud máxima de ruta;
- qué ocurre al renombrar sobre un archivo existente o al borrar uno abierto;
- el rango de fechas del reloj y el método de creación de procesos.

Python esconde muchas diferencias y expone otras: las expuestas lanzan una excepción (`PermissionError`), las escondidas cambian el resultado. Por eso se escribe una matriz de soporte con lo realmente probado ([SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md)) y se aíslan las diferencias en adaptadores.

Para la nube ([SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)), la guía de Google sobre patrones híbridos y multi-cloud organiza motivos: aprovechar funciones distintas, cumplir una regulación de ubicación de datos, reducir una dependencia, repartir riesgo, aprovechar inversiones existentes. Cada motivo se evalúa con su propio cálculo.

## Ejemplo

```python
open("datos.txt", "w", encoding="utf-8", newline="\n")   # fija lo que el entorno decidiría por defecto
```

Sin `encoding` ni `newline`, el mismo programa escribe bytes distintos en Windows y Linux.

## Errores y confusiones comunes

- **Dos proveedores y la misma caída anual.** Causa: un componente compartido en serie; corrección: dibujar las dependencias y eliminar o duplicar el común ([SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)).
- **La conmutación falla cuando se necesita.** Causa: nunca se ensayó; corrección: ensayarla con regularidad y medir su acierto ([SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)).
- **Declarar portable lo que solo se probó en un entorno.**

## Límites y cuándo no aplica

La portabilidad total es una ilusión de costo alto: normalmente se persigue una portabilidad acotada y probada. Multi-cloud sin motivo concreto produce arquitecturas caras que no resuelven ningún problema ([SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md)). Y portable no significa idéntico en rendimiento: el resultado funcional puede igualar mientras el desempeño difiere.

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
