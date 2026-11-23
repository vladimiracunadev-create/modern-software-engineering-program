# Guía editorial del glosario

[↑ Glosario](README.md) · [Inventario](INVENTARIO.md)

## Reglas

1. **No inventar.** Cada afirmación de una entrada se apoya en lo que una clase enseña o en una fuente verificada. Si un término es ambiguo, la entrada dice qué sentido usa el programa.
2. **Una entrada por concepto.** Variantes de singular y plural, siglas y expansión, y términos en español e inglés comparten entrada.
3. **Esquema único.** Las diez secciones de [la lectura de una entrada](README.md#cómo-se-lee-una-entrada), siempre en el mismo orden.
4. **Enlazar, no repetir.** La entrada resume y remite a las clases; no copia lecciones enteras.
5. **Referencias.** Escribe `SE-nnn` y `Parte NN` como texto: la publicación las enlaza.

## Dónde vive cada cosa

| Ruta | Qué contiene | ¿Se edita a mano? |
| --- | --- | --- |
| `glosario/curado/<slug>.md` | texto escrito a mano de un concepto (secciones `## Definición`, `## Por qué importa`, …) | sí |
| `glosario/entradas/<letra>/<slug>.md` | entrada publicada | no, la genera `scripts/build_glossary.py` |
| `glosario/README.md`, `INVENTARIO.md`, `indice/`, `familias/` | puntos de entrada e inventario | no |
| `glosario/casos.json` | dónde aparece cada concepto en los casos | no, `--refresh-cases` |
| `site/glosario/` | páginas del portal con búsqueda | no |

## Procedimiento para varias personas o sesiones escritoras

Varias personas pueden desarrollar entradas a la vez sin pisarse, porque cada una edita archivos distintos:

1. **Elige conceptos de un solo grupo** (una familia o una letra) y no los repitas con nadie: un concepto, un archivo `glosario/curado/<slug>.md`.
2. **Escribe** el archivo con las seis secciones obligatorias (Definición, Por qué importa, Cómo funciona, Ejemplo, Errores y confusiones comunes, Límites y cuándo no aplica). Las demás secciones se componen solas. Cita las clases como `SE-nnn` sin enlazar: la publicación las enlaza.
3. **Fundamenta cada afirmación** en lo que enseñan las clases (cítalas) o en una fuente verificada; marca como ilustración lo que no venga de ellas.
4. **Regenera** con `python scripts/build_glossary.py` y valida con `python scripts/validate_glossary.py`.
5. **Commitea solo** tus `glosario/curado/*.md` y los archivos generados que cambian (`glosario/entradas/`, `glosario/README.md`, `glosario/INVENTARIO.md`, `glosario/indice/`, `glosario/familias/`, `site/glosario/`) y, si cambian por tus conteos, `README.md`, `STATUS.md`, `FILE_INDEX.md` y `site/index.html` (los regenera `python scripts/build_phase2.py`).
6. **Antes de empujar**, `git fetch` y rebase. Ante un conflicto en un archivo generado, no lo edites: toma cualquiera de las dos versiones, vuelve a ejecutar `build_glossary.py` (y `build_phase2.py` si el conflicto fue en README, STATUS, FILE_INDEX o `site/index.html`) y añade el resultado. Los archivos `glosario/curado/` de personas distintas no entran en conflicto.
7. **Los conteos** (desarrolladas y compuestas) los calcula el generador a partir de `glosario/curado/`: no se escriben a mano en ninguna parte.

Calidad mínima exigida por `scripts/validate_glossary.py` y `tests/test_glossary.py` a cada entrada curada: las seis secciones presentes; entre 350 y 1.100 palabras en las seis secciones si el concepto es troncal (entre 110 y 800 si es de apoyo); enlaces a clases existentes; y ninguna mención `SE-nnn` o `Parte NN` sin enlazar en la entrada publicada.

## Cómo desarrollar una entrada

1. Busca el `slug` del concepto en [`INVENTARIO.md`](INVENTARIO.md) o en el índice.
2. Crea `glosario/curado/<slug>.md` con las secciones que quieras sustituir (las demás siguen compuestas desde las clases).
   Una entrada **desarrollada** escribe al menos Definición, Por qué importa, Cómo funciona, Ejemplo, Errores y confusiones comunes
   y Límites y cuándo no aplica. Entrada troncal larga: entre 400 y 900 palabras; entrada de apoyo: entre 150 y 350.
3. Ejecuta `python scripts/build_glossary.py` y `python scripts/validate_glossary.py`.
4. Una figura propia solo si muestra un patrón, una relación o un mecanismo que el texto no da; usa `scripts/figure_kit.py`,
   sin repetir una tabla y con texto alternativo sin corchetes.

[↑ Glosario](README.md) · [Inventario](INVENTARIO.md)
