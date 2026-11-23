# Build hermético

[↑ Glosario](../../README.md) · [← Build aislado](./build-aislado.md) · [Build reproducible →](./build-reproducible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Construcción que solo puede leer las entradas que declaró, sin red ni variables heredadas.

Definición de trabajo de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md).

## Por qué importa

La clase donde se define, [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), existe con este propósito: la clase existe para que puedas responder, con evidencia y no con una promesa, a la pregunta «¿este binario sale de este código?».

## Cómo funciona

Según [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

Un build es **reproducible** si dos ejecuciones con las mismas entradas producen el mismo resultado bit a bit. Es **hermético** si solo puede leer las entradas que declaró: el código fuente, las dependencias fijadas por huella y las herramientas en versiones concretas, sin acceso a la red, a variables de entorno arbitrarias ni a archivos del sistema que nadie listó. Son propiedades distintas. Un build puede ser reproducible por casualidad y no hermético (hoy lee una variable que casi nunca cambia) y puede ser hermético y no reproducible (declara todo pero escribe la hora en la cabecera). La hermeticidad es una condición de diseño que se hace cumplir bloqueando el acceso; la reproducibilidad es un resultado que se comprueba reconstruyendo.

## Ejemplo

Caso medido en la sección «Localizar la diferencia y el build hermético» de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

**Cómo leer la figura.** A la izquierda están los dos builds que no coinciden y a la derecha tres casos. La dorada es una diferencia localizada, un solo archivo de 42; la coral es un build que lee una entrada no declarada, por lo que no es hermético; la turquesa es el resultado deseado, un único hash. **Dónde deja de valer:** la comparación por archivo localiza dónde difiere el contenido, no por qué; un compilador puede producir un archivo distinto por una decisión interna que no hay forma de ver en el archivo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md)) son:

- **Cada build produce un hash distinto** — causa: fechas, orden o rutas incrustadas. Corrección: normalizar tiempo y orden; eliminar rutas.
- **El hash cambia solo en otra máquina** — causa: campo del formato dependiente del sistema. Corrección: repetir en otro sistema y fijar el campo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una sin la otra no sirve para verificar: un build hermético y no reproducible es auditable pero no comparable, y uno reproducible y no hermético es comparable hasta que cambia la entrada oculta. ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Build reproducible](./build-reproducible.md), [Entrada no declarada](../e/entrada-no-declarada.md), [Huella](../h/huella.md), [Normalizar](../n/normalizar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — qué es un build reproducible; autoridad: proyecto Reproducible Builds.
- [Reproducible Builds: SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — fecha fija para el build; autoridad: proyecto Reproducible Builds.
- [Lamb y Zacchiroli, «Reproducible Builds: Increasing the Integrity of Software Supply Chains»](https://doi.org/10.1109/MS.2021.3073045) — motivación y técnicas; autoridad: IEEE Software.
- [Thompson, «Reflections on trusting trust»](https://doi.org/10.1145/358198.358210) — compiladores comprometidos; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Build aislado](./build-aislado.md) · [Build reproducible →](./build-reproducible.md)
