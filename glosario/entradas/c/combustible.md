# Combustible

[↑ Glosario](../../README.md) · [← Combinación de prácticas](./combinacion-de-practicas.md) · [Comisión →](./comision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Contador de trabajo que el runtime descuenta por instrucción para poder detener una ejecución.

Definición de trabajo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md).

## Por qué importa

En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), el tema «Combustible y límites» importa porque el aislamiento de memoria no limita CPU; hay que medirla y cortarla.

## Cómo funciona

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

El aislamiento de memoria no hace nada contra un bucle infinito. El módulo `spin` del laboratorio (`loop $l (br $l)`) es válido, no toca memoria ni importa nada, y se queda ejecutando para siempre. El anfitrión necesita un mecanismo propio: en `wasmtime` es el **combustible**. Se activa en la configuración (`consume_fuel`), se asigna una cantidad al almacén con `set_fuel`, y cada instrucción ejecutada la consume; al agotarse hay una trampa (`all fuel consumed by WebAssembly`). Con 5 000 000 de unidades, el bucle infinito se detuvo en unos 11 ms. Dos consecuencias de diseño: el combustible mide trabajo, no tiempo de reloj (una importación lenta del anfitrión no gasta combustible), y activar la medición tiene un costo de ejecución que se paga en toda llamada.

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

El equipo de *Avisos* decide aceptar reglas de las universidades como módulos de Wasm. Define un contrato mínimo: la regla exporta `debe_avisar(horas_para_vencer, dia_semana, minutos_de_aviso_previo) -> i32` y no importa nada. El servicio carga el módulo, comprueba que declara cero importaciones (si declara alguna, se rechaza con el nombre), crea una instancia nueva por llamada, le asigna combustible suficiente para unas miles de instrucciones y una memoria máxima de una página, y registra cuántas reglas agotan combustible. Durante la primera semana, una universidad sube una regla con un bucle que recorre un calendario embebido: agota el combustible, la llamada falla, el servicio responde con la regla por defecto y el panel muestra la causa con el nombre de la universidad. Nadie vio una caída.

## Ejemplo

Ejemplo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* decide aceptar reglas de las universidades como módulos de Wasm. Define un contrato mínimo: la regla exporta `debe_avisar(horas_para_vencer, dia_semana, minutos_de_aviso_previo) -> i32` y no importa nada. El servicio carga el módulo, comprueba que declara cero importaciones (si declara alguna, se rechaza con el nombre), crea una instancia nueva por llamada, le asigna combustible suficiente para unas miles de instrucciones y una memoria máxima de una página, y registra cuántas reglas agotan combustible.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Dos consecuencias de diseño: el combustible mide trabajo, no tiempo de reloj (una importación lenta del anfitrión no gasta combustible), y activar la medición tiene un costo de ejecución que se paga en toda llamada. ([SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Instrucción](../i/instruccion.md), [Runtime](../r/runtime.md).
- **Ver también:** [Contador](./contador.md), [Trabajo](../t/trabajo.md), [Capacidad](./capacidad.md), [Importación](../i/importacion.md), [Instancia](../i/instancia.md), [Memoria lineal](../m/memoria-lineal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Combinación de prácticas](./combinacion-de-practicas.md) · [Comisión →](./comision.md)
