# Efecto

[↑ Glosario](../../README.md) · [← Editor e ide](./editor-e-ide.md) · [Efecto de red cruzado →](./efecto-de-red-cruzado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Un **efecto** es una interacción **observable fuera del valor retornado** ([SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md)): leer un archivo, consultar la hora, hacer una llamada de red, escribir en pantalla, modificar una variable global o un argumento mutable. La pregunta que lo caracteriza es: ¿qué cambia, o de qué depende, fuera del cálculo? Una **función pura** depende solo de sus argumentos y retorna un valor sin alterar el exterior; toda función que se aparta de eso tiene efectos. En el programa «efecto» no significa «error» ni «consecuencia»: es un término técnico neutro.

## Por qué importa

Las funciones puras son fáciles de razonar y de probar: mismas entradas, misma salida, sin preparar nada. Las funciones con efectos dependen de un estado que no se ve en la firma y producen resultados que cambian entre llamadas. [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md) no condena los efectos (sin ellos un programa no leería ni escribiría nada) sino que pide **ubicarlos**: se aíslan en adaptadores y el núcleo recibe valores. La decisión que cambia es dónde se hacen las cosas con el mundo exterior: en pocos lugares conocidos, no esparcidas por todo el código.

## Cómo funciona

Lo que define el efecto es la dependencia o el cambio externo:

- **Efecto de salida:** escribir un archivo, imprimir, enviar un mensaje, modificar un objeto recibido.
- **Efecto de entrada (dependencia oculta):** leer el reloj, el generador aleatorio, el entorno o la red. Una función que consulta la hora no es pura aunque no escriba nada, porque su resultado depende de algo que no es un argumento.

Cuando el cálculo está mezclado con los efectos, probarlo exige simular el exterior. Cuando se separa, el **núcleo** (puro) recibe valores y devuelve valores, y los **adaptadores** (en los bordes) leen y escriben. Así el cálculo «se prueba sin red ni disco». Una consecuencia práctica aparece en [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md): importar un módulo que abre archivos o red al importarse es un efecto a nivel de módulo; la corrección es moverlos a `main()` o a una función llamada explícitamente. Y en [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), cuando se pregunta si una función puede imprimir, la respuesta es que imprimir es un efecto; en la práctica se **confina**: la función calcula y devuelve, y quien llama imprime.

## Ejemplo

Una función que calcula un recargo e imprime el resultado mezcla las dos cosas:

```python
def recargo_y_mostrar(monto):
    r = monto * 0.1
    print(f"Recargo: {r}")      # efecto
    return r
```

Separada, el cálculo es puro y el efecto queda en el borde:

```python
def recargo(monto):             # pura: se prueba con asserts
    return monto * 0.1

def main():
    print(f"Recargo: {recargo(1500)}")   # el efecto vive aquí
```

`assert recargo(1000) == 100.0` no necesita capturar la salida estándar.

## Errores y confusiones comunes

- **Creer que «sin efectos» es el objetivo.** Un programa sin efectos no hace nada; el objetivo es confinarlos.
- **Olvidar los efectos de entrada.** Consultar la hora o el entorno también hace impura una función.
- **Efectos al importar.** Abrir archivos o red a nivel de módulo hace que importar tenga consecuencias.
- **Memoizar funciones con efectos.** El efecto se ejecuta solo la primera vez ([SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md)).

## Límites y cuándo no aplica

La distinción puro/impuro es útil pero no es binaria en la práctica: escribir un registro de depuración es un efecto que casi nadie quiere esconder en un adaptador. El costo de aislarlos tiene un límite: en un script corto, separar núcleo y borde puede ser más estructura que valor. Y «puro» no equivale a «correcto» ni a «rápido»: una función pura puede contener un error o ser costosa.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Valor](../v/valor.md), [Condición](../c/condicion.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Cortocircuito](../c/cortocircuito.md), [Enlace](./enlace.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (348 clases más lo mencionan; las que más):

[SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Editor e ide](./editor-e-ide.md) · [Efecto de red cruzado →](./efecto-de-red-cruzado.md)
