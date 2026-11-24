# Camino crítico

## Definición

El **camino crítico** es la secuencia de elementos dependientes de mayor duración acumulada: fija la duración mínima de la entrega si las duraciones fueran las supuestas. Es el sentido de `SE-186`. Las clases lo reutilizan con el mismo núcleo en otros grafos: la cadena de requisitos dependientes (`SE-156`), la cadena de jobs de una canalización (`SE-482`), la cadena de dependencias al aplicar infraestructura como código (`SE-402`) y, en `SE-340`, la secuencia de llamadas de la que depende la respuesta al usuario.

## Por qué importa

Dice dónde mirar. Cualquier retraso en un elemento del camino crítico retrasa la entrega; un retraso fuera de él, dentro de su holgura, no. Cambia la decisión de dónde poner a la gente, qué dependencia externa atacar primero y qué optimizar: acelerar un eslabón que no es crítico no acorta nada.

## Cómo funciona

El cálculo es el recorrido del grafo de dependencias sumando duraciones y quedándose con la cadena más larga; la suma es la duración mínima con recursos ilimitados (`SE-156`). La consecuencia práctica es que añadir recursos tiene un piso: en una canalización, añadir ejecutores no baja de un mínimo porque el camino crítico ya está alcanzado (`SE-482`); hay que acortar su eslabón más largo.

`SE-186` añade el matiz decisivo: calcularlo con duraciones típicas sirve para saber dónde mirar, y engaña si se toma como duración esperada. Con duraciones inciertas, otros caminos casi tan largos también se vuelven críticos en una parte de las ejecuciones. La noción útil es la **probabilidad de que un elemento sea crítico**, no su etiqueta determinista. En una red ancha, comprometer el plazo del camino crítico determinista subestima el riesgo.

## Ejemplo

`SE-186` incluye un fragmento que calcula la duración de una red pequeña cuyo camino crítico es de 6 días, y pide predecir antes de ejecutar cuánto vale la duración si el elemento C tarda un día más. La respuesta depende de si C está en el camino crítico: si lo está, la entrega se mueve un día; si tiene holgura, puede no moverse. El ejercicio entrena justo esa lectura.

## Errores y confusiones comunes

- **Todo el equipo espera la misma entrega externa.** El camino crítico pasa por una dependencia; corrección de `SE-186`: dividir el trabajo para que avance sin ella, con un contrato o un doble.
- **El plan supone que todo es secuencial.** Las dependencias no están declaradas; escribir el grafo y calcular (`SE-156`).
- **Esperar que más recursos acorten siempre.** No bajan del camino crítico (`SE-482`).
- **Tratarlo como duración esperada.** Es un mínimo bajo supuestos, no un pronóstico.

## Límites y cuándo no aplica

Presupone que las dependencias están completas y que las duraciones son las supuestas; con incertidumbre alta, o redes anchas con muchos caminos casi iguales, la etiqueta determinista pierde valor y conviene simular y hablar de probabilidad de ser crítico. Tampoco modela restricciones de recursos compartidos: el cálculo habla de recursos ilimitados. Y no dice nada sobre la calidad o el valor de lo que se entrega, solo sobre el tiempo.
