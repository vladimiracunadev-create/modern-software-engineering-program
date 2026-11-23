# Interfaz

## Definición

Una **interfaz** es el punto en que dos partes intercambian información, control o responsabilidad. El programa la usa en varias escalas con ese núcleo:

- **En la frontera de un sistema** (`SE-001`): punto de intercambio de información, control o responsabilidad, que puede ser entre un equipo y un proveedor tanto como entre dos programas.
- **En la descomposición** (`SE-049`): el contrato entre subproblemas.
- **En módulos** (`SE-068`): el comportamiento público esperado por los consumidores, distinto de los nombres internos.
- **En integración** (`SE-423`): el punto en que un componente expone o consume datos de otro (una respuesta JSON, una tabla compartida, una cola).

## Por qué importa

Una interfaz fija qué puede asumir cada parte de la otra, y por eso concentra los defectos de integración. `SE-423` lo dice así: cada componente asume algo sobre la otra parte (nombres, tipos, valores posibles, orden, cuántos elementos aparecen por página), y un defecto de integración es una asunción que ya no se cumple; ninguna prueba de una sola parte lo ve, porque cada una se comprueba contra su propia versión de la asunción.

## Cómo funciona

El mecanismo es separar lo **público** de lo **interno**. `SE-068` lo ilustra con módulos de Python: los consumidores importan nombres internos y se rompen al refactorizar porque no hay una interfaz pública declarada; la corrección es declararla (`__all__`, guion bajo) y probar sobre ella. `SE-049` la ve como contrato entre subproblemas: quien resuelve una parte solo necesita saber la interfaz de las demás. En integración (`SE-423`), la consecuencia práctica es una prueba por interfaz crítica: ejecutar dos o más piezas reales juntas y comprobar que la asunción de una coincide con la de la otra. En la frontera de un sistema (`SE-001`), las interfaces con proveedores deben documentarse con contrato, señal de degradación, respuesta local y escalamiento.

## Ejemplo

En `SE-423`, un componente espera una respuesta con cierto orden y cantidad de elementos por página; el otro cambia la paginación. Cada una de las dos partes pasa sus pruebas aisladas, y solo una prueba de integración sobre esa interfaz muestra el defecto. En `SE-001`, un proveedor externo aparece en el mapa del sistema con su interfaz y su modo de fallo en vez de quedar como una caja sin contrato.

## Errores y confusiones comunes

- **Un fallo de extremo a extremo tarda horas en localizarse.** Solo hay recorridos completos; corrección (`SE-423`): añadir una prueba por interfaz crítica.
- **Un proveedor aparece sin interfaz ni fallo.** Se trató «externo» como «irrelevante»; corrección (`SE-001`): documentar contrato, señal de degradación, respuesta local y escalamiento.
- **Consumidores que importan nombres internos.** No hay interfaz pública declarada (`SE-068`).

## Límites y cuándo no aplica

Una interfaz describe lo que se promete, no lo que ocurre dentro: `SE-423` aclara que una prueba de integración comprueba que las asunciones coinciden, no que cada pieza sea correcta. Y la palabra cambia de alcance entre clases (de una función pública a la frontera entre equipos), de modo que al leerla hay que confirmar cuál es.
