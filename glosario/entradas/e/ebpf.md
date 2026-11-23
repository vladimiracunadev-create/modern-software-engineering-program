# EBPF

[↑ Glosario](../../README.md) · [← Duración inclusiva](../d/duracion-inclusiva.md) · [ECE →](./ece.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Máquina virtual dentro del núcleo de Linux que ejecuta programas cargados desde el espacio de usuario tras una verificación.

Definición de trabajo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Por qué importa

La clase donde se define, [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), existe con este propósito: la clase existe para que entiendas eBPF como lo que es en la práctica: un mecanismo para cargar programas pequeños en el núcleo de Linux sin recompilarlo ni reiniciarlo, con un verificador que decide antes de ejecutar si el programa es seguro.

## Cómo funciona

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

Un programa eBPF es una secuencia de instrucciones de 8 bytes (con una excepción de 16 para cargar constantes de 64 bits) para una máquina de registros: diez registros de 64 bits, `r0` para el valor de retorno, `r1` a `r5` para los argumentos, `r10` como puntero de solo lectura a una pila de 512 bytes. Se carga con la llamada de sistema `bpf` y la orden `BPF_PROG_LOAD`, que recibe el tipo de programa, las instrucciones, la licencia y un búfer donde el núcleo escribe el registro del verificador. Si el verificador acepta, el núcleo compila el programa a instrucciones nativas (compilación JIT, habilitada en el núcleo del laboratorio) y devuelve un descriptor de archivo.

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

El equipo de *Avisos* necesita saber cuántas conexiones salientes hacia el servidor de correo se reintentan por minuto, sin tocar el servicio. Un ingeniero de plataforma propone un programa eBPF enganchado al punto donde el núcleo inicia una conexión TCP. El equipo de seguridad pide tres condiciones antes de aprobarlo: que solo cargue programas una cuenta de servicio con capacidades mínimas, que cada programa cargado quede registrado con su huella y su autor, y que el programa solo cuente (sin leer el contenido de los paquetes, que contienen datos de estudiantes). El programa se escribe en C, se compila a bytecode, se prueba primero con el servicio de pruebas del núcleo y luego se despliega en un nodo de preproducción.

## Ejemplo

Ejemplo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sección «Ejemplo mínimo»):

Un programa de dos instrucciones que devuelve 42, cargado y ejecutado desde Python con `ctypes`. Se muestra el esqueleto; el experimento completo está en `scripts/experiments_part23_ebpf_wsl.py`:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un programa eBPF es una secuencia de instrucciones de 8 bytes (con una excepción de 16 para cargar constantes de 64 bits) para una máquina de registros: diez registros de 64 bits, `r0` para el valor de retorno, `r1` a `r5` para los argumentos, `r10` como puntero de solo lectura a una pila de 512 bytes. ([SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md))
- **Fallo.** Un programa eBPF que funcionaba en los nodos de preproducción se rechaza en producción con `invalid mem access` aunque el código no cambió. ([SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espacio de usuario](./espacio-de-usuario.md), [Máquina virtual](../m/maquina-virtual.md), [Núcleo](../n/nucleo.md), [Verificación](../v/verificacion.md), [BPF_PROG_TEST_RUN](../b/bpf-prog-test-run.md), [Compilación JIT](../c/compilacion-jit.md).
- **Se confunde con:** La comparación no es equivalente (el programa de eBPF no lee el paquete ni cruza de espacio) pero fija la escala: contar en el núcleo es órdenes de magnitud más barato que sacar el evento hacia el espacio de usuario para contarlo allí.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Duración inclusiva](../d/duracion-inclusiva.md) · [ECE →](./ece.md)
