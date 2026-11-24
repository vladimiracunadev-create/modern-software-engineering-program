# Bloom filter

## Definición

Un **filtro de Bloom** (*Bloom filter*) es una estructura probabilística que responde a «¿está este elemento en el conjunto?» con solo dos respuestas posibles: **«posiblemente presente»** o **«definitivamente ausente»**. En `SE-093` se describe como un arreglo de bits donde cada elemento marca varios bits mediante varias funciones hash. Admite **falsos positivos** (dice «posiblemente» de algo que nunca se insertó) pero, bajo operación correcta y sin borrado, no admite **falsos negativos**. A cambio ocupa mucha menos memoria que guardar los elementos.

## Por qué importa

Hay consultas caras (leer del disco, llamar a otro servicio) cuya respuesta es «no» casi siempre. Un filtro pequeño en memoria permite responder «no» sin pagar esa consulta. La decisión profesional que cambia es aceptar un error acotado a cambio de memoria y velocidad: se pierde exactitud en un sentido (falsos positivos) y se conserva en el otro. Esa asimetría es lo que lo hace útil: un «no» es fiable, y un «sí» solo obliga a confirmar con la fuente de verdad.

## Cómo funciona

El filtro tiene `m` bits en cero y `k` funciones hash.

- **Insertar:** se calculan `k` posiciones del elemento y se ponen esos bits en 1.
- **Consultar:** si alguno de los `k` bits está en 0, el elemento **seguro no** se insertó; si todos están en 1, puede que sí, o que otros elementos hayan marcado esas mismas posiciones.

Por eso no hay falsos negativos: insertar solo enciende bits, y un elemento insertado dejó todos los suyos encendidos. Los falsos positivos aparecen por colisiones, y su tasa crece con el número de elementos `n` respecto a `m`. Con parámetros bien elegidos la tasa esperada se aproxima por `(1 - e^(-kn/m))^k`, y existe un `k` óptimo cercano a `(m/n)·ln 2`. Por eso `SE-093` insiste en que tamaño, hashes y tasa esperada **se calculan para la carga**; no se eligen por intuición. Un filtro estándar no permite borrar: apagar un bit podría ocultar a otro elemento y crearía falsos negativos.

## Ejemplo

Un servicio consulta un almacenamiento lento para saber si una clave existe. Antepone un filtro con las claves conocidas: si responde «ausente», devuelve «no existe» sin tocar el disco; si responde «posiblemente», consulta el disco, que decide. Una prueba mínima (ilustración) mide el error con elementos que sabemos ausentes:

```python
ausentes = [f"x{i}" for i in range(10_000)]
falsos = sum(1 for a in ausentes if a in filtro)
print(falsos / len(ausentes))  # tasa observada de falsos positivos
```

En `SE-093`, el síntoma «el filtro reporta *posiblemente* demasiado a menudo» tiene como causa pocos bits por elemento o demasiadas inserciones, y la corrección es dimensionar `m` y `k` según el error objetivo y verificarlo con ausentes.

## Errores y confusiones comunes

- **Creer que garantiza presencia.** «Posiblemente presente» no es «presente»; siempre hay que confirmar donde importa.
- **Esperar que permita borrar.** Sin variantes especiales (por ejemplo, con contadores), borrar un elemento no es seguro y crearía falsos negativos.
- **No medir la tasa real.** Con más inserciones de las previstas, la tasa se degrada sin aviso.
- **Confundirlo con un índice.** Un índice devuelve dónde está el dato; el filtro solo dice si puede estar.

## Límites y cuándo no aplica

Una garantía teórica no predice constantes, asignaciones ni la distribución real de las claves (`SE-093`); hay que medir con datos del uso. No sirve cuando se necesita recuperar los elementos o contarlos, ni cuando el conjunto es lo bastante pequeño para guardarlo exacto sin problema de memoria. Si cada falso positivo es costoso o peligroso, la estructura no es la adecuada.
