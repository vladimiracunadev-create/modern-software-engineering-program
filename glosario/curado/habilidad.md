# Habilidad

## Definición

Una **habilidad** (*skill*) es un conjunto de instrucciones, a veces con scripts y documentos de apoyo, empaquetado con una descripción, que el agente carga cuando la tarea lo pide. Es la definición de `SE-570`. En Claude Code, una habilidad es un directorio con un archivo `SKILL.md` cuyo encabezado incluye un nombre y una descripción.

## Por qué importa

Resuelve el problema de poner todo el conocimiento en el contexto de partida. El agente ve las descripciones de todas las habilidades y carga el cuerpo solo cuando decide que una es relevante o cuando la persona la invoca: es **carga progresiva**. La descripción es siempre visible y barata; el cuerpo es caro y solo entra cuando se usa.

## Cómo funciona

El mecanismo crea otro problema: la **selección** depende de la descripción. Una descripción vaga o solapada con otra hace que se active la habilidad equivocada o que ninguna se active. Por eso se escriben con frases de activación concretas («úsala cuando…») y se eliminan los solapes entre habilidades.

## Ejemplo

`SE-570` (escenario hipotético, sin datos reales): el equipo de *Avisos* reduce las habilidades cargadas al arrancar a las seis que usa el proyecto, reescribe sus descripciones con frases de activación y quita el solape entre dos de ellas.

## Errores y confusiones comunes

- **El agente carga mucho contexto al arrancar.** Todas las habilidades completas en memoria; cargar descripciones y cuerpos bajo demanda.
- **Se activa la habilidad equivocada.** Descripciones vagas o solapadas; frases de activación y sin solapes.

## Límites y cuándo no aplica

Una habilidad es una instrucción, no un control: no impone nada. Lo que debe cumplirse siempre (bloquear una acción peligrosa) pertenece a un gancho de política o a un permiso, no a una habilidad que el agente puede no cargar.
