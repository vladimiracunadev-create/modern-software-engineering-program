# Análisis estático

[↑ Glosario](../../README.md) · [← Análisis entre artefactos](./analisis-entre-artefactos.md) · [Análisis estático y límites →](./analisis-estatico-y-limites.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

El **análisis estático** es el examen del código fuente sin ejecutarlo, mediante reglas sobre su estructura, normalmente sobre su árbol sintáctico, para encontrar patrones de defecto. [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) lo define así y [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) lo reutiliza dentro del ciclo de desarrollo seguro. Se contrapone al análisis dinámico, que observa el programa mientras corre.

## Por qué importa

Decide qué defectos se descartan barato y cuáles no. Un analizador revisa cada cambio en segundos, sin datos de prueba y sin cansancio, así que es ideal para defectos *de patrón*: un parámetro por defecto mutable, una cláusula `except` sin tipo, una variable sin uso. Pero «pipeline verde» solo dice que ninguna regla vio nada, no que el código esté bien. Saber qué no ve evita delegar en él lo que corresponde a la revisión humana y a las pruebas.

## Cómo funciona

El código se convierte en un **árbol sintáctico**; una regla es una función que recorre los nodos y señala los que cumplen una condición. En Python, el módulo `ast` expone ese árbol, y [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) escribe con él reglas que buscan argumentos por defecto mutables, `except` sin tipo y variables locales sin uso.

La causa de sus límites está en que las reglas se escriben sobre la **forma**, y la forma no es la intención. De ahí dos clases de error:

- **Falsa alarma:** la regla señala algo correcto. Una lista como parámetro por defecto usada a propósito como caché; una variable que se consulta de forma dinámica con `eval`.
- **Defecto no visto:** el defecto no tiene patrón. Un recorrido que empieza en uno en lugar de cero es sintácticamente impecable y ninguna regla de forma lo detecta.

Por eso la utilidad de una regla se mide con su **precisión** (qué fracción de sus alertas son defectos reales) y su **cobertura** (qué fracción de los defectos de esa clase encuentra), y no con la cantidad de alertas.

## Ejemplo

[SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) genera 300 funciones desde plantillas con semilla fija y siembra defectos con probabilidad conocida: argumento mutable (a veces como caché intencional), `except` sin tipo (a veces seguido de `raise`), variable sin uso (a veces usada con `eval` o con prefijo de guion bajo) y un recorrido que omite el primer elemento. Todas las funciones compilan. Tres reglas con `ast` buscan los tres primeros defectos y la cuarta no tiene regla. El resultado ilustra la tesis: las reglas encuentran lo que tiene forma, producen alguna falsa alarma en los casos intencionales, y el defecto lógico pasa intacto.

```python
import ast

def parametros_mutables(codigo):
    for nodo in ast.walk(ast.parse(codigo)):
        if isinstance(nodo, ast.FunctionDef):
            for d in nodo.args.defaults:
                if isinstance(d, (ast.List, ast.Dict, ast.Set)):
                    yield nodo.name, nodo.lineno
```

## Errores y confusiones comunes

- **El pipeline está verde y el defecto llegó a producción.** La regla no ve esa clase de defecto. Corrección ([SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md)): listar lo que no ve cada comprobación y cubrirlo con revisión o pruebas.
- **Las alertas se ignoran.** Precisión baja: se mide, se afina con datos y se apartan las reglas ruidosas.
- **Confundirlo con una prueba.** No ejecuta nada, así que no demuestra comportamiento.
- **Tratar cero alertas como ausencia de defectos.** Solo hay ausencia de *esos patrones*.

## Límites y cuándo no aplica

[SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) trabaja con datos sintéticos, sin ninguna herramienta comercial ni revisión humana medidas, y las reglas se afinaron con los mismos casos que las evalúan, de modo que sus cifras ilustran el mecanismo, no el rendimiento de un analizador real. No sirve para defectos de lógica, de requisitos o de integración; para eso están las pruebas, la revisión y la observación en ejecución. En seguridad ([SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md)) complementa, no reemplaza, las pruebas negativas y el modelado de abuso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](./arbol.md), [Estructura](../e/estructura.md), [Regla](../r/regla.md), [Sobre](../s/sobre.md), [Caso de abuso](../c/caso-de-abuso.md), [Cobertura del cambio](../c/cobertura-del-cambio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-434 — Revisión, análisis estático y quality gates](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sadowski et al., «Lessons from building static analysis tools at Google»](https://doi.org/10.1145/3188720) — adopción de análisis estático y falsas alarmas; autoridad: Communications of the ACM, 2018.
- [Python: ast](https://docs.python.org/3/library/ast.html) — árbol sintáctico usado en las reglas; autoridad: documentación de Python.
- [Bacchelli y Bird, «Expectations, outcomes, and challenges of modern code review»](https://doi.org/10.1109/ICSE.2013.6606617) — qué aporta la revisión; autoridad: ICSE 2013.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — límites de la cobertura; autoridad: ICSE 2014.
- [SonarQube: quality gates](https://docs.sonarsource.com/sonarqube/latest/user-guide/quality-gates/) — ejemplo de compuerta sobre código nuevo; autoridad: documentación del producto.

---

[↑ Glosario](../../README.md) · [← Análisis entre artefactos](./analisis-entre-artefactos.md) · [Análisis estático y límites →](./analisis-estatico-y-limites.md)
