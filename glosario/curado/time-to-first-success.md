# Time to first success

## Definición

El **time to first success** (tiempo hasta el primer éxito) es el tiempo que una persona nueva necesita, desde que decide probar un producto técnico hasta que obtiene **un resultado significativo**. `SE-118` lo plantea como un requisito sobre el **camino mínimo**: debe producir un resultado que le importe a quien lo ejecuta, con **precondiciones explícitas**. Es una medida de experiencia de desarrollo (DX), la segunda etapa del recorrido tras evaluar el producto y la primera que se puede cronometrar.

## Por qué importa

Los primeros minutos con una biblioteca o API deciden si se sigue usando. Si el primer resultado tarda horas o exige conocimiento no documentado, muchas personas abandonan antes de la primera llamada. `SE-118` documenta ese síntoma: los usuarios abandonan por demasiados pasos o requisitos previos ocultos, y la corrección es medir el recorrido con alguien nuevo y eliminar pasos o dar valores por defecto. La decisión que cambia es qué se optimiza primero: el camino de menor fricción hacia algo que funcione, no la cobertura completa de funciones.

## Cómo funciona

La medida se sostiene en tres reglas:

- **Resultado significativo.** No basta con «imprimir hola»: debe ser algo que muestre el valor real del producto (una consulta con datos de ejemplo, un caso resuelto).
- **Precondiciones explícitas.** Qué hace falta antes de empezar (versión del lenguaje, credenciales, permisos) se declara al inicio, no se descubre al fallar.
- **Medición con alguien nuevo.** Se observa a una persona o un entorno nuevo recorriendo el camino, cronometrando y anotando **dónde pide contexto no documentado**. Quien construyó el producto no puede medirlo porque ya conoce los atajos.

Hay un riesgo que `SE-118` señala: **reducir pasos mediante «magia oculta» puede empeorar el diagnóstico**. Si el producto adivina la configuración, crea archivos o elige valores sin decirlo, el primer éxito llega rápido, pero cuando algo falla, la persona no sabe qué ocurrió ni cómo corregirlo. El objetivo no es el menor número de pasos a toda costa, sino un camino corto y comprensible.

## Ejemplo

El *quickstart* del SDK del programa, medido con alguien nuevo (ilustración, tiempos inventados):

```text
00:00  lee la página de inicio
01:10  pip install engineering-sdk                    (precondición: Python >= 3.9, declarada)
02:30  copia el ejemplo y lo ejecuta -> error: falta el archivo casos.json
       (contexto no documentado: el ejemplo no lo incluía)
04:40  añade el archivo de ejemplo al paquete -> resultado: "siguiente caso: #2"
```

El tiempo hasta el primer éxito fue 4 min 40 s, y el bloqueo se registra con su causa. La corrección es incluir el archivo de datos de ejemplo en el paquete o generar uno al ejecutar con un mensaje que lo diga, no adivinarlo en silencio.

## Errores y confusiones comunes

- **Medirlo el propio equipo.** Conoce los atajos y subestima el tiempo.
- **Un primer éxito trivial.** Si no muestra valor, no cuenta.
- **Esconder pasos con magia.** Acelera el inicio y daña el diagnóstico posterior.
- **Optimizar solo el inicio.** El recorrido completo incluye integrar, depurar y actualizar.

## Límites y cuándo no aplica

Una evaluación interna de DX no sustituye investigación diversa ni soporte real (`SE-118`): el tiempo de una persona no es el de todas. La métrica captura el inicio, no la experiencia sostenida con el producto. En productos con una sola población conocida y entrenada (una herramienta interna), el esfuerzo de optimizarlo puede ser innecesario; se justifica donde la adopción es una decisión libre de quien usa.
