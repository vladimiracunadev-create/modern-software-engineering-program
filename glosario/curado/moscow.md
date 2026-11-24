# MoSCoW

## Definición

**MoSCoW** es una técnica de priorización que clasifica los requisitos en cuatro categorías: lo que **debe** estar (*Must*), lo que **debería** (*Should*), lo que **podría** (*Could*) y lo que **no estará esta vez** (*Won't*). Las «o» del nombre son de relleno. Es el sentido de SE-150.

## Por qué importa

Obliga a decir «no» de forma explícita. En una conversación de alcance, la tendencia es a decir «sí, y también» a todo; la categoría Won't convierte el rechazo en un acuerdo visible. Cambia el modo de negociar el alcance: en lugar de discutir cada ítem en abstracto, se discute en qué categoría va.

## Cómo funciona

Cada requisito recibe una categoría. Must son los imprescindibles: sin ellos el producto no cumple su propósito; Should son importantes pero con alternativa; Could son deseables; Won't quedan fuera de esta entrega, y se anotan para que no reaparezcan como sorpresa.

SE-150 señala su debilidad principal: **no impone un presupuesto**. Si cada interesado puede marcar Must, la categoría crece hasta cubrir casi todo y deja de ordenar. Este es el síntoma «casi todo es Must». La causa es que la técnica clasifica pero no limita. Las guías de la técnica recomiendan limitar Must a una fracción del esfuerzo disponible; la clase subraya que ese límite es una decisión del equipo, no una propiedad del método. La corrección es fijar un tope como fracción del esfuerzo y desempatar con una regla escrita.

Otra falla que SE-150 menciona en el mismo contexto de priorización: un plan aprobado que no se puede construir porque se ordenó por valor sin comprobar dependencias. La corrección es verificar el cierre del conjunto (que todo lo que un Must necesita también esté dentro) antes de aprobar. Y todo el orden se registra en una tabla con la razón y quién decidió.

## Ejemplo

El trimestre de la plataforma tiene 30 días-persona de esfuerzo disponible y los interesados piden requisitos que suman 90. Si cada área marca los suyos como Must, el Must suma 70: no cabe. Con un tope del 60 % del esfuerzo para Must (18 días), el equipo debe decidir qué baja a Should. Si un Must depende de otro marcado Could, hay que subir el segundo o bajar el primero. (Cifras ilustrativas; la clase fija el principio, no estos números.)

## Errores y confusiones comunes

- **Casi todo es Must**: no hay límite; corrección: tope como fracción del esfuerzo.
- **El plan aprobado no se puede construir**: se ordenó sin dependencias.
- **Confundir Won't con «nunca»**: significa «esta vez».
- **Priorizar sin registrar quién decidió y por qué.**

## Límites y cuándo no aplica

MoSCoW da una clasificación, no un orden fino dentro de cada categoría: para ordenar hacen falta otras técnicas (valor, costo, riesgo). No sustituye la negociación de intereses, que a veces transforma un conflicto en una solución que satisface a ambos. Con pocos requisitos y un solo decisor, la técnica aporta poco.
