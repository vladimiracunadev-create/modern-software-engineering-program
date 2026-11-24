# Criterio de abandono

## Definición

Un **criterio de abandono** es una condición medible, fijada de antemano, que obliga a detener una iniciativa (`SE-526`).

## Por qué importa

Una reescritura sin forma de pararla se convierte en compromiso irreversible por inercia. `SE-526` propone que la conclusión de un análisis no sea «reescribir» ni «evolucionar» sino una **opción con salida**: se decide con indicadores, y se acuerda de antemano cuándo se corta.

## Cómo funciona

Si se elige reescribir, se hace de forma incremental (`SE-521`) para que cada rebanada entregue valor y pueda detenerse; se fijan criterios de abandono, como el porcentaje de alcance cubierto o la desviación acumulada del presupuesto; y se define quién tiene autoridad para parar, sin que parar se considere un fracaso personal. Si se elige evolucionar, se fijan indicadores (costo por cambio, tiempo de ciclo, incidencias) que revisan la decisión si no mejoran en un plazo.

## Ejemplo

`SE-526` (escenario hipotético): el equipo convierte las propuestas en parámetros. Del historial de la empresa obtiene que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto; mide el crecimiento del costo del módulo (9 % anual) y la deriva por peticiones al módulo antiguo; ejecuta una simulación con análisis de sensibilidad. Un criterio sería, por ejemplo, abandonar si el gasto acumulado excede una proporción fijada del presupuesto antes de cubrir cierto alcance.

## Errores y confusiones comunes

**No hay forma de parar la reescritura.** Sin criterios de abandono ni dueño; fijar criterios y quién puede aplicarlos.

## Límites y cuándo no aplica

Un criterio solo sirve si se mide con datos reales y alguien con autoridad lo aplica. Cifras como las de la clase son del escenario, no valores universales.
