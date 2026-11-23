# Rojo

[↑ Glosario](../../README.md) · [← RMA](./rma.md) · [Rojo y verde →](./rojo-y-verde.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Estado en que una prueba nueva falla por la razón esperada.

Definición de trabajo de [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md).

## Por qué importa

En [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), el tema «Rojo por la razón correcta» importa porque una prueba que falla por un error de sintaxis no demuestra nada.

## Cómo funciona

Según [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md):

**Diagnóstico paso a paso.** (1) La prueba nunca vio un rojo, así que no hay evidencia de que detecte algo. (2) Se siembra el mutante «silencia a la persona en todos los cursos»: sobrevive. (3) La causa es que ningún ejemplo tenía dos cursos para una persona. (4) Se añade el escenario a la lista.

## Ejemplo

Ejemplo de [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) (sección «Ejemplo mínimo»):

Con una función que devuelve siempre `[]`, la prueba pasa de inmediato: es un caso del que no se puede extraer nada, y el ciclo lo reconoce porque no hubo rojo. La segunda prueba es la que hace falta: «a las 72 horas hay aviso». Falla con la función vacía, con el mensaje `assert [] == [('a', 72)]`, y esa es la razón correcta. La versión mínima que la pasa es el bucle de la versión 1.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Diagnóstico paso a paso.** (1) La prueba nunca vio un rojo, así que no hay evidencia de que detecte algo. ([SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Lista de escenarios](../l/lista-de-escenarios.md), [Prueba que pasa de inmediato](../p/prueba-que-pasa-de-inmediato.md), [Refactor](./refactor.md), [Triangulación](../t/triangulacion.md), [Verde](../v/verde.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (80 clases más lo mencionan; las que más):

[SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← RMA](./rma.md) · [Rojo y verde →](./rojo-y-verde.md)
