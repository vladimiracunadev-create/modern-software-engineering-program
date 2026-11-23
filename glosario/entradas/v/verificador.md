# Verificador

[↑ Glosario](../../README.md) · [← Verificación independiente](./verificacion-independiente.md) · [Verificador independiente →](./verificador-independiente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Análisis estático que acepta o rechaza un programa antes de ejecutarlo.

Definición de trabajo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Por qué importa

En [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), el tema «Verificador» importa porque es la garantía de seguridad: se comprueba antes de ejecutar.

## Cómo funciona

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

Un programa eBPF es una secuencia de instrucciones de 8 bytes (con una excepción de 16 para cargar constantes de 64 bits) para una máquina de registros: diez registros de 64 bits, `r0` para el valor de retorno, `r1` a `r5` para los argumentos, `r10` como puntero de solo lectura a una pila de 512 bytes. Se carga con la llamada de sistema `bpf` y la orden `BPF_PROG_LOAD`, que recibe el tipo de programa, las instrucciones, la licencia y un búfer donde el núcleo escribe el registro del verificador. Si el verificador acepta, el núcleo compila el programa a instrucciones nativas (compilación JIT, habilitada en el núcleo del laboratorio) y devuelve un descriptor de archivo.

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

El equipo de *Avisos* necesita saber cuántas conexiones salientes hacia el servidor de correo se reintentan por minuto, sin tocar el servicio. Un ingeniero de plataforma propone un programa eBPF enganchado al punto donde el núcleo inicia una conexión TCP. El equipo de seguridad pide tres condiciones antes de aprobarlo: que solo cargue programas una cuenta de servicio con capacidades mínimas, que cada programa cargado quede registrado con su huella y su autor, y que el programa solo cuente (sin leer el contenido de los paquetes, que contienen datos de estudiantes). El programa se escribe en C, se compila a bytecode, se prueba primero con el servicio de pruebas del núcleo y luego se despliega en un nodo de preproducción.

## Ejemplo

Ejemplo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sección «Ejemplo mínimo»):

Las dos instrucciones ocupan 16 bytes. El verificador procesó 2 instrucciones y el núcleo, al ejecutarlo con `BPF_PROG_TEST_RUN`, devolvió 42.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Primera: los bucles sí existen en eBPF moderno, pero solo los que el verificador logra demostrar acotados con el número de iteraciones que su análisis alcance; un bucle con un contador que el verificador no puede acotar se rechaza aunque el programador sepa que termina. ([SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md))
- No protege de que alguien con permiso de carga observe datos sensibles, ni de errores del propio verificador (que se han encontrado y corregido como en cualquier software). ([SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis estático](../a/analisis-estatico.md), [Análisis](../a/analisis.md), [BPF_PROG_TEST_RUN](../b/bpf-prog-test-run.md), [Compilación JIT](../c/compilacion-jit.md), [EBPF](../e/ebpf.md), [Mapa](../m/mapa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (49 clases más lo mencionan; las que más):

[SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Verificación independiente](./verificacion-independiente.md) · [Verificador independiente →](./verificador-independiente.md)
