# Salida accesible

## Definición

La **salida accesible** es, en `SE-106`, la propiedad de que lo que un programa muestra a quien lo desarrolla (**trazas, diagnósticos y mensajes**) pueda percibirse y entenderse sin depender de un solo canal sensorial. Se concreta en tres requisitos: **texto seleccionable** (se puede copiar, buscar y leer con un lector de pantalla), **orden de lectura** coherente y **niveles claros** (se distingue un error de una advertencia por algo más que el color). Los diagramas aportan su **notación fuente** o una explicación, no solo la imagen. Es un requisito de calidad del entorno de desarrollo, no solo de las aplicaciones para usuarios finales.

## Por qué importa

Quien programa también puede tener baja visión, daltonismo o usar un lector de pantalla, o simplemente trabajar en un entorno con poca luz o con un terminal sin color. Una salida que solo se entiende por colores o por una imagen excluye a esas personas y, a todas, dificulta buscar y copiar un error. La decisión que cambia es cómo se escribe un mensaje: como texto que se puede procesar. `SE-106` observa que **una terminal con mensajes accionables suele ser una alternativa robusta a una vista exclusivamente visual**: el texto se puede leer, buscar, copiar y reenviar.

## Cómo funciona

Tres prácticas hacen accesible la salida:

- **Texto en lugar de imagen para lo que se debe leer.** Un error dentro de una captura de pantalla no se busca ni se lee con tecnología asistiva; el mismo error en texto, sí. Los diagramas se acompañan de su fuente (por ejemplo, el texto que los genera) o de una descripción.
- **Orden de lectura:** la salida se estructura de modo que, leída de arriba abajo, tenga sentido (qué falló, dónde, qué hacer), sin depender de la disposición espacial.
- **Más de un canal para el significado:** los **errores no se distinguen solo por color**; se añade símbolo, subrayado o texto («ERROR», «ADVERTENCIA»). `SE-106` documenta el síntoma: los errores solo se distinguen por el color porque el color es el único canal; la corrección es añadir símbolo, subrayado o texto. De manera análoga, un tema de colores «se ve bien» y no cumple porque se juzgó a ojo; se calcula la **razón de contraste** con la fórmula de las pautas WCAG.

## Ejemplo

Una salida solo con color:

```text
(en rojo) conexión fallida
(en verde) conexión establecida
```

Una persona con daltonismo rojo-verde no distingue ambas. La versión accesible:

```text
[ERROR] conexión fallida: puerto 5432 rechazó la conexión. Compruebe que el servicio esté activo.
[OK]    conexión establecida con 127.0.0.1:5432
```

Lleva texto de nivel, dice qué falló y qué hacer, y se puede copiar a una incidencia. El color puede añadirse como refuerzo, pero el significado no depende de él.

## Errores y confusiones comunes

- **Color como único canal.** Excluye a quien no lo percibe y no sobrevive a un terminal sin color.
- **Juzgar el contraste a ojo.** Se calcula con la fórmula.
- **Capturas de pantalla como forma de reportar errores.** El texto es más útil y accesible.
- **Pensar que accesibilidad es solo asunto del producto final.** También el entorno de desarrollo debe serlo.

## Límites y cuándo no aplica

Una lista de verificación básica no sustituye una auditoría con personas y tecnologías asistivas (`SE-106`): puede cumplir pautas y seguir siendo difícil de usar. Algunas salidas son inherentemente visuales (gráficos, mapas de calor), y allí se ofrecen alternativas textuales (tabla de datos, descripción). La accesibilidad completa de una aplicación va más allá de la salida del entorno de desarrollo.
