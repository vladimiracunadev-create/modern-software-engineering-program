# PDF del programa

El programa se publica también como libros en PDF, para leer sin conexión, imprimir o
archivar. Son una **vista generada** del portal: el repositorio y GitHub Pages siguen
siendo la fuente viva, y ningún PDF se edita a mano. Cada volumen nace de
[`scripts/build_pdf.py`](../scripts/build_pdf.py), pasa por
[`scripts/verify_pdf.py`](../scripts/verify_pdf.py) y se publica como activo de un
GitHub Release con su suma SHA-256.

## Volúmenes

<!-- pdf-volumes:start -->
Edición generada el **2026-11-24** desde el commit `e6575e51` (release [`pdf-2026-11-24-e6575e51`](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/tag/pdf-2026-11-24-e6575e51)).

| Volumen | Contenido | Páginas | Tamaño | SHA-256 | Descarga |
| --- | --- | ---: | ---: | --- | --- |
| **Libro completo** | 51 partes · 612 clases · 47 guías de rol · 32 casos · glosario | 13.029 | 185.0 MB | `53468b686ae570ab…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_libro-completo.pdf) |
| **Etapa A · Fundamentos de la profesión** | 5 partes · 60 clases | 631 | 17.5 MB | `50af9e748755d347…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-a-fundamentos.pdf) |
| **Etapa B · Programación y construcción** | 5 partes · 60 clases | 669 | 19.5 MB | `d239fa92d7645c53…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-b-programacion.pdf) |
| **Etapa C · Producto. requisitos y especificación** | 8 partes · 96 clases | 1.180 | 34.3 MB | `6fcbaaaca5ca3712…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-c-producto.pdf) |
| **Etapa D · Superficies y formas de software** | 7 partes · 84 clases | 1.077 | 31.8 MB | `4030ad88bb80320b…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-d-superficies.pdf) |
| **Etapa E · Diseño. arquitectura. datos e integración** | 10 partes · 120 clases | 1.582 | 51.4 MB | `d1d8a7c17f43a79a…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-e-arquitectura.pdf) |
| **Etapa F · Calidad. seguridad y entrega** | 6 partes · 72 clases | 964 | 27.0 MB | `b40b81c8bb6ddb59…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-f-calidad-entrega.pdf) |
| **Etapa G · Operación. evolución y liderazgo** | 4 partes · 48 clases | 660 | 17.2 MB | `e8049164be95d63f…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-g-operacion-liderazgo.pdf) |
| **Etapa H · Ingeniería de software nativa con IA** | 6 partes · 72 clases | 941 | 24.8 MB | `f17a37fed699b395…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_etapa-h-ia.pdf) |
| **Casos de estudio** | 32 casos | 960 | 27.7 MB | `bbc8a298e1bf75b4…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_casos-de-estudio.pdf) |
| **Glosario** | glosario | 3.938 | 63.6 MB | `da820bb205872bea…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_glosario.pdf) |
| **Guías de rol** | 47 guías de rol | 453 | 17.8 MB | `d86b42d81bed2909…` | [PDF](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases/latest/download/ingenieria-software-moderna_guias-de-rol.pdf) |

Sumas SHA-256 completas: [`pdf/SHA256SUMS`](../pdf/SHA256SUMS) y [`pdf/manifest.json`](../pdf/manifest.json).
<!-- pdf-volumes:end -->

Los enlaces `releases/latest/download/…` apuntan siempre a la edición más reciente; la
edición exacta de cada fila está en la página del release enlazada arriba.

### Qué contiene cada volumen

| Volumen | Para qué sirve |
| --- | --- |
| Libro completo | Las 51 partes y 612 clases (`SE-001`–`SE-612`), las 47 guías de rol, los casos de estudio y el glosario, con enlaces internos entre todo. |
| Etapas A–H | Una etapa del programa por volumen, para leer o imprimir por tramos (de 48 a 120 clases). |
| Casos de estudio | Los casos de éxito y de fallo, con sus esquemas y su vínculo con las clases. |
| Glosario | El vocabulario técnico del programa, con enlaces a las clases que usan cada término. |
| Guías de rol | Las rutas profesionales y las clases asociadas a cada rol. |

Cada volumen incluye portada con edición y commit, índice con números de página,
marcadores (volumen › etapa › parte › clase), encabezado por parte y clase, número de
página, figuras SVG vectoriales y bloques de código con ajuste de línea. Un enlace a una
clase, caso o término **del mismo volumen** salta dentro del PDF; uno a material que ese
volumen no contiene abre la página equivalente del portal.

## Comprobar una descarga

```powershell
Get-FileHash .\ingenieria-software-moderna_libro-completo.pdf -Algorithm SHA256
```

```bash
sha256sum -c SHA256SUMS --ignore-missing
```

El resultado debe coincidir con la tabla y con `pdf/SHA256SUMS` (se añade con el primer release).

## Generación reproducible

### Herramienta elegida y por qué

El PDF se imprime con **Microsoft Edge, Google Chrome o Chromium en modo sin interfaz**
(`--headless=new --print-to-pdf`), sin ningún servicio externo. Se descartó WeasyPrint
porque necesita las bibliotecas GTK/Pango, que en Windows no se instalan con `pip`
(en este repositorio falló al importar), mientras que Chromium trae lo necesario:
márgenes de página con nombre (`@page`) para encabezados y números, SVG vectorial,
control de saltos de página y enlaces internos. PyMuPDF (versión fijada) completa el
trabajo que el navegador no hace: marcadores, metadatos, idioma del documento y los
números de página del índice (segunda pasada).

### Instalación

| Sistema | Navegador | Fuentes recomendadas |
| --- | --- | --- |
| Windows | Microsoft Edge (ya instalado) o Chrome | Segoe UI, Georgia, Cascadia Mono / Consolas (incluidas) |
| Linux | `sudo apt install chromium fonts-noto-core fonts-noto-mono` (o Google Chrome) | Noto Sans, DejaVu Sans Mono |
| macOS | `brew install --cask google-chrome` | Helvetica Neue, Georgia, Menlo (incluidas) |

```powershell
python -m pip install -r pdf/requirements.txt
```

Si el navegador no está en una ruta estándar, indícala con `--browser` o con la variable
`PDF_BROWSER`.

### Generar y verificar

```powershell
python scripts/build_pdf.py --out build/pdf                      # todos los volúmenes
python scripts/build_pdf.py --volumes etapa-a,glosario --out build/pdf
python scripts/verify_pdf.py --dir build/pdf --release           # abre cada PDF y cuenta lo que lleva
python scripts/publish_pdf.py --dir build/pdf                    # registra sumas, manifiesto y esta tabla
python scripts/publish_pdf.py --dir build/pdf --create-release   # crea el Release con los activos
```

`--volumes` acepta el nombre del volumen o un prefijo (`etapa-a`, `libro`, `casos`).
`--parts 00,01` restringe a algunas partes y sirve solo para pruebas rápidas: no
produce volúmenes publicables. La carpeta `build/` no se versiona.

### Qué comprueba `verify_pdf.py`

No basta con que el build termine: el verificador abre cada PDF y lo compara con las
fuentes.

- páginas, metadatos, idioma y SHA-256 frente al manifiesto;
- partes, clases (`SE-001`–`SE-612`), casos, guías de rol y términos de glosario presentes
  y en el orden del currículo;
- figuras: una marca invisible `fig:<archivo>.svg` por figura de origen, comparada con la
  cuenta de las páginas fuente;
- texto extraído: sin código Mermaid ni vallas de código sueltas, sin caracteres de
  reemplazo, sin restos de Markdown o HTML y con toda mención `SE-nnn` enlazada (salvo
  código, rutas y texto dentro de figuras);
- enlaces internos sin romper, índice que enlaza cada unidad y marcadores que caen en la
  página que nombran;
- fuentes incrustadas y ninguna palabra fuera del margen (código o tablas cortados);
- con `--release`, que el árbol estuviera limpio al generar.

El flujo de publicación ejecuta el verificador antes de registrar nada.

## Alojamiento

Los PDF **no se guardan en git**: pesan decenas de megabytes por volumen, el repositorio
es público y el historial no se puede limpiar sin reescribirlo. Se publican como activos
de un [GitHub Release](https://github.com/vladimiracunadev-create/modern-software-engineering-program/releases)
con `SHA256SUMS`. En el repositorio solo viven el script, la hoja de estilo
([`pdf/print.css`](../pdf/print.css)), las dependencias fijadas, las sumas y el manifiesto.
Un PDF pequeño podría vivir como activo de Pages, pero se mantiene un único canal para
que ninguna copia quede desfasada.

## Límites honestos

- El PDF refleja el contenido publicado en el commit indicado en la portada; no añade
  revisión propia. El programa declara sus clases como desarrolladas «a falta de revisión
  editorial humana independiente», y los PDF heredan esa condición.
- La reproducción es **determinista en el contenido y en los metadatos** (la fecha del
  documento es la del commit), no byte a byte: los bytes dependen de la versión del
  navegador y de las fuentes instaladas. Por eso la suma que vale es la del Release.
- Los laboratorios, scripts y datos enlazados viven en el repositorio y no van dentro del
  PDF; sus enlaces apuntan a GitHub.
- El texto de las figuras SVG se incrusta como gráfico vectorial: se ve nítido y se puede
  buscar en la mayoría de los lectores, pero no siempre se selecciona como texto.
- Los PDF no son documentos etiquetados (PDF/UA): para lectura con lector de pantalla,
  el portal HTML sigue siendo la superficie accesible.
