# Importación

[↑ Glosario](../../README.md) · [← Implicación](./implicacion.md) · [Importancia por contexto →](./importancia-por-contexto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Función, memoria o tabla que el módulo pide al anfitrión por módulo y nombre.

Definición de trabajo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md).

## Por qué importa

En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), el tema «Importaciones y exportaciones» importa porque son la única superficie de contacto entre módulo y anfitrión.

## Cómo funciona

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

Un módulo de WebAssembly es una secuencia de secciones: tipos de función, importaciones, funciones, memoria, exportaciones y código. El código es de una máquina de pila con tipos estáticos: cada instrucción declara qué consume y qué produce, y la validación comprueba, sin ejecutar nada, que cada función deja la pila como su tipo promete, que los saltos van a etiquetas estructuradas (bloques y bucles anidados, no direcciones arbitrarias) y que las llamadas respetan los tipos. El módulo del laboratorio, escrito en texto (WAT) con cinco funciones y una memoria, ocupa **236 bytes** una vez compilado a binario, y los primeros ocho bytes son `0061736d01000000`: la marca `\0asm` y la versión 1.

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

El equipo de *Avisos* decide aceptar reglas de las universidades como módulos de Wasm. Define un contrato mínimo: la regla exporta `debe_avisar(horas_para_vencer, dia_semana, minutos_de_aviso_previo) -> i32` y no importa nada. El servicio carga el módulo, comprueba que declara cero importaciones (si declara alguna, se rechaza con el nombre), crea una instancia nueva por llamada, le asigna combustible suficiente para unas miles de instrucciones y una memoria máxima de una página, y registra cuántas reglas agotan combustible. Durante la primera semana, una universidad sube una regla con un bucle que recorre un calendario embebido: agota el combustible, la llamada falla, el servicio responde con la regla por defecto y el panel muestra la causa con el nombre de la universidad. Nadie vio una caída.

## Ejemplo

Ejemplo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) (sección «Ejemplo mínimo»):

El módulo más pequeño útil: suma dos enteros y declara cero importaciones.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Dos consecuencias de diseño: el combustible mide trabajo, no tiempo de reloj (una importación lenta del anfitrión no gasta combustible), y activar la medición tiene un costo de ejecución que se paga en toda llamada. ([SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md))
- Decide si un módulo con importaciones explícitas y límites del anfitrión lo contendría y qué parte seguiría dependiendo de la confianza. ([SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Anfitrión](../a/anfitrion.md), [Función](../f/funcion.md), [Módulo](../m/modulo.md), [Capacidad](../c/capacidad.md), [Combustible](../c/combustible.md), [Instancia](./instancia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (39 clases más lo mencionan; las que más):

[SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Implicación](./implicacion.md) · [Importancia por contexto →](./importancia-por-contexto.md)
