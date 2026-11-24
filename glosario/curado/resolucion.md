# Resolución

## Definición

**Resolución** designa en el programa un proceso de «llegar a una respuesta concreta» con tres sentidos:

- **De dependencias** (`SE-111`): el resolvedor busca una asignación de versiones que satisfaga las restricciones, retrocede ante un conflicto y aplica reglas del ecosistema.
- **De una ambigüedad o defecto** (`SE-154`): una decisión registrada, con responsable, que elimina el defecto o acepta el riesgo.
- **De rutas** (`SE-026`): el proceso de recorrer componentes, montajes y enlaces hasta el objeto real.

## Por qué importa

En dependencias, el resultado depende del orden de índices, versiones retiradas y plataforma: la misma lista puede resolver distinto. En requisitos, no resolver significa que la decisión la tomó el código. Cambia lo que se registra: la solución elegida y, en `SE-154`, quién y por qué.

## Cómo funciona

**Dependencias** (`SE-111`): el resolvedor trata el problema como satisfacción de restricciones; puede existir más de una solución válida. Un manifiesto declara rangos; la resolución elige versiones concretas, que el archivo de bloqueo conserva para repetir la instalación (`SE-032`). Si hay conflicto, retrocede e intenta otra combinación.

**Requisitos** (`SE-154`): encontrar el defecto es la mitad; la otra mitad es decidir quién lo resuelve. Una pregunta va a quien tiene autoridad (producto para un comportamiento, privacidad para una retención), con las alternativas, sus consecuencias y una fecha. Resolver puede significar reescribir, eliminar un requisito, separar casos o aceptar el riesgo. Registrar la respuesta en el expediente evita preguntar otra vez.

**Rutas** (`SE-026`): resolver una ruta es seguir directorios, montajes y enlaces; dos rutas distintas pueden resolver al mismo objeto, y una resoluble puede estar prohibida por permisos.

## Ejemplo

```text
requisito: lib-a>=1.0, lib-b>=2.0 ; lib-b 2.0 exige lib-a<1.5
resolución: lib-a 1.4, lib-b 2.0  (única asignación compatible)
```

En requisitos: «el retraso de 30 minutos, ¿cuenta como tardío?» → decisión de producto, registrada con fecha y responsable.

## Errores y confusiones comunes

- **Un defecto reaparece tras un cambio.** Causa: la resolución no se registró o se repitió el análisis; corrección: guardar cada decisión con responsable y repetir las búsquedas tras cada cambio (`SE-154`).
- **Una actualización rompe otro proyecto.** Causa: alcance global sin control de resolución; corrección: aislar por proyecto y conservar manifiesto y bloqueo (`SE-032`).
- **Confundir resolver con descartar.** Aceptar el riesgo también es resolver, pero debe quedar escrito.

## Límites y cuándo no aplica

Un archivo de bloqueo conserva resoluciones para reproducibilidad, pero no garantiza disponibilidad futura, ausencia de vulnerabilidades ni equivalencia entre plataformas (`SE-032`). Y una resolución sin responsable ni fecha es una opinión: no cierra el defecto, solo lo oculta.
