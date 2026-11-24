# Contexto delimitado

## Definición

Un **contexto delimitado** (*bounded context*) es la frontera dentro de la cual un modelo y su lenguaje son consistentes y tienen un significado único y preciso (`SE-546`, `SE-329`, `SE-381`). Es un concepto del diseño orientado al dominio: la consistencia se garantiza dentro del límite, no en todo el sistema.

## Por qué importa

La misma palabra significa cosas distintas en áreas distintas del negocio. Pretender un modelo único para todo el sistema produce, según `SE-546`, un objeto con campos para todos los usos que nadie entiende por completo. La decisión que cambia es dónde trazar las fronteras: en lugar de unificar definiciones, se acepta que cada contexto tiene la suya y se invierte en una traducción explícita entre ellas.

## Cómo funciona

`SE-546` da un ejemplo sobre la palabra «entrega». En el contexto académico, una entrega es el trabajo de una persona estudiante, con un estado «pendiente» o «recibida». En el contexto de avisos, una entrega es un elemento con vencimiento y un indicador de si ya se entregó. Los dos contextos no necesitan acordar una definición única; necesitan una **traducción explícita en su frontera**.

Esa traducción es el punto de contacto: la capa anticorrupción convierte el vocabulario de un contexto al del otro, y es el único lugar donde se conocen ambos. Dentro de cada contexto, el modelo puede ser simple y coherente, porque no tiene que servir a usos ajenos. Las fronteras se relacionan en el mapa de contextos, que registra qué contexto depende de cuál y de qué manera: por ejemplo, adoptando el modelo ajeno tal cual (conformista) o traduciéndolo. `SE-329` lo trata como una decisión de arquitectura de dominio y `SE-381` como una frontera de integración, donde un modelo y su vocabulario tienen un significado único.

## Ejemplo

El contexto académico guarda `entrega` con `estado = recibida`. El contexto de avisos guarda `entrega` con `vence_en` y `entregada = true/false`. Entre ambos, una función traduce `recibida` a `true`. Si mañana el contexto académico añade «en revisión», se decide en un solo lugar si cuenta como entregada. Ejemplo de `SE-546`.

## Errores y confusiones comunes

- **Un modelo único para todo el sistema**: produce un objeto con campos para todos los usos.
- **Creer que un contexto es un servicio**: un contexto delimitado es una frontera de modelo y lenguaje; puede o no coincidir con un servicio desplegable.
- **Fronteras sin traducción explícita**: el vocabulario de uno se filtra al otro.
- **Dibujar el contexto por organigrama** en vez de por significado de las palabras.

## Límites y cuándo no aplica

`SE-546` lo limita expresamente: los contextos delimitados importan cuando hay dos o más modelos con la misma palabra; en un sistema con un solo modelo no hacen falta. Trazar fronteras tiene costo (traducción, mantenimiento) y un sistema pequeño o con un vocabulario único no lo recupera. Y las fronteras no se descubren por decreto: dependen de entender el dominio con quienes lo conocen.
