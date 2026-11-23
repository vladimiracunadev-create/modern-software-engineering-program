# Ley de Little

## Definición

La **ley de Little** afirma que, en un sistema estable, el número medio de elementos dentro del sistema es igual a la tasa media de llegadas por el tiempo medio que cada elemento pasa dentro: **L = λ · W**. Es la formulación de `SE-184`, `SE-247`, `SE-321`, `SE-396` y `SE-436`, que la aplican a tableros de trabajo, colas de peticiones y concurrencia de servicios. Es una identidad, no un modelo: no necesita suponer distribuciones de llegada, de servicio ni orden de atención.

## Por qué importa

Convierte tres números que suelen medirse por separado en una comprobación de coherencia y en una herramienta de dimensionamiento. Para un equipo, `SE-184` lo traduce en una frase práctica: plazo medio = trabajo en curso ÷ rendimiento; si el rendimiento no cambia, duplicar el trabajo en curso duplica el plazo. Para un servicio, `SE-436` muestra que se usa para saber cuántas solicitudes concurrentes hay que soportar.

## Cómo funciona

Con **L** el número medio de elementos en el sistema, **λ** la tasa media de llegadas (en régimen estable, igual a la de terminaciones) y **W** el tiempo medio de estancia, cualquiera de los tres se despeja de los otros dos. Dos usos que las clases desarrollan:

1. **Comprobar una medición.** Si un panel dice 50 solicitudes en vuelo, 100 por segundo y 300 ms de latencia media, la ley exige 100 × 0,3 = 30; como 50 ≠ 30, alguno de los tres números mide otra cosa (`SE-436`).
2. **Dimensionar.** Un servicio de 200 solicitudes por segundo con 500 ms de estancia media necesita soportar 200 × 0,5 = 100 solicitudes concurrentes (`SE-436`).

Vale sin más supuestos porque no depende de la distribución de llegadas, de la del servicio ni de la disciplina de la cola (`SE-436`). Su condición es que el sistema esté en **régimen estable** y que las definiciones de «dentro» sean coherentes (`SE-184`).

## Ejemplo

En el tablero de trabajo de `SE-184`, con un límite de trabajo en curso igual al número de personas, el rendimiento llega a unos 3 elementos por día y no crece más, mientras que el plazo crece linealmente y coincide con n ÷ rendimiento, como predice la ley. La clase usa esa relación para proponer un límite de trabajo en curso para el tablero del equipo, con la observación que lo cambiaría. Los números son de una simulación con datos sintéticos.

## Errores y confusiones comunes

- **No cuadra con el tablero.** Elementos abandonados o fechas de inicio inconsistentes rompen la igualdad. Corrección (`SE-184`): definir qué entra, qué sale y qué fecha cuenta, y recalcular.
- **El plazo crece sin que baje el rendimiento.** Es el trabajo en curso el que crece; aplicar la ley y fijar un límite.
- **Creer que la ley predice la espera por sí sola.** Relaciona promedios; no dice cómo se distribuye la espera ni cómo crece cerca de la saturación, cosa que `SE-184` trata aparte con utilización y variabilidad.

## Límites y cuándo no aplica

Little advirtió que la ley exige un sistema en régimen estable y definiciones coherentes de qué es «dentro» (`SE-184`). No describe lo que ocurre durante picos transitorios, ni da percentiles: dos sistemas con el mismo L, λ y W pueden tener colas de latencia muy distintas. Tampoco dice qué hacer cuando el sistema no es estable (la cola crece sin límite): ahí no hay promedio que relacionar.
