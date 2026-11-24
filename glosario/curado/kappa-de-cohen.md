# Kappa de Cohen

## Definición

El **kappa de Cohen** (κ) es un estadístico que mide el acuerdo entre dos evaluadores que clasifican los mismos elementos, descontando el acuerdo que se esperaría por puro azar. El programa lo usa en SE-180 (clasificación de solicitudes de cambio), SE-500 (severidad de incidentes) y SE-517 (clasificación de cambios de mantenimiento).

## Por qué importa

El porcentaje de coincidencias crudo engaña: si el 90 % de los incidentes son de severidad baja, dos personas que pusieran «baja» siempre coincidirían el 90 % de las veces sin mirar nada. El kappa descuenta ese acuerdo de fondo y responde la pregunta útil: ¿el criterio de clasificación produce acuerdo por encima del azar? Cambia la decisión de si un criterio (por ejemplo, una escala de severidad) está lo bastante claro como para usarse.

## Cómo funciona

Se calcula como κ = (p₀ − pₑ) / (1 − pₑ), donde p₀ es la proporción observada de acuerdo y pₑ la proporción de acuerdo esperada por azar a partir de cómo reparte cada evaluador sus etiquetas. Un valor de 1 es acuerdo perfecto; 0, acuerdo igual al del azar; negativo, peor que el azar.

SE-500 lo usa en una simulación: genera un impacto latente para 400 incidentes, asigna una severidad verdadera con tres umbrales y hace que tres personas perciban el impacto con un error multiplicativo (σ = 0,9, 0,35 y 0,15 en escala logarítmica según el criterio sea vago, numérico o numérico con un ejemplo por nivel). Calcula el kappa entre pares, el acuerdo con la severidad verdadera y los errores de dos o más niveles. El mecanismo que muestra: un criterio más preciso reduce el ruido de percepción y sube el kappa.

SE-517 aporta la lectura de un kappa bajo: «ajustar el cálculo del promedio» puede ser corrección, mejora o adaptación, y el texto no decide, sino la intención y el contexto. El desacuerdo no es un defecto del procedimiento sino información: las solicitudes en las que dos revisoras discrepan son las que necesitan una conversación con quien pidió el cambio.

## Ejemplo

Dos personas clasifican diez incidentes como leve o grave. Coinciden en 8 (p₀ = 0,8). Si cada una puso «leve» en 7 de 10, el acuerdo esperado por azar es 0,7 × 0,7 + 0,3 × 0,3 = 0,58. Entonces κ = (0,8 − 0,58) / (1 − 0,58) ≈ 0,52: un acuerdo moderado, bastante menos impresionante que el 80 % crudo. (Cálculo propio de ilustración; SE-500 propone un ejercicio similar con predicción previa.)

## Errores y confusiones comunes

- **Reportar solo el porcentaje de acuerdo.**
- **Interpretar umbrales como reglas universales**: las escalas habituales de interpretación son convenciones, no leyes.
- **Usarlo con más de dos evaluadores o categorías ordenadas sin adaptar**: hay variantes (kappa ponderado, kappa de Fleiss).
- **Ignorar la prevalencia**: con categorías muy desbalanceadas el kappa puede ser bajo aun con alto acuerdo.

## Límites y cuándo no aplica

El kappa mide acuerdo, no corrección: dos personas pueden coincidir en un error. Depende de la distribución de las categorías, y con muestras pequeñas es inestable. En SE-500 los datos son simulados, de modo que muestran el mecanismo, no valores esperables en un equipo real. Para clasificaciones ordinales (severidad), un kappa ponderado respeta que «por dos niveles» es peor que «por uno».
