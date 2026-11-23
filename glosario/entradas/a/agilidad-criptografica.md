# Agilidad criptográfica

[↑ Glosario](../../README.md) · [← Agentic Harness Engineer](./agentic-harness-engineer.md) · [Agregación →](./agregacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Capacidad de cambiar de algoritmo sin reescribir el sistema.

Definición de trabajo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Por qué importa

La clase donde se define, [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), existe con este propósito: la clase existe para que puedas planificar y ejecutar una migración criptográfica sin esperar a que exista un ordenador cuántico capaz de romper la criptografía actual.

## Cómo funciona

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

Una migración criptográfica sigue las pautas de `SE-474` a `SE-476` (versionado, banderas de funcionalidad, canary y retroceso) aplicadas a un cambio con un riesgo especial: los tamaños. El plan mínimo: (1) inventariar usos y bibliotecas, incluyendo dependencias y dispositivos; (2) clasificar por vida útil de los datos; (3) añadir agilidad criptográfica (algoritmo identificado en los datos, no fijo en el código) antes de cambiar nada; (4) activar el híbrido en el acuerdo de claves de los servicios con datos de vida larga, con métricas de errores de conexión y de latencia; (5) probar los límites de tamaño (campos fijos, certificados, bases de datos, dispositivos); (6) planificar las firmas, que son más difíciles porque los certificados y las raíces de confianza tienen ciclos de vida largos;

## Ejemplo

Ejemplo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) (sección «Caso conductor»):

*Avisos* tiene un plan de migración con prioridad por vida útil, agilidad criptográfica y un despliegue híbrido que ya encontró un problema real de tamaño. `SE-286` cierra el bloque técnico con una pregunta que atraviesa todo lo anterior: en un sistema donde ninguna frontera ni ninguna red es de confianza por defecto, ¿cómo se decide, petición por petición, quién puede hacer qué?

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- (3) añadir agilidad criptográfica (algoritmo identificado en los datos, no fijo en el código) antes de cambiar nada; ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Algoritmo](./algoritmo.md), [Capacidad](../c/capacidad.md), [Criptografía poscuántica](../c/criptografia-poscuantica.md), [Desigualdad de Mosca](../d/desigualdad-de-mosca.md), [Híbrido](../h/hibrido.md), [ML-DSA](../m/ml-dsa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Agentic Harness Engineer](./agentic-harness-engineer.md) · [Agregación →](./agregacion.md)
