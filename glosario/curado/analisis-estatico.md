# Análisis estático

## Definición

El **análisis estático** es el examen del código fuente sin ejecutarlo, mediante reglas sobre su estructura, normalmente sobre su árbol sintáctico, para encontrar patrones de defecto. `SE-434` lo define así y `SE-464` lo reutiliza dentro del ciclo de desarrollo seguro. Se contrapone al análisis dinámico, que observa el programa mientras corre.

## Por qué importa

Decide qué defectos se descartan barato y cuáles no. Un analizador revisa cada cambio en segundos, sin datos de prueba y sin cansancio, así que es ideal para defectos *de patrón*: un parámetro por defecto mutable, una cláusula `except` sin tipo, una variable sin uso. Pero «pipeline verde» solo dice que ninguna regla vio nada, no que el código esté bien. Saber qué no ve evita delegar en él lo que corresponde a la revisión humana y a las pruebas.

## Cómo funciona

El código se convierte en un **árbol sintáctico**; una regla es una función que recorre los nodos y señala los que cumplen una condición. En Python, el módulo `ast` expone ese árbol, y `SE-434` escribe con él reglas que buscan argumentos por defecto mutables, `except` sin tipo y variables locales sin uso.

La causa de sus límites está en que las reglas se escriben sobre la **forma**, y la forma no es la intención. De ahí dos clases de error:

- **Falsa alarma:** la regla señala algo correcto. Una lista como parámetro por defecto usada a propósito como caché; una variable que se consulta de forma dinámica con `eval`.
- **Defecto no visto:** el defecto no tiene patrón. Un recorrido que empieza en uno en lugar de cero es sintácticamente impecable y ninguna regla de forma lo detecta.

Por eso la utilidad de una regla se mide con su **precisión** (qué fracción de sus alertas son defectos reales) y su **cobertura** (qué fracción de los defectos de esa clase encuentra), y no con la cantidad de alertas.

## Ejemplo

`SE-434` genera 300 funciones desde plantillas con semilla fija y siembra defectos con probabilidad conocida: argumento mutable (a veces como caché intencional), `except` sin tipo (a veces seguido de `raise`), variable sin uso (a veces usada con `eval` o con prefijo de guion bajo) y un recorrido que omite el primer elemento. Todas las funciones compilan. Tres reglas con `ast` buscan los tres primeros defectos y la cuarta no tiene regla. El resultado ilustra la tesis: las reglas encuentran lo que tiene forma, producen alguna falsa alarma en los casos intencionales, y el defecto lógico pasa intacto.

```python
import ast

def parametros_mutables(codigo):
    for nodo in ast.walk(ast.parse(codigo)):
        if isinstance(nodo, ast.FunctionDef):
            for d in nodo.args.defaults:
                if isinstance(d, (ast.List, ast.Dict, ast.Set)):
                    yield nodo.name, nodo.lineno
```

## Errores y confusiones comunes

- **El pipeline está verde y el defecto llegó a producción.** La regla no ve esa clase de defecto. Corrección (`SE-434`): listar lo que no ve cada comprobación y cubrirlo con revisión o pruebas.
- **Las alertas se ignoran.** Precisión baja: se mide, se afina con datos y se apartan las reglas ruidosas.
- **Confundirlo con una prueba.** No ejecuta nada, así que no demuestra comportamiento.
- **Tratar cero alertas como ausencia de defectos.** Solo hay ausencia de *esos patrones*.

## Límites y cuándo no aplica

`SE-434` trabaja con datos sintéticos, sin ninguna herramienta comercial ni revisión humana medidas, y las reglas se afinaron con los mismos casos que las evalúan, de modo que sus cifras ilustran el mecanismo, no el rendimiento de un analizador real. No sirve para defectos de lógica, de requisitos o de integración; para eso están las pruebas, la revisión y la observación en ejecución. En seguridad (`SE-464`) complementa, no reemplaza, las pruebas negativas y el modelado de abuso.
