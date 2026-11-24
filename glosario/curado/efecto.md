# Efecto

## Definición

Un **efecto** es una interacción **observable fuera del valor retornado** (`SE-064`): leer un archivo, consultar la hora, hacer una llamada de red, escribir en pantalla, modificar una variable global o un argumento mutable. La pregunta que lo caracteriza es: ¿qué cambia, o de qué depende, fuera del cálculo? Una **función pura** depende solo de sus argumentos y retorna un valor sin alterar el exterior; toda función que se aparta de eso tiene efectos. En el programa «efecto» no significa «error» ni «consecuencia»: es un término técnico neutro.

## Por qué importa

Las funciones puras son fáciles de razonar y de probar: mismas entradas, misma salida, sin preparar nada. Las funciones con efectos dependen de un estado que no se ve en la firma y producen resultados que cambian entre llamadas. `SE-064` no condena los efectos (sin ellos un programa no leería ni escribiría nada) sino que pide **ubicarlos**: se aíslan en adaptadores y el núcleo recibe valores. La decisión que cambia es dónde se hacen las cosas con el mundo exterior: en pocos lugares conocidos, no esparcidas por todo el código.

## Cómo funciona

Lo que define el efecto es la dependencia o el cambio externo:

- **Efecto de salida:** escribir un archivo, imprimir, enviar un mensaje, modificar un objeto recibido.
- **Efecto de entrada (dependencia oculta):** leer el reloj, el generador aleatorio, el entorno o la red. Una función que consulta la hora no es pura aunque no escriba nada, porque su resultado depende de algo que no es un argumento.

Cuando el cálculo está mezclado con los efectos, probarlo exige simular el exterior. Cuando se separa, el **núcleo** (puro) recibe valores y devuelve valores, y los **adaptadores** (en los bordes) leen y escriben. Así el cálculo «se prueba sin red ni disco». Una consecuencia práctica aparece en `SE-068`: importar un módulo que abre archivos o red al importarse es un efecto a nivel de módulo; la corrección es moverlos a `main()` o a una función llamada explícitamente. Y en `SE-064`, cuando se pregunta si una función puede imprimir, la respuesta es que imprimir es un efecto; en la práctica se **confina**: la función calcula y devuelve, y quien llama imprime.

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
- **Memoizar funciones con efectos.** El efecto se ejecuta solo la primera vez (`SE-074`).

## Límites y cuándo no aplica

La distinción puro/impuro es útil pero no es binaria en la práctica: escribir un registro de depuración es un efecto que casi nadie quiere esconder en un adaptador. El costo de aislarlos tiene un límite: en un script corto, separar núcleo y borde puede ser más estructura que valor. Y «puro» no equivale a «correcto» ni a «rápido»: una función pura puede contener un error o ser costosa.
