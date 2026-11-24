# Factor de camión

## Definición

El **factor de camión** (*bus factor*) es el número mínimo de personas cuya salida deja sin conocedor a una parte significativa del sistema. `SE-530` lo presenta así; `SE-518` lo define como el mínimo de personas que, al irse, dejan a un proyecto o a un archivo sin conocimiento clave, y `SE-215` como el número cuya salida dejaría al proyecto sin conocimiento suficiente de una parte esencial. La versión operativa más precisa es la de Avelino et al., que `SE-518` recoge: el mínimo de autoras cuya salida deja abandonados a más de la mitad de los archivos de un repositorio, con el abandono medido por la autoría.

## Por qué importa

Cambia dónde se invierte en repartir conocimiento. Mide cuánto depende el conocimiento de pocas personas, y por eso orienta decisiones concretas: dónde exigir una segunda persona que conozca el código, qué rotaciones hacer y qué documentar primero. Un factor de 1 significa que una sola salida deja zonas del sistema sin nadie que las entienda.

## Cómo funciona

El cálculo operativo prueba combinaciones de salidas: se retiran personas del conjunto de autoras hasta que más de la mitad de los archivos queda sin ninguna autora que los conozca; el número mínimo de retiradas necesarias es el factor. La clase incluye un fragmento que lo calcula para un repositorio pequeño y pide predecir el resultado antes de ejecutarlo.

La definición tiene límites claros, que `SE-518` subraya: la autoría en el historial no equivale a conocimiento (alguien pudo escribir un archivo y olvidarlo, o conocer a fondo uno que nunca tocó). Es, por tanto, una aproximación que conviene contrastar con una conversación y no tomar como medida exacta. Los síntomas de un factor bajo, según `SE-530`, son un archivo que espera semanas por una persona (propiedad fuerte sin segundo conocedor; corrección: revisión obligatoria por una segunda persona y rotación) o fronteras por capa que obligan a tres equipos en cada cambio (corrección: organizar por dominio).

## Ejemplo

En el taller de `SE-215`, se reconstruye conocimiento perdido de un módulo cuya única autora se fue. El cálculo del factor ya lo anticipaba: el módulo dependía de una sola persona. La recuperación pasa por leer el historial, documentar decisiones y asignar un segundo conocedor.

## Errores y confusiones comunes

- **Equiparar autoría con conocimiento.** El historial es una aproximación.
- **Usarlo como ranking de personas.** Mide riesgo del sistema, no valor individual.
- **Corregirlo solo documentando.** Se necesita práctica compartida: revisión cruzada y rotación.
- **Calcularlo una vez.** Cambia con cada salida e ingreso.

## Límites y cuándo no aplica

No ve el conocimiento que no deja huella en el repositorio (operación, decisiones de negocio, contexto de clientes). En equipos de una persona es 1 por definición. Y un factor alto no garantiza que el conocimiento sea bueno, solo que está repartido.
