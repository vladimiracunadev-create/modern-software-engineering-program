# Cobertura

## Definición

**Cobertura** designa en el programa una fracción de lo que se debía detectar o cubrir que realmente se detectó o cubrió. Tiene tres sentidos en esta serie: en SE-372 (pruebas de mutación y reglas), las mutaciones detectadas sobre las mutaciones inyectadas; en SE-559 (revisión asistida por IA), la fracción de los defectos reales que el revisor marca (en inglés *recall*); en SE-185 (estimación), la fracción de veces que un intervalo contiene el resultado real: un intervalo está calibrado si su cobertura es la anunciada. No es la cobertura de código (líneas o ramas ejecutadas).

## Por qué importa

Dice cuánto de lo que importa se está viendo. Una suite o un revisor con mucha precisión y poca cobertura es fiable cuando habla, pero calla casi siempre. Cambia cómo se interpreta una alarma o una ausencia de alarma: la ausencia solo tranquiliza si la cobertura es alta.

## Cómo funciona

SE-559 lo explica con el compromiso entre precisión y cobertura. Un revisor automático emite una puntuación de sospecha por cambio y un umbral decide cuáles se marcan. La **precisión** es la fracción de lo marcado que era un defecto real; la **cobertura** (recall), la fracción de los defectos reales que se marcaron. **Subir el umbral sube la precisión y baja la cobertura**; bajarlo hace lo contrario. No existe un umbral correcto en abstracto: depende del costo de una falsa alarma (tiempo de lectura) frente al de un defecto que pasa.

El ejemplo de la clase fija el umbral en 0,60 tras medir, en doscientos cambios etiquetados del año anterior, 58 % de precisión y 72 % de cobertura; la persona que revisa lee primero las alarmas y después el diff completo, y la aprobación nombra a quien responde. Eso muestra por qué la cobertura debe medirse: el 28 % restante son defectos que el revisor no marca y que la lectura humana debe encontrar.

En el sentido de intervalos (SE-185), la cobertura se comprueba con retrospectiva: si el intervalo del 85 % contiene el resultado real el 85 % de las veces, está calibrado; si cubre el 60 %, el intervalo es demasiado estrecho. En el sentido de mutación (SE-372), la cobertura dice qué familias de defectos ve cada regla.

## Ejemplo

De cien defectos reales en una muestra de cambios, el revisor marca 72: cobertura del 72 %. De 124 cambios que marca, 72 eran defectos y 52 falsas alarmas: precisión del 58 %. Con el mismo revisor, bajar el umbral podría subir la cobertura al 85 % a cambio de 40 alarmas falsas más. (Cifras de SE-559 completadas con una aritmética ilustrativa.)

## Errores y confusiones comunes

- **Confundir cobertura con precisión**: una dice cuántos defectos se encontraron; la otra, cuántas alarmas eran reales.
- **Confundirla con cobertura de código**: ejecutar una línea no es detectar un defecto.
- **Medir con datos que el revisor ya vio.**
- **Hablar de cobertura sin decir de qué población.**

## Límites y cuándo no aplica

La cobertura depende de la muestra de defectos etiquetados, que puede no ser representativa. Los datos de SE-559 son un escenario hipotético, construido para la clase. Una cobertura alta no sustituye la revisión humana en los cambios críticos.
