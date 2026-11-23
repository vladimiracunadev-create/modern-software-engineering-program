# Sellado

[↑ Glosario](../../README.md) · [← Selector de patrón](./selector-de-patron.md) · [Semántica →](./semantica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Derivación de una clave atada a una medición concreta.

Definición de trabajo de [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md).

## Por qué importa

En [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), el tema «Sellado» importa porque ata los datos al estado medido.

## Cómo funciona

Según [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md):

La misma medición permite derivar una clave solo disponible cuando el estado coincide: en el modelo, `clave = HMAC(clave_del_dispositivo, "sellado" ‖ medición)`. La clave derivada de la cadena esperada coincidió con la derivada al arrancar la misma cadena y no coincidió con la de la cadena alterada: los datos sellados no se pueden abrir con software modificado. La consecuencia operativa es tan importante como la ventaja: *actualizar el software cambia la medición y por tanto la clave*. Un servicio sellado necesita un plan de actualización (volver a sellar con una clave autorizada por la versión anterior, o liberar la clave de datos desde un servicio de gestión de claves tras una atestación de la versión nueva) o pierde el acceso a sus datos.

Según [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md):

La universidad exige computación confidencial para el servicio que procesa los datos de estudiantes con necesidades especiales. El equipo de *Avisos* separa ese servicio del resto, lo empaqueta como un componente pequeño con un build reproducible y publica su medición firmada en el repositorio de la universidad. El servicio de claves de la universidad solo libera la clave de datos a un nodo cuya cita (con un desafío fresco) coincida con una medición publicada y con una fecha de validez. En la primera actualización, la medición cambia y el servicio no puede abrir sus datos: el equipo no había diseñado el paso de re-sellado. Se resuelve con una ventana de dos versiones aceptadas y un procedimiento firmado por dos personas de la universidad para retirar la anterior.

## Ejemplo

Ejemplo de [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (sección «Ejemplo profesional»):

La universidad exige computación confidencial para el servicio que procesa los datos de estudiantes con necesidades especiales. El equipo de *Avisos* separa ese servicio del resto, lo empaqueta como un componente pequeño con un build reproducible y publica su medición firmada en el repositorio de la universidad. El servicio de claves de la universidad solo libera la clave de datos a un nodo cuya cita (con un desafío fresco) coincida con una medición publicada y con una fecha de validez. En la primera actualización, la medición cambia y el servicio no puede abrir sus datos: el equipo no había diseñado el paso de re-sellado.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La misma medición permite derivar una clave solo disponible cuando el estado coincide: en el modelo, `clave = HMAC(clave_del_dispositivo, "sellado" ‖ medición)`. ([SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medición](../m/medicion.md), [Extensión](../e/extension.md), [Raíz de confianza](../r/raiz-de-confianza.md), [TEE](../t/tee.md), [Valor de referencia](../v/valor-de-referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Selector de patrón](./selector-de-patron.md) · [Semántica →](./semantica.md)
