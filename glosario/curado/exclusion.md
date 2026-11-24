# Exclusión

## Definición

En una estrategia de pruebas, una **exclusión** es la decisión explícita de no probar un componente o una clase de fallo, con razón, responsable y fecha de revisión (`SE-421`, `SE-432`).

## Por qué importa

Todo equipo deja cosas sin probar; la diferencia profesional es saberlo. `SE-421` lo resume: lo que no se prueba nadie lo sabe cuando la omisión es silenciosa. Una exclusión escrita convierte un descuido en una decisión asumida.

## Cómo funciona

El paquete de estrategia de `SE-432` incluye una lista de exclusiones con razón y **caducidad**. Una exclusión sin caducidad se convierte en una omisión; una con caducidad vence y obliga a revisarla. La estructura permite que un programa valide que cada exclusión tiene fecha.

## Ejemplo

`SE-432`: el paquete de la plataforma lista nueve componentes probados y tres exclusiones con razón y caducidad a 75 días; una de ellas es la búsqueda.

## Errores y confusiones comunes

- **Las exclusiones nunca se revisan.** Sin caducidad; fecha menor de 90 días y revisión.
- **Lo que no se prueba nadie lo sabe.** Omisión silenciosa; lista de exclusiones con razón, responsable y caducidad.

## Límites y cuándo no aplica

Una exclusión justificada no elimina el riesgo, solo lo hace visible. Excluir componentes de impacto alto exige aprobación de quien asume el riesgo.
