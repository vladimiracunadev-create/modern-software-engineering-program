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

## Cómo desarrollar una entrada

1. Busca el `slug` del concepto en [`INVENTARIO.md`](INVENTARIO.md) o en el índice.
2. Crea `glosario/curado/<slug>.md` con las secciones que quieras sustituir (las demás siguen compuestas desde las clases).
   Una entrada **desarrollada** escribe al menos Definición, Por qué importa, Cómo funciona, Ejemplo, Errores y confusiones comunes
   y Límites y cuándo no aplica. Entrada troncal larga: entre 400 y 900 palabras; entrada de apoyo: entre 150 y 350.
3. Ejecuta `python scripts/build_glossary.py` y `python scripts/validate_glossary.py`.
4. Una figura propia solo si muestra un patrón, una relación o un mecanismo que el texto no da; usa `scripts/figure_kit.py`,
   sin repetir una tabla y con texto alternativo sin corchetes.

[↑ Glosario](README.md) · [Inventario](INVENTARIO.md)
