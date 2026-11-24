# Procedimientos de verificación

[↑ Glosario](../../README.md) · [← Procedimiento y contrato](./procedimiento-y-contrato.md) · [Proceso →](./proceso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Un **procedimiento de verificación** es la descripción de qué se ejecuta, con qué datos, en qué entorno, cuántas veces y cómo se decide ([SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)). Convierte un criterio («responde rápido») en una medición con método y variación conocidos.

## Por qué importa

Un criterio sin procedimiento no se puede comprobar de forma repetible: dos personas medirían de modo distinto y obtendrían resultados distintos. Cambia la redacción del requisito: junto al criterio va el procedimiento que lo comprobará.

## Cómo funciona

[SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) enumera los elementos: **qué se ejecuta** (la operación medida), **con qué datos** (un conjunto representativo), **en qué entorno** (hardware, carga de fondo), **cuántas veces** y **cómo se decide** (el umbral y la regla). Una medición de percentil tiene **variación entre corridas**: el mismo procedimiento da valores distintos cada vez. Por eso la decisión debe indicar cuánta **tolerancia** acepta y cuántas **repeticiones** hacen falta.

La clase aclara que un procedimiento **no es necesariamente una prueba automatizada**. Puede ser una inspección con criterios, una prueba con personas con una tarea y un umbral, o una revisión de un artefacto por una lista. Lo que lo define es que alguien más pueda ejecutarlo y llegar a la misma decisión.

El procedimiento se conecta con los patrones de reparación: tras cuantificar y acotar un requisito, se escribe cómo se medirá. La reparación de un requisito en el ejemplo de la clase viene con su procedimiento y con la decisión sobre lo que no se repara. Dos riesgos: una cifra sin origen (se registra la necesidad o medición de la que proviene) y una prueba que pasa mientras las personas se quejan, porque mide un proxy (se valida con personas el umbral).

## Ejemplo

Criterio: «el 95 % de las peticiones de listado responde en 1.500 ms o menos con 200 usuarios concurrentes». Procedimiento: ejecutar el listado con 200 clientes simulados durante 5 minutos sobre el conjunto de datos de referencia en el entorno de pruebas, repetir 5 veces, calcular el percentil 95 de cada corrida; se acepta si el máximo de las 5 corridas es ≤ 1.500 ms y se investiga si la variación entre corridas supera el 10 %. (Procedimiento ilustrativo según los elementos de [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).)

## Errores y confusiones comunes

- **Una sola corrida** para decidir sobre un percentil.
- **Entorno distinto al declarado.**
- **Prueba que pasa y la gente se queja**: el proxy no refleja la necesidad.
- **Procedimiento imposible de repetir** por falta de datos o entorno descritos.

## Límites y cuándo no aplica

Un procedimiento detallado no garantiza que el criterio sea el correcto. Para requisitos sencillos y de bajo riesgo, una comprobación informal basta. El costo de ejecutar el procedimiento (tiempo, entornos) puede limitar cuántas veces se hace.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Patrones de reparación](./patrones-de-reparacion.md), [Reformulación](../r/reformulacion.md), [Requisitos universales y negativos](../r/requisitos-universales-y-negativos.md), [Verificabilidad](../v/verificabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — características de un buen requisito, entre ellas ser verificable; autoridad: ISO, IEC e IEEE.
- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de redacción; autoridad: IEEE International Requirements Engineering Conference.
- [Hanley y Lippman-Hand: If nothing goes wrong, is everything all right? (1983)](https://doi.org/10.1001/jama.1983.03330370053031) — regla de tres para cero fallos; autoridad: JAMA.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — objetivos con percentil, ventana y medición; autoridad: Google.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — verificación y validación de requisitos; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Procedimiento y contrato](./procedimiento-y-contrato.md) · [Proceso →](./proceso.md)
