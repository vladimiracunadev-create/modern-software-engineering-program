# README

[↑ Glosario](../../README.md) · [← ReAct](./react.md) · [Rebanada →](./rebanada.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Documento de portada de un proyecto que dice qué es, cómo se prueba y dónde seguir, en el menor espacio útil.

Definición de trabajo de [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md).

## Por qué importa

En [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), el tema «Función del README» importa porque es la portada: decide si alguien sigue o se va, y desde dónde se deriva todo lo demás.

## Cómo funciona

Según [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md):

El README es lo primero que ve quien llega a un repositorio y lo único que ve quien no sigue más. Su trabajo es contestar cinco preguntas en el orden en que se formulan: qué es esto, para qué sirve, cómo lo pruebo, dónde sigo y cómo contribuyo. No tiene que contestarlas a fondo; tiene que contestarlas rápido y enlazar el fondo. Un README que intenta ser manual, referencia y registro de cambios a la vez cae en el problema de la página mixta de `SE-206`. La regla práctica es que lo que no sirve al camino hacia el primer éxito se enlaza, no se incluye, y que el README cabe en dos pantallas antes de pasar a los enlaces.

Según [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md):

El README de la plataforma queda en 70 líneas: dos frases de descripción, un bloque de instalación con los comandos de Windows y de Linux, un bloque «Primer éxito» con `entregas penalizar --nota 80 --horas 30` y la salida esperada `64`, y una lista de cuatro enlaces (guía por tareas, referencia, explicación y cómo contribuir). La integración continua ejecuta el bloque de instalación en un entorno limpio de ambos sistemas, compara las opciones citadas con las del analizador y ejecuta el primer éxito comprobando la salida. Cuando alguien renombra una opción, la comparación falla en el pull request.

## Ejemplo

Ejemplo de [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) (sección «Ejemplo mínimo»):

El fragmento comprueba que las opciones citadas en un README existan en un analizador. Antes de ejecutarlo, predice qué opción detecta como rota.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Quien sigue el README instala fuera del entorno** — causa: se omitió la activación y nada lo comprueba. Corrección: añadir un paso de comprobación que muestre la ruta del intérprete. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))
- **El README tiene 500 líneas y nadie llega al final** — causa: mezcla portada, manual y referencia. Corrección: mover lo que no es camino al primer éxito a otras páginas y enlazar. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))
- **El README es correcto pero los ejemplos dan otra salida** — causa: cambió el significado de una opción sin cambiar el nombre. Corrección: ejecutar los ejemplos y comparar la salida en la integración continua. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El README es lo primero que ve quien llega a un repositorio y lo único que ve quien no sigue más. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))
- La transferencia está lograda cuando puedes explicar qué parte del README depende del producto y cuál es estructura reutilizable. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Deriva del README](../d/deriva-del-readme.md), [Entorno aislado](../e/entorno-aislado.md), [Paso de comprobación](../p/paso-de-comprobacion.md), [Primer éxito](../p/primer-exito.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (452 clases más lo mencionan; las que más):

[SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Make a README](https://www.makeareadme.com/) — estructura mínima de un README; autoridad: proyecto Make a README.
- [GitHub: acerca de los README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — cómo se muestra un README en un repositorio; autoridad: GitHub Docs.
- [Python Packaging User Guide: instalar paquetes](https://packaging.python.org/en/latest/tutorials/installing-packages/) — instalación y entornos virtuales; autoridad: Python Packaging Authority.
- [Python: `venv`](https://docs.python.org/3/library/venv.html) — creación y activación de entornos virtuales en cada sistema; autoridad: documentación de Python.
- [Python: `argparse`](https://docs.python.org/3/library/argparse.html) — definición de opciones y subcomandos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← ReAct](./react.md) · [Rebanada →](./rebanada.md)
