# Código de salida

## Definición

El **código de salida** es el entero con que un proceso informa a su padre cómo terminó (`SE-220`). Por convención, 0 es éxito; en `SE-113` el cero es éxito contractual y los valores distintos de cero clasifican uso inválido, datos rechazados, dependencia fallida o error interno según una matriz publicada. `SE-028` lo presenta como el valor con el que un proceso comunica una categoría de resultado.

## Por qué importa

Es la parte de una CLI que el sistema operativo y la integración continua interpretan sin leer una palabra (`SE-113`). Un script que encadena comandos, un job de CI o un orquestador deciden continuar o abortar a partir de ese número. Si un programa devuelve 0 tras fallar, la automatización sigue con datos malos; si devuelve 1 por cualquier cosa, nadie distingue un uso incorrecto de un fallo de la dependencia.

## Cómo funciona

Al terminar, el proceso entrega un entero al padre (`SE-028`, `SE-029`). El intérprete de comandos lo expone y permite componerlo: continuar solo si el anterior tuvo éxito, o reaccionar según el valor. El diseño profesional (`SE-113`, `SE-220`) consiste en:

- publicar una **tabla de códigos** (por ejemplo, uso inválido, datos rechazados, dependencia no disponible, error interno);
- una prueba por cada valor;
- reservar los detalles para otro canal: el código no transporta el detalle, que viaja por stderr o por JSON estructurado.

Por eso la separación habitual es: stdout para el resultado, stderr para diagnóstico y el código para la categoría. `SE-072` lo aplica en una herramienta de línea de comandos probada, y `SE-583` lo usa como contrato de las compuertas de validación.

## Ejemplo

`SE-113` prueba la CLI con `subprocess` y entradas explícitas: `capture_output=True`, entorno controlado y comparación del código de salida y de los bytes. Así se vieron la codificación y el CRLF; llamar a `main()` directamente no pasa por la tubería. Ilustración:

```python
r = subprocess.run(["herramienta", "--help"], capture_output=True)
assert r.returncode == 0
```

## Errores y confusiones comunes

- **`--help` o un error de uso devuelve un código inesperado.** Causa: los códigos no se documentaron; corrección: tabla en el README y una prueba por valor (`SE-113`).
- **Usar el código como mensaje.** Solo comunica una categoría; el detalle va por otro canal.
- **Probar la función y no el proceso.** Llamar a `main()` no verifica el código real que ve el padre.

## Límites y cuándo no aplica

Un entero comunica poco: distinguir causas finas exige salida estructurada. La convención 0/no cero es universal en los shells, pero el significado de cada valor no cero lo fija cada programa, y la tabla de `SE-113` es contrato de esa herramienta, no un estándar general. Para servicios que no terminan, el estado se expresa por otros medios (sondas, métricas).
