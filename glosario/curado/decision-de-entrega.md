# Decisión de entrega

## Definición

La **decisión de entrega** es el juicio explícito, con criterios de salida comprobables y defectos conocidos, sobre si se puede construir sobre una especificación (SE-156). SE-550 usa el mismo término de otro modo, en el contexto de IA agéntica: la acción de empujar, abrir un pull request o fusionar, que se separa de la implementación y se decide aparte.

## Por qué importa

Entregar una especificación es una decisión con riesgo, no un hito de calendario. Si se entrega por la fecha, quien construye hereda defectos sin saberlo. Con una decisión explícita, queda dicho qué se sabe que falta y quién responde. Cambia el momento de la responsabilidad: el equipo que especifica declara el estado real de su trabajo.

## Cómo funciona

SE-156 pide criterios de salida **comprobables**:

- el validador de estructura no produce errores;
- las mutaciones que el validador no detecta están documentadas;
- se hicieron dos revisiones con criterios distintos;
- los defectos abiertos tienen responsable;
- el defecto estimado restante es conocido, con su incertidumbre.

La frase de la clase es que lo que se entrega **incluye lo que se sabe que falta**. Una especificación entregada no es «completa»; es suficiente para construir con el riesgo declarado. El expediente que acompaña a la entrega es el registro de revisión: encabezado, resultados de las comprobaciones, defectos abiertos y la decisión con responsable y fecha. La estimación de defectos restantes se apoya en la detección de defectos con técnicas distintas, y en lo que se sabe de la cobertura del validador (medida con mutaciones).

En el sentido de SE-550, la decisión de entrega en desarrollo con agentes es la misma idea de separar el juicio del hacer: el agente puede implementar, pero empujar, abrir un PR o fusionar son acciones que se deciden aparte, con una persona responsable y criterios de salida.

## Ejemplo

El encabezado de una especificación entregada dice: «Versión 1.0. Validador: 0 errores. Mutaciones no detectadas: 3 (documentadas). Revisiones: 2 (una de contenido, una de consistencia). Defectos abiertos: 4 (con responsable). Estimación de defectos restantes: entre 2 y 7. Decisión: construir. Responsable: producto. Fecha: …». Quien construye sabe qué riesgo hereda. (Estructura ilustrativa derivada de los criterios de SE-156.)

## Errores y confusiones comunes

- **La lectora tarda un día en entender qué falta**: el expediente no responde sin su autor; corrección: revisar contra la lista de elementos obligatorios.
- **El validador pasa y hay errores graves**: solo comprueba estructura.
- **Decidir por el calendario.**
- **Entregar sin defectos abiertos declarados**: «sin defectos» casi nunca es verdad.

## Límites y cuándo no aplica

Los criterios de salida y las estimaciones de defectos de SE-156 son supuestos del autor. Para especificaciones pequeñas o exploratorias, el expediente completo es excesivo. Una decisión explícita no elimina el riesgo; lo hace visible y asignado.
