# Valor

[↑ Glosario](../../README.md) · [← Valla](./valla.md) · [Valor de borde →](./valor-de-borde.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Un **valor** es un **dato concreto que el programa puede manipular**: un entero, una cadena, una lista. En [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) se precisa que es información concreta **interpretada según un tipo**: `800`, `800.0` y `'800'` son tres valores distintos, no intercambiables. Un valor no tiene por sí mismo nombre (eso lo da una variable), unidades ni dominio de negocio: eso no viene incluido en el tipo incorporado. Aquí se usa el sentido de la programación; el «valor» de negocio (el beneficio que aporta un producto) es otro concepto y se trata en otras clases.

## Por qué importa

Muchos defectos son confusiones entre valor y representación. [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) da el ejemplo de un indicador `--enabled false` que queda **activado**: `bool('false')` es `True`, porque la cadena `'false'` es un valor de tipo cadena no vacía, no el booleano falso. La decisión que cambia es cuándo se convierte un dato de texto en un valor del dominio: con un analizador explícito que acepte solo lo documentado, y no con las reglas implícitas de conversión del lenguaje.

## Cómo funciona

Cada valor pertenece a un tipo, que define qué operaciones admite y cómo se interpreta:

- **Enteros** de Python tienen precisión arbitraria, limitada en la práctica solo por la memoria.
- **`float`** aproxima números binarios: muchos decimales (como `0.1`) **no se representan exactamente**, y por eso `0.1 + 0.2` no da exactamente `0.3`.
- **`bool`** modela dos valores; **no sirve para distinguir «desconocido» de «falso»**: para eso hace falta un tercer estado (`None` u otro).
- Una función sin `return` explícito **devuelve `None`**, que es también un valor ([SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md)).

Una pregunta frecuente que [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) responde: ¿por qué `256 is 256` es verdadero y `257 is 257` no siempre? Porque **CPython reutiliza objetos enteros pequeños** (la clase midió que 256 sí y 257 no). Es un **detalle de implementación**: el programa debe comparar **valores** con `==` y reservar `is` (identidad de objeto) para `None`.

## Ejemplo

El ejercicio mínimo de [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) pide evaluar expresiones prediciendo valor y tipo antes de ejecutarlas:

```python
0.1 + 0.2        # 0.30000000000000004  (float: aproximación binaria)
bool('false')    # True                 (cadena no vacía)
3 / 2            # 1.5                  (división real)
3 // 2           # 1                    (división entera)
'3' * 2          # '33'                 (repetición de cadena)
```

Cada resultado depende del tipo del valor, no de su aspecto. Otros defectos del curso relacionados con valores: un valor negativo clasificado como válido porque la cadena de condiciones no tiene rama de entrada inválida ([SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md); se corrige con una guarda inicial que rechace el dominio no admitido) y el resultado de una función que depende de llamadas anteriores por un **valor por defecto mutable compartido** ([SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md); se usa `None` como centinela y se crea el objeto dentro).

## Errores y confusiones comunes

- **Confundir `'800'`, `800` y `800.0`.** No son intercambiables.
- **Convertir texto a booleano con `bool()`.** Cualquier cadena no vacía es verdadera.
- **Comparar valores con `is`.** Funciona por accidente para enteros pequeños.
- **Usar `float` para dinero.** No representa exactamente muchos decimales.

## Límites y cuándo no aplica

El tipo incorporado no lleva unidades ni dominio: `800` puede ser metros, segundos o pesos, y el programa no lo sabe. Esa información debe expresarse con tipos propios o con convenciones, o aparecen defectos silenciosos. Además, `bool` no distingue desconocido de falso ([SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md)). El concepto de valor como dato inmutable o mutable, y su relación con la identidad, se desarrolla en otras clases; aquí se trata el valor como dato concreto de un programa.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Condición](../c/condicion.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Cortocircuito](../c/cortocircuito.md), [Efecto](../e/efecto.md), [Enlace](../e/enlace.md).
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

**También se usa en** (486 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md), [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Valla](./valla.md) · [Valor de borde →](./valor-de-borde.md)
