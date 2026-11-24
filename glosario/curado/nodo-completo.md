# Nodo completo

## Definición

Un **nodo completo** de un árbol de métricas es un nodo con nombre, fórmula o fuente, responsable nombrado, decisión que informa y, en la raíz, métrica contraria (SE-143). Es la unidad de un árbol de métricas, que descompone una métrica raíz (por ejemplo, ingresos o entregas aceptadas) en factores y hojas medibles.

## Por qué importa

Un nodo sin responsable, fuente o decisión es una métrica sin dueño ni uso. Un árbol con nodos incompletos se ve bien en un diagrama y no sirve para actuar: nadie sabe de dónde sale cada cifra ni qué se hace con ella. Cambia la disciplina de construir y mantener un árbol: cada nodo se añade con todos sus campos o no se añade.

## Cómo funciona

SE-143 enumera los campos de cada nodo:

- **nombre**;
- **fórmula** (si el nodo no es hoja, cómo se calcula a partir de sus hijos) o **fuente** (si es hoja, de dónde viene el dato);
- **responsable nombrado**, una persona o un rol con nombre, **no «el equipo»**;
- **decisión que informa**, qué se hace distinto si el valor cambia;
- en la raíz, una **métrica contraria** que vigila el daño posible de optimizarla.

La razón de cada campo es la ausencia que evita. Una hoja con fuente pero sin decisión **no se usa**; una con decisión pero sin fuente **no se puede calcular**. Sin responsable, nadie atiende cuando el valor se desvía. Sin fórmula, la raíz no se puede recuperar de las hojas.

El árbol de la plataforma vive en un archivo con una fila por nodo, un validador y dieciséis mutaciones que miden qué detecta. El contrato es que **ningún nodo se añade sin los cinco campos** y que cada cambio de fórmula conserva la raíz exacta. Dos fallos con causa conocida: el árbol con dos raíces (se mezclaron métricas de dos objetivos; se elige una raíz y se mueve la otra a una guarda) y la raíz que no se recupera de las hojas (la fórmula suma donde debía multiplicar; se valida la aritmética con los valores declarados).

El validador comprueba la completitud de forma mecánica; que la decisión sea relevante o que el responsable sea adecuado lo juzga una persona.

## Ejemplo

Raíz: «entregas aceptadas a tiempo por semana» = «estudiantes activos» × «entregas por estudiante» × «tasa de aceptación a tiempo». Nodo hoja «tasa de aceptación a tiempo»: fuente, tabla de entregas; responsable, la coordinadora de producto; decisión que informa, si se revisa el flujo de validación; sin métrica contraria porque no es la raíz. La raíz lleva como contraria la tasa de reclamos. (Árbol ilustrativo en el estilo de SE-143.)

## Errores y confusiones comunes

- **Árbol con dos raíces**: se mezclaron objetivos.
- **Raíz que no se recupera de las hojas**: error de aritmética (suma en lugar de producto).
- **Responsable «el equipo».**
- **Hojas con fuente pero sin decisión**: métricas decorativas.

## Límites y cuándo no aplica

Un árbol completo no garantiza que las métricas sean las correctas ni que el responsable actúe. El validador de SE-143 se evaluó con dieciséis mutaciones elegidas por el autor, de modo que su exactitud real es desconocida. Para métricas efímeras de un experimento, la formalidad completa puede ser excesiva.
