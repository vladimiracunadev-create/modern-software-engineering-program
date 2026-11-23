# TEE

[↑ Glosario](../../README.md) · [← Tecnología de apoyo](./tecnologia-de-apoyo.md) · [Telemetría →](./telemetria.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Entorno cuya memoria y ejecución quedan protegidas del sistema operativo y del operador mediante hardware.

Definición de trabajo de [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md).

## Por qué importa

En [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), el tema «Qué protege un TEE» importa porque define la amenaza que se cubre: operador y sistema operativo.

## Cómo funciona

Según [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md):

La criptografía clásica protege datos en reposo (cifrado de discos) y en tránsito (TLS). Los datos *en uso* deben estar descifrados en memoria, donde un operador con control del sistema operativo, del hipervisor o de la máquina física podría leerlos. Un entorno de ejecución confiable aísla la ejecución y cifra o protege la memoria con soporte del hardware, de modo que ni el sistema operativo ni el hipervisor del anfitrión pueden leerla. El Confidential Computing Consortium lo define como protección de datos en uso mediante un TEE respaldado por hardware.

Según [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md):

No. El cifrado homomórfico calcula sobre datos cifrados sin descifrarlos, con un costo de cómputo muy alto; un TEE descifra dentro de una región protegida por hardware. Los compromisos de rendimiento y de confianza son distintos.

## Ejemplo

Ejemplo de [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (sección «Preguntas frecuentes»):

No. El cifrado homomórfico calcula sobre datos cifrados sin descifrarlos, con un costo de cómputo muy alto; un TEE descifra dentro de una región protegida por hardware. Los compromisos de rendimiento y de confianza son distintos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un entorno de ejecución confiable aísla la ejecución y cifra o protege la memoria con soporte del hardware, de modo que ni el sistema operativo ni el hipervisor del anfitrión pueden leerla. ([SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md))
- El cifrado homomórfico calcula sobre datos cifrados sin descifrarlos, con un costo de cómputo muy alto; un TEE descifra dentro de una región protegida por hardware. ([SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](../s/sistema-operativo.md), [Entorno](../e/entorno.md), [Extensión](../e/extension.md), [Medición](../m/medicion.md), [Raíz de confianza](../r/raiz-de-confianza.md), [Sellado](../s/sellado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «entorno de ejecución confiable».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tecnología de apoyo](./tecnologia-de-apoyo.md) · [Telemetría →](./telemetria.md)
