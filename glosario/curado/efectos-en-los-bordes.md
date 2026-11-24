# Efectos en los bordes

## Definición

**Efectos en los bordes** es el patrón de diseño por el que el **núcleo** de un programa calcula una decisión a partir de valores, mientras los **adaptadores** situados en los límites leen entradas y escriben salidas. En `SE-074` el ejemplo es: el núcleo calcula una recomendación y los adaptadores leen JSON o escriben texto. El término designa tanto la separación como el lugar donde se confinan los efectos: el borde del sistema, no su interior.

## Por qué importa

Si el cálculo y el contacto con el exterior están mezclados, repetir una decisión implica repetir su efecto: reenviar el correo, escribir otra vez el archivo, volver a consultar el servicio. `SE-074` lo plantea como la razón práctica de la separación: permite **repetir la decisión sin repetir un efecto**. La decisión profesional que cambia es cómo se prueba y se reproduce el comportamiento: el núcleo se prueba con valores y se vuelve reproducible; los adaptadores, más delgados, se prueban aparte con dobles o con pruebas de integración.

## Cómo funciona

La estructura tiene tres zonas:

1. **Adaptador de entrada:** lee el archivo, la solicitud o el mensaje y lo convierte en valores del dominio (el parseo del dominio).
2. **Núcleo:** funciones que reciben esos valores y devuelven un resultado. No abren archivos, no consultan el reloj, no hacen red.
3. **Adaptador de salida:** convierte el resultado en texto, archivo o llamada y lo envía.

El mecanismo que lo hace valer es que **todo lo que el núcleo necesita llega como argumento**. Si necesita la hora, se le pasa como valor; si necesita datos, se le pasan. Así, la misma entrada produce siempre la misma decisión. `SE-074` señala dónde se rompe el límite: cuando una función **supuestamente pura** consulta el reloj, el entorno o un *singleton* sin declararlo. La dependencia oculta devuelve al núcleo la imprevisibilidad que se quería dejar fuera. La separación también se conoce como núcleo funcional con cáscara imperativa (*functional core, imperative shell*) en la literatura de diseño; aquí se usa el nombre del programa.

## Ejemplo

El motor de reglas del programa decide una recomendación. Sin separación, la función lee un JSON, consulta la hora, decide y escribe en pantalla. Con separación:

```python
def recomendar(caso, politica, ahora):      # núcleo: valores in, valor out
    return "revisar" if caso["monto"] > politica["umbral"] else "aprobar"

def main(ruta):                              # borde: lee y escribe
    caso = json.load(open(ruta))
    resultado = recomendar(caso, POLITICA, datetime.now())
    print(f"Recomendación: {resultado}")
```

Para reproducir una decisión pasada se llama a `recomendar` con el mismo caso, la misma política y la misma hora registrada, sin tocar archivos ni reloj. El tiempo entra como argumento (`ahora`), no se consulta dentro.

## Errores y confusiones comunes

- **Dependencias ocultas en el núcleo.** El reloj, el entorno o un *singleton* leído en medio del cálculo.
- **Memoizar la parte con efectos.** Tras añadir un caché, un efecto «desaparece» porque ya no se ejecuta.
- **Adaptadores con lógica de negocio.** La decisión se filtra al borde y vuelve a mezclarse.
- **Separar por capas sin separar efectos.** Tener carpetas `servicios` y `repositorios` no impide que el núcleo abra archivos.

## Límites y cuándo no aplica

La descomposición procedural no define por sí misma cómo representar entidades con identidad o ciclos de vida largos (`SE-074`): el patrón supone transformaciones de datos. En programas cuyo propósito principal son los efectos (copiar archivos, sincronizar servicios), el «núcleo» es casi vacío y la separación aporta poco. Y cuando el cálculo depende de datos que solo se saben a mitad del proceso (consultas encadenadas), pasar todo como argumento antes de empezar no siempre es posible.
