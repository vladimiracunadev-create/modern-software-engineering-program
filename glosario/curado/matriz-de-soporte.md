# Matriz de soporte

## Definición

Una **matriz de soporte** es la tabla de plataformas, versiones y escenarios realmente probados (`SE-030`). `SE-036` precisa lo esencial: separa las plataformas **objetivo** de los escenarios **efectivamente probados**. La diferencia es la información útil: una plataforma puede ser «objetivo» sin que nadie la haya probado, y entonces el soporte es una intención.

## Por qué importa

«Compatible» sin evidencia es un adjetivo. Una matriz publicada dice a quien usa el producto qué puede esperar y dice al equipo dónde falta cobertura. `SE-030` muestra el error contrario: llamar «compatible» a lo que solo inicia el shell, sin verificar las capacidades subyacentes. Cambia qué se promete y qué se prueba en integración continua.

## Cómo funciona

La matriz cruza ejes que importan al producto: sistema operativo, versión, arquitectura, intérprete o runtime, y escenarios (instalación limpia, actualización, política corporativa restrictiva). Cada celda tiene un estado con su evidencia: probada y pasa, probada y falla, no probada. En el proyecto de kit de diagnóstico multiplataforma (`SE-036`), la matriz acompaña a los adaptadores: cada adaptador declara qué capacidades ofrece y la matriz registra en qué combinaciones se ejecutó la suite. La celda «no probada» es explícita: no se rellena por analogía.

La causa de que sea útil es que la compatibilidad no se hereda: que algo funcione en Linux no dice nada de Windows, ni de una versión distinta del intérprete.

## Ejemplo

```text
| Plataforma     | Intérprete | Instalación | Diagnóstico | Estado           |
| Ubuntu 24.04   | 3.12       | probada     | probada     | soportada        |
| Windows 11     | 3.12       | probada     | probada     | soportada        |
| macOS 14       | 3.12       | no probada  | no probada  | objetivo, sin evidencia |
```

La fila de macOS dice la verdad: es objetivo, pero no hay evidencia, por lo que no se anuncia como soportada.

## Errores y confusiones comunes

- **«Compatible» significa que el shell inicia.** Causa: no se verificaron las capacidades subyacentes; corrección: publicar y probar una matriz de soporte (`SE-030`).
- **Copiar la matriz de otro producto.** Cada producto depende de capacidades distintas.
- **Matriz sin fecha ni versión.** Queda desactualizada y deja de ser una afirmación verificable.

## Límites y cuándo no aplica

Una matriz crece combinatoriamente: no se pueden probar todas las combinaciones, así que se escoge un subconjunto con criterio y se declara. Pasar en cada celda no prueba ausencia de defectos. Y `SE-030` advierte que no busca cubrir toda la sintaxis ni producir scripts idénticos en cada shell: la matriz documenta lo probado, no lo que debería funcionar.
