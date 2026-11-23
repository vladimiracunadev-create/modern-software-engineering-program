# Guía de casos de estudio

Esta guía fija el esquema único y las reglas editoriales de la superficie **Casos de estudio**: la
realidad frente a la teoría del curso. Léela completa antes de escribir o revisar un caso. Complementa
el [estándar pedagógico](../docs/PEDAGOGICAL-STANDARD.md) y la
[guía de rediseño de figuras](../docs/FIGURE-REDESIGN-GUIDE.md).

## Qué es y qué no es

- Es una superficie propia, como los talleres o simuladores de otros programas: dos páginas especiales
  ([éxito](exito/README.md) y [fallo](fallo/README.md)) y un archivo por caso.
- **No** son clases, **no** son roles, **no** crean partes y **no** cambian los contadores de
  612 clases y 51 partes. No se escribe ningún ADR de ampliación de clases por ellos.
- Se leen **después** de la teoría. Cada caso enlaza las clases reales (`SE-nnn`) que explican lo que
  muestra; no las sustituye.

## Los 16 casos (lista fija)

La lista vive en [`scripts/cases_data.py`](../scripts/cases_data.py) y no se cambia sin decisión explícita.

- Éxito: `netflix`, `whatsapp`, `uber`, `mercado-libre`, `amazon`, `spotify`, `airbnb`, `stripe`.
- Fallo: `knight-capital`, `healthcare-gov`, `tsb`, `meta-2021`, `crowdstrike`, `therac-25`, `gitlab-2017`, `quibi`.

Cada caso vive en `casos/<exito|fallo>/<slug>.md`. Mientras otra sesión lo escribe, el archivo es un
esqueleto con la marca `<!-- case:status=skeleton -->` y una nota «en elaboración». **Quien escribe un caso
sustituye el archivo completo y elimina esa marca**: a partir de ese momento los validadores exigen el
esquema completo.

## Esquema único de un caso

Un caso terminado tiene exactamente estas secciones `##`, en este orden (los validadores comprueban el
prefijo del título). Las marcadas «solo fallo» van únicamente en `casos/fallo/`.

| Orden | Encabezado `##` | Qué debe contener |
| ---: | --- | --- |
| 1 | `Ficha histórica` | nombre, fundadores u organización, año, sede, hitos con año, tamaño, estado actual |
| 2 | `Contexto y problema` | el mundo anterior, el problema que nadie resolvía bien y la apuesta |
| 3 | `Mercado, usuarios y casos de uso` | segmentos, tipos de usuario, trabajos que contratan al sistema |
| 4 | `Funcionalidad de principio a fin` | por cada instancia (tipo de usuario o flujo): de la primera interacción a la operación diaria |
| 5 | `Negocio y economía` | modelo de ingresos, estructura de costes, palancas y límites, con cifras fechadas y fuente |
| 6 | `Arquitectura y esquemas` | contexto, componentes, flujo crítico, datos y escala, cada uno con figura propia |
| 7 | `Casos especiales y cómo se resuelven` (en fallo: `Casos especiales y cómo fallan`) | bordes, picos, errores, regulación, recuperación |
| 8 | `Línea de tiempo` | hechos con año o fecha y fuente, separados de la interpretación |
| 9 | `Qué falló en cada instancia` | solo fallo: instancia por instancia, qué se esperaba y qué ocurrió |
| 10 | `Causa raíz y factores` | solo fallo: detonante, condiciones latentes y factores de contexto, sin buscar culpables |
| 11 | `Mejoras que debieron hacerse` | solo fallo: cada mejora ligada a la causa que corta y a la clase que la enseña |
| 12 | `Vínculo con el curso` | al menos cinco enlaces a clases reales `SE-nnn` y qué mecanismo muestra el caso de cada una |
| 13 | `Qué no generalizar` | condiciones propias del caso que no se transfieren |
| 14 | `Fuentes públicas verificadas` | al menos cinco enlaces `https` abiertos; qué afirma cada fuente |

## Estructura del archivo

1. Línea `# Nombre del caso` (la misma de la lista fija).
2. Línea de navegación exacta, la misma al principio y al final (después de `---`). La calcula
   `case_nav()` en `scripts/build_cases.py`: enlaza a `README.md` del grupo (`↑ Casos de éxito` o
   `↑ Casos de fallo`), al caso anterior (`← Nombre`) y al siguiente (`Nombre →`); el primero y el último
   omiten el vecino que no existe. Cópiala del esqueleto que sustituyes.
3. Un párrafo de apertura (gancho y alcance) antes de la primera sección.
4. Las secciones del esquema.
5. Línea `---` y de nuevo la navegación.

## Reglas editoriales

- **Hechos, interpretación y lecciones** se separan siempre; los hechos llevan fuente. Lo que no es
  público se declara como desconocido: no se inventa una cifra, una cita ni una intención.
