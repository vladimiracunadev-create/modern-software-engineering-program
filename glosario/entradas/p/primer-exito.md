# Primer éxito

[↑ Glosario](../../README.md) · [← Prevalencia](./prevalencia.md) · [Primera divergencia →](./primera-divergencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Resultado observable y comprobable que obtiene quien instala el proyecto por primera vez.

Definición de trabajo de [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md).

## Por qué importa

En [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), el tema «Primer éxito» importa porque un resultado observable convierte «parece que funciona» en una comprobación.

## Cómo funciona

Según [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md):

El README es lo primero que ve quien llega a un repositorio y lo único que ve quien no sigue más. Su trabajo es contestar cinco preguntas en el orden en que se formulan: qué es esto, para qué sirve, cómo lo pruebo, dónde sigo y cómo contribuyo. No tiene que contestarlas a fondo; tiene que contestarlas rápido y enlazar el fondo. Un README que intenta ser manual, referencia y registro de cambios a la vez cae en el problema de la página mixta de `SE-206`. La regla práctica es que lo que no sirve al camino hacia el primer éxito se enlaza, no se incluye, y que el README cabe en dos pantallas antes de pasar a los enlaces.

Según [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md):

El README de la plataforma queda en 70 líneas: dos frases de descripción, un bloque de instalación con los comandos de Windows y de Linux, un bloque «Primer éxito» con `entregas penalizar --nota 80 --horas 30` y la salida esperada `64`, y una lista de cuatro enlaces (guía por tareas, referencia, explicación y cómo contribuir). La integración continua ejecuta el bloque de instalación en un entorno limpio de ambos sistemas, compara las opciones citadas con las del analizador y ejecuta el primer éxito comprobando la salida. Cuando alguien renombra una opción, la comparación falla en el pull request.

## Ejemplo

Ejemplo de [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) (sección «Ejemplo profesional»):

El README de la plataforma queda en 70 líneas: dos frases de descripción, un bloque de instalación con los comandos de Windows y de Linux, un bloque «Primer éxito» con `entregas penalizar --nota 80 --horas 30` y la salida esperada `64`, y una lista de cuatro enlaces (guía por tareas, referencia, explicación y cómo contribuir). La integración continua ejecuta el bloque de instalación en un entorno limpio de ambos sistemas, compara las opciones citadas con las del analizador y ejecuta el primer éxito comprobando la salida. Cuando alguien renombra una opción, la comparación falla en el pull request.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El README tiene 500 líneas y nadie llega al final** — causa: mezcla portada, manual y referencia. Corrección: mover lo que no es camino al primer éxito a otras páginas y enlazar. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))
- **El «hola mundo» funciona y el proyecto real no** — causa: el primer éxito no ejerce una función real. Corrección: elegir un primer éxito que use la función principal con una entrada conocida. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La regla práctica es que lo que no sirve al camino hacia el primer éxito se enlaza, no se incluye, y que el README cabe en dos pantallas antes de pasar a los enlaces. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Deriva del README](../d/deriva-del-readme.md), [Entorno aislado](../e/entorno-aislado.md), [Paso de comprobación](./paso-de-comprobacion.md), [README](../r/readme.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md), [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — el primer éxito como parte de un recorrido guiado; autoridad: proyecto Diátaxis.
- [Make a README](https://www.makeareadme.com/) — estructura mínima de un README; autoridad: proyecto Make a README.
- [GitHub: acerca de los README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — cómo se muestra un README en un repositorio; autoridad: GitHub Docs.
- [Python Packaging User Guide: instalar paquetes](https://packaging.python.org/en/latest/tutorials/installing-packages/) — instalación y entornos virtuales; autoridad: Python Packaging Authority.
- [Python: `venv`](https://docs.python.org/3/library/venv.html) — creación y activación de entornos virtuales en cada sistema; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Prevalencia](./prevalencia.md) · [Primera divergencia →](./primera-divergencia.md)
