# Dependencia externa

## Definición

Una **dependencia externa** es una dependencia cuya fecha y calidad controla alguien ajeno al equipo (SE-186): la entrega de otro equipo, una aprobación, un proveedor. Se opone a la dependencia interna, que el equipo puede reordenar o acelerar.

## Por qué importa

Cada dependencia externa añade una probabilidad de espera, y con varias, esperar es lo normal. Un plan que supone que todas llegan a tiempo es optimista por construcción. Cambia cómo se planifica: la espera se trata como el caso habitual y se diseña el trabajo para seguir avanzando mientras llega.

## Cómo funciona

SE-186 da la cuenta: la probabilidad de que **todas** las dependencias lleguen a tiempo es el **producto** de las individuales. Con diez dependencias de 90 % de fiabilidad cada una, la probabilidad conjunta es 0,9¹⁰ ≈ 35 %. Por eso un plan con muchas dependencias externas casi siempre se retrasa en alguna.

Dos prácticas lo mitigan. Primero, **pedir una fecha de aviso** a cada proveedor (cuándo sabrán si llegan tarde) y acordar una alternativa o un doble; la clase pide acordar con cada proveedor una fecha de aviso. Segundo, **tener trabajo útil que hacer mientras se espera**, dividiendo el trabajo para que avance sin la dependencia, con un contrato de interfaz acordado de antemano o un doble.

En el análisis de la red, las dependencias externas que están en el **camino crítico** son las que más importan: un retraso allí retrasa la entrega. En el ejemplo de SE-186, el equipo de la plataforma dibuja la red de la entrega con 15 elementos propios y cuatro dependencias externas; calcula el camino crítico (10 días con medianas) y lo contrasta con la simulación, que da una media cercana a 14 y un percentil 85 cercano a 16: comunica «entre 12 y 16 días». De las cuatro externas, dos están en el camino crítico, y para cada una acuerdan una fecha de aviso.

## Ejemplo

Un plan necesita la API de calificaciones de secretaría, una aprobación legal y la nueva versión de una biblioteca. Con 90 %, 80 % y 95 % de probabilidad de llegar a tiempo, la probabilidad conjunta es 0,9 × 0,8 × 0,95 ≈ 68 %. Si además dos están en el camino crítico, el plazo prometido debe incluir ese riesgo. (Cifras ilustrativas con el cálculo de SE-186.)

## Errores y confusiones comunes

- **El plan cumple las fechas parciales y falla la final**: se sumaron fechas de caminos paralelos; corrección: simular la red y comunicar un rango.
- **Siempre hay una dependencia «casi lista» que llega tarde**: no se pidió fecha de aviso ni alternativa; corrección: acordar fecha de aviso y un doble.
- **Suponer independencia entre dependencias** cuando comparten un proveedor.
- **No tener trabajo alternativo mientras se espera.**

## Límites y cuándo no aplica

La cuenta supone independencia entre dependencias; si dos dependen del mismo proveedor, el riesgo se correlaciona. Las probabilidades individuales son estimaciones. Las dependencias externas contractuales (con penalizaciones) se gestionan de otro modo que las informales.
