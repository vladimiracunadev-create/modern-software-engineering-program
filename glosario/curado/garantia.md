# Garantía

## Definición

Una **garantía** es un compromiso verificable sobre el comportamiento de una operación bajo condiciones y fallos declarados (`SE-396`). Una garantía bien escrita dice qué operación, bajo qué fallo y con qué límite. No es un adjetivo («confiable») ni una intención: es una afirmación que se puede comprobar y que puede cumplirse o violarse.

## Por qué importa

Quien usa una operación decide en función de lo que cree garantizado. Si cree más de lo prometido, construye sobre arena; si la promesa es vaga, nadie puede probarla. Escribir garantías precisas cambia qué se comunica a otros equipos, qué se prueba y qué se asume.

## Cómo funciona

Una garantía tiene tres partes: la **operación** (guardar una entrega), el **fallo** o condición declarados (caída del nodo, red particionada) y el **límite** (en cuánto tiempo, con qué orden, a quién).

En redes (`SE-040`) se ve la ausencia de garantías como diseño: UDP preserva fronteras de datagrama y aporta comprobación mínima, pero no promete entrega, orden, unicidad ni control de congestión para la aplicación. Eso es adecuado cuando importa la actualidad y perder una muestra es mejor que acumular retraso (voz, vídeo, telemetría de alta frecuencia), o cuando la aplicación necesita sus propias reglas; quien lo elige asume orden, duplicados, pérdida y congestión, y QUIC ofrece esas garantías sobre UDP. En `SE-396`, la garantía de un sistema de entregas distingue estados («recibida» y «guardada») porque el acuse en el momento de encolar no garantiza persistencia.

## Ejemplo

`SE-396`: un estudiante tiene acuse pero no entrega porque el acuse se emitió al encolar sin distinguir estados. La garantía corregida: «recibida» significa encolada; «guardada» significa persistida con réplica. Ilustración:

```text
Garantía: tras responder "guardada", la entrega sobrevive a la caída de un nodo y es legible en ≤ 5 s.
```

## Errores y confusiones comunes

- **Acuse sin estados.** Causa: se emite el acuse al encolar sin distinguir qué se cumplió; corrección: estados «recibida» y «guardada» en la garantía (`SE-396`).
- **Confundir política con garantía.** Round robin, menor carga o hashing son políticas de selección, no garantías de igualdad (`SE-044`).
- **Asumir garantías que el protocolo no da.** Esperar orden o entrega de UDP.

## Límites y cuándo no aplica

Una garantía solo vale bajo las condiciones declaradas: fuera de ellas no se promete nada. Garantías muy fuertes cuestan latencia o disponibilidad, así que no siempre conviene exigir la más fuerte. Y una garantía no verificada es una intención: debe tener una prueba o una observación que la sostenga.