- **Cifras fechadas**: toda magnitud lleva año y fuente. Si dos fuentes difieren, se muestran ambas.
- **Sin culpables**: en los fallos se analizan decisiones, incentivos y sistemas, no personas. Se nombra
  a las personas solo cuando la fuente pública las nombra por su papel en un hecho verificado.
- **Sin copiar**: nada de párrafos ni citas largas de las fuentes; como máximo una cita corta con
  atribución. Se escribe con palabras propias.
- **Casos reales, no ficticios**: no se mezclan ejemplos inventados; si se ilustra con un modelo, se rotula
  como «modelo didáctico» y se distingue del hecho.
- **Profundidad**: cada sección explica mecanismo, causa, ejemplo y límite. Un caso no se da por
  terminado por tener las secciones o un número de palabras; se revisa completo de forma cualitativa.
- **Vínculo real**: los enlaces a clases usan la ruta real, por ejemplo
  `../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-.../README.md`, y el validador
  comprueba que el archivo existe.
- **Neutralidad**: ni propaganda de la empresa ni juicio retrospectivo injusto; el caso explica por qué
  tenía sentido decidir como se decidió con la información de entonces.
- **Marcas y licencias**: no se incrustan logotipos ni capturas de pantalla protegidas; los esquemas
  son dibujos propios.

## Figuras: contrato fijo

Cada caso aporta sus figuras con el script **`scripts/figures_case_<slug>.py`**, que expone un diccionario
`FIGURES` igual que `scripts/figures_part*_a.py` (nombre de archivo → función que devuelve una `Fig`).

- El nombre de cada SVG **empieza por el slug** (`netflix-flujo-de-reproduccion.svg`) y se escribe en
  `casos/figures/`. `python scripts/build_figures.py` descubre todos los
  `scripts/figures_case_*.py`; `--check` falla si el SVG está desactualizado.
- En el caso se incrustan con la sintaxis Markdown de imagen (texto alternativo y ruta
  `../figures/<slug>-<nombre>.svg`, sin título).
- Mínimo **dos figuras** por caso terminado: contexto o ecosistema, y flujo crítico o arquitectura. Lo ideal
  son cuatro o más: contexto, componentes, flujo crítico y datos o escala.
- Usa las primitivas de [`scripts/figure_kit.py`](../scripts/figure_kit.py): `Fig.box`, `Fig.arrow`,
  `flow()` para mecanismos; `timeline`, `line_chart`, `grouped_bars` o `heatmap` para datos.
- **Ninguna figura de casos puede repetir una tabla.** El trinquete de
  `scripts/figure_tab_baseline.py` cuenta la clave `casos` con tope 0: una figura creada con `tab()`,
  un diagrama con `Fig.table()` o un `alt` que empiece por «Tabla» rompe la prueba. Si la información es
  una tabla, va en Markdown y la figura muestra otra cosa (secuencia, estructura, magnitud).
- **Texto alternativo**: describe el esquema y su conclusión; no empieza por «Tabla» y **no contiene
  corchetes**. El `desc` de la figura dice lo mismo.
- Tras cada figura, un párrafo «Cómo leer la figura» con qué representa cada elemento, qué mirar primero y
  dónde deja de valer.
- Datos numéricos de una figura: los mismos del texto, con año y fuente en el `foot` de la figura.

## Procedimiento de una sesión de caso

1. Lee esta guía, el esqueleto de tu caso y las clases a las que lo vas a vincular.
2. Reúne fuentes públicas primarias (informes oficiales, post-mortems, presentaciones técnicas, cartas a
   accionistas, documentos regulatorios) y verifica cada enlace.
3. Escribe `casos/<tipo>/<slug>.md` completo y `scripts/figures_case_<slug>.py`.
4. Genera y valida:

```bash
python scripts/build_figures.py
python scripts/build_cases.py
python scripts/validate_cases.py
python scripts/build_phase2.py --check
python scripts/validate_site.py
python -m unittest discover -s tests
npx --yes markdownlint-cli2@0.23.0 "casos/**/*.md"
```

5. Revisa los SVG a tamaño real y en ancho de móvil antes de confirmar.
6. Un commit por caso; tras el push, espera a que **Validate**, **Pages** y **Security** estén en verde.

Solo toca tu `casos/<tipo>/<slug>.md` y tu `scripts/figures_case_<slug>.py`; las páginas de grupo, el
portal y los validadores los genera el sistema.

## Qué validan los scripts

`python scripts/validate_cases.py` comprueba: que existan los 16 casos y las dos páginas de grupo; que
cada caso tenga su navegación; que los enlaces relativos existan; que el índice de cada página liste todos
los casos; y, para un caso terminado, el esquema de secciones, la longitud mínima, las figuras, el texto
alternativo sin corchetes, los enlaces a clases reales y las fuentes. `tests/test_cases.py` repite estas
comprobaciones y añade la del trinquete contra figuras que repiten una tabla.
