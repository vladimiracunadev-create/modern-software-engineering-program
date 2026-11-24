# Precisión

## Definición

**Precisión** tiene dos sentidos que el programa mantiene separados:

- **Precisión de una detección** (`SE-559`, `SE-483`, `SE-324`): la fracción de lo que se marcó que era realmente un defecto o un patrón. Es el sentido principal de esta entrada.
- **Precisión numérica** (`SE-016`, `SE-281`): la cantidad de información significativa representada, por ejemplo 16, 32 o 64 bits.

No debe confundirse con la **exactitud** (cercanía al valor verdadero) ni con la **cobertura** (*recall*).

## Por qué importa

En revisión automática, la precisión decide si el equipo cree o ignora las alarmas: cuando cae, las personas aprenden a ignorarlas y la cobertura efectiva del proceso se hunde por debajo de la del revisor (`SE-559`). En cómputo, bajar la precisión numérica cambia velocidad y memoria, pero no siempre a favor.

## Cómo funciona

**Detección** (`SE-559`): un revisor emite una puntuación de sospecha por cambio y un umbral decide cuáles se marcan. Dos cantidades describen el resultado: la **precisión** (fracción de lo marcado que era un defecto real) y la **cobertura** (fracción de los defectos reales que se marcaron). Subir el umbral sube la precisión y baja la cobertura; bajarlo hace lo contrario. No existe un umbral correcto en abstracto: depende del costo de una alarma falsa (tiempo de lectura, desgaste de atención) frente al de un defecto omitido (un incidente). `SE-483` aplica lo mismo a reglas de análisis: se mide la precisión con casos etiquetados y se afina con casos negativos.

**Numérica** (`SE-281`): pasar de 64 a 32 bits reduce los bytes por valor y, con hardware que lo soporte, aumenta las operaciones por segundo. En la CPU del laboratorio, la multiplicación de 1024×1024 pasó de unos 41 ms en 64 bits a unos 19 ms en 32 bits: casi el doble. Pero una de 256×256 en 16 bits tardó unos 221 ms frente a 0,58 ms en 32 bits: NumPy no dispone de un camino optimizado para 16 bits en esa CPU.

## Ejemplo

Un revisor marca 50 cambios; 30 eran defectos reales; hay 40 defectos en total. Precisión = 30/50 = 0,6; cobertura = 30/40 = 0,75. Ilustración:

```python
precision = tp / (tp + fp)   # 30 / 50
cobertura = tp / (tp + fn)   # 30 / 40
```

## Errores y confusiones comunes

- **El revisor automático se ignora.** Causa: umbral bajo, precisión baja, fatiga; corrección: medir con cambios etiquetados y subir el umbral (`SE-559`).
- **Las reglas se desactivan.** Causa: muchas falsas alarmas; corrección: medir precisión y afinar con casos negativos (`SE-483`).
- **Creer que menos bits siempre es más rápido.** «La precisión baja es una ventaja del hardware y de la biblioteca, no del tipo de dato» (`SE-281`).

## Límites y cuándo no aplica

Optimizar la precisión sola lleva a marcar casi nada; hay que leerla junto con la cobertura. Las cifras de `SE-281` son de una CPU y una biblioteca concretas. Y con clases muy desbalanceadas (defectos raros), una precisión aparentemente alta puede ocultar una cobertura pobre.
