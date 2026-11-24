# Normalización

## Definición

**Normalización** es la transformación de datos hacia una forma canónica (`SE-066`). El programa la usa con dos sentidos distintos:

- **Normalización de texto Unicode** (`SE-015`): conversión a una forma definida (NFC, NFD…) para que cadenas que se ven iguales comparen iguales.
- **Normalización de datos relacionales** (`SE-160`): organización de los datos de modo que cada hecho se guarde en un único lugar.

Ambos persiguen una sola representación por cosa, pero operan en dominios distintos.

## Por qué importa

Sin normalizar, dos representaciones del mismo valor se tratan como distintas: búsquedas que fallan, duplicados, actualizaciones inconsistentes. `SE-015` lo muestra con texto; `SE-160` con tablas, donde repetir un hecho en varios lugares permite que se contradigan.

## Cómo funciona

**Texto** (`SE-015`): `"José"` compuesto y `"José"` (la `e` más un acento combinante) son canónicamente equivalentes; tras NFC comparan iguales. Pero la normalización resuelve solo una parte: `ß` en mayúsculas es `SS`, con lo que `len` cambia; para comparar sin distinguir mayúsculas conviene `casefold()` y no `lower()`; algunos pliegues dependen del idioma (la «i» turca), y ninguna función universal los resuelve sin contexto.

**Datos** (`SE-160`): se reorganizan las tablas para que cada hecho viva en un lugar: un dato de curso se guarda una vez y las entregas lo referencian, en lugar de repetirlo en cada fila.

## Ejemplo

```python
import unicodedata
a, b = "José", "José"
a == b                                     # False
unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b)   # True
```

`SE-015` corre ese fallo controlado: como claves de un diccionario, las dos cadenas se tratan como distintas y una búsqueda falla. Corrección: normalizar con NFC al entrar, comparar con la misma forma y documentar qué campos se normalizan.

## Errores y confusiones comunes

- **Normalización universal.** Causa: no considerar el dominio; corrección: elegir forma y campos con criterio explícito (`SE-015`).
- **Creer que NFC unifica caracteres parecidos.** No unifica la `a` latina (U+0061) con la `а` cirílica (U+0430): eso exige una política de repertorio permitido, no de normalización (`SE-015`).
- **Confundir los dos sentidos.** Normalizar texto no es normalizar tablas.

## Límites y cuándo no aplica

La normalización de texto no impide la suplantación visual (un nombre de usuario o un dominio puede suplantar a otro sin que una persona lo note). Normalizar tablas al máximo puede costar rendimiento en consultas que unen muchas tablas; a veces se desnormaliza con criterio. Y normalizar es una decisión por campo: aplicarla a contraseñas, identificadores o datos que deben conservarse tal cual puede ser incorrecto.
