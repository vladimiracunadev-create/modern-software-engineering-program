# Costo de construir

## Definición

El **costo de construir** es el gasto necesario para dejar el producto en uso: diseño, desarrollo, pruebas, migración inicial y documentación mínima. Es el sentido de `SE-134`, donde se distingue de dos costos hermanos: el de operar (mantener, alojar, dar soporte) y el de oportunidad (lo que se deja de hacer por hacer esto). Es el costo visible, el que se aprueba en un presupuesto.

## Por qué importa

Cambia qué se aprueba. Según `SE-134`, el costo de construir pesa menos de lo que se cree en el costo de propiedad: un presupuesto que cubre la construcción y no la operación alcanza para llegar y no para seguir. Por eso la clase propone aprobar un costo de propiedad a cinco años con intervalo, no una cifra de construcción aislada.

## Cómo funciona

Se estima por trabajo y por insumos, y casi siempre se subestima porque se estima lo conocido. Dos reglas lo corrigen. Primero, su rango debe incluir lo que el equipo todavía no sabe (integraciones, requisitos que cambian), de modo que se expresa con mínimo, moda y máximo y no con un número único. Segundo, se declara quién estimó y cuándo, para poder comparar con el costo real y mejorar el siguiente rango.

Combinar estimaciones exige cuidado. Si un plan de «100 días» se retrasa casi siempre, la causa que da `SE-134` es que se sumaron medianas: la suma de medianas no es la mediana de la suma cuando las partes son asimétricas y están correlacionadas. La corrección es prometer el percentil 80 del plan y declarar la correlación que se supuso.

## Ejemplo

En la plataforma de entregas, `cost-model.md` contiene una fila por rubro (construcción, mantenimiento, infraestructura, soporte, otro) con mínimo, moda, máximo, quién estimó, fecha y fuente de comparación. El total se calcula siempre desde las filas y ningún total se informa sin su percentil 80. Cuando existan costos reales, cada fila se compara con su estimación.

## Errores y confusiones comunes

- **El presupuesto alcanza para construir y no para seguir.** Se aprobó solo la construcción; aprobar el costo de propiedad a cinco años con intervalo.
- **Sumar medianas.** El plan se retrasa casi siempre; prometer el percentil 80.
- **Un número sin rango.** Oculta la incertidumbre y se lee como compromiso.
- **Estimar solo lo conocido.** Las integraciones y requisitos cambiantes son justo lo que no se ve.

## Límites y cuándo no aplica

Las cifras de `SE-134` provienen de experimentos con datos sintéticos: no se midió el costo de ninguna plataforma real, y la distribución lognormal y la correlación única son supuestos de la clase. Sirve para comparar y decidir bajo incertidumbre, no para predecir un costo concreto. Y no basta por sí solo: sin los costos de operación y de oportunidad, decide con una parte del cuadro.
