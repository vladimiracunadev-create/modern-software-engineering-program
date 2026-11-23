# Paso de comprobación

[↑ Glosario](../../README.md) · [← Paso ambiguo](./paso-ambiguo.md) · [Paso fijo →](./paso-fijo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Comando cuyo único propósito es demostrar que el paso anterior dejó el entorno como se esperaba.

Definición de trabajo de [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md).

## Por qué importa

La clase donde se define, [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), existe con este propósito: la clase existe para que escribas el README como el camino más corto desde «acabo de llegar» hasta «ya vi funcionar algo», y para que sepas calcular cuánta gente se pierde en ese camino según el número de pasos y qué parte del README puede comprobarse automáticamente.

## Cómo funciona

[SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el portal; no reemplazan las de la documentación de Python y de GitHub enlazadas abajo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md):

El README de la plataforma queda en 70 líneas: dos frases de descripción, un bloque de instalación con los comandos de Windows y de Linux, un bloque «Primer éxito» con `entregas penalizar --nota 80 --horas 30` y la salida esperada `64`, y una lista de cuatro enlaces (guía por tareas, referencia, explicación y cómo contribuir). La integración continua ejecuta el bloque de instalación en un entorno limpio de ambos sistemas, compara las opciones citadas con las del analizador y ejecuta el primer éxito comprobando la salida.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Quien sigue el README instala fuera del entorno** — causa: se omitió la activación y nada lo comprueba. Corrección: añadir un paso de comprobación que muestre la ruta del intérprete. ([SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de la documentación de Python y de GitHub enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se instaló ningún paquete real, no se observó a nadie instalando y el detector usa un atributo no documentado de `argparse`; las probabilidades de fallo son supuestos del autor. La siguiente clase pasa de las páginas que guían al registro de por qué el sistema es como es: las decisiones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comando](../c/comando.md), [Entorno](../e/entorno.md), [Deriva del README](../d/deriva-del-readme.md), [Entorno aislado](../e/entorno-aislado.md), [Primer éxito](./primer-exito.md), [README](../r/readme.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-207 — README, instalación y primer éxito](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

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

[↑ Glosario](../../README.md) · [← Paso ambiguo](./paso-ambiguo.md) · [Paso fijo →](./paso-fijo.md)
