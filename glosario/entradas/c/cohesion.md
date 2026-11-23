# Cohesión

[↑ Glosario](../../README.md) · [← Coeficiente de variación](./coeficiente-de-variacion.md) · [Cola de cartas muertas →](./cola-de-cartas-muertas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

La **cohesión** es el grado en que los elementos de un módulo cambian juntos y se entienden juntos ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)). Para una clase, [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) la expresa como el grado en que lo que hace la clase tiene un propósito común, y [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) la reduce a una medida: la fracción de pares de métodos que comparten estado. Las tres versiones son la misma idea con distinto nivel de precisión. El programa la usa como propiedad **observable** (cuántos lugares hay que tocar cuando una decisión cambia), no como un adjetivo de estilo como «limpio».

## Por qué importa

Una clase con poca cohesión cambia por varias razones a la vez: modificar la plantilla de un aviso obliga a releer el cálculo del costo. [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) corrige el error de tratarla como una opinión: es una propiedad que se mide, de forma parcial y con límites conocidos. Esa medida permite discutir un diseño con datos y decidir qué separar antes de que el costo del cambio lo imponga.

## Cómo funciona

Un módulo es cohesivo cuando sus partes cambian juntas y se entienden juntas. En una clase, una forma operativa de mirarlo ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)) es ver qué métodos comparten atributos o se llaman entre sí: si forman un solo grupo conectado, la clase cuenta una sola historia; si forman varios, son varias clases con un nombre común. **LCOM4** cuenta esos grupos conectados. [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) y [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) usan una aproximación hermana: para cada par de métodos, ¿comparten algún atributo de la instancia?

La cohesión no pide clases pequeñas: pide que lo que se agrupa tenga un motivo común de cambio ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)). Y se contrapesa con el acoplamiento: bajar uno sin mirar el otro desplaza el problema ([SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) los presenta como criterios que tiran en direcciones opuestas).

## Ejemplo

En el experimento de [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), la clase `Servicio` tiene 10 métodos y 8 dependencias, y 37 de los 45 pares de métodos no comparten ningún atributo: es el síntoma clásico de baja cohesión. Al separar el servicio en tres clases pequeñas, la barra de pares sin estado compartido desaparece. En [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), una clase `Envio` con siete métodos se separa en `Precio`, `Aviso` y `Bitacora`, y se comprueba con LCOM4 de cada clase y con los sitios que hay que editar para el cambio previsto. Las clases y los números son sintéticos.

## Errores y confusiones comunes

- **Confiar solo en la métrica.** Un atributo común (`self.datos`) puede conectar todo y dar LCOM4 = 1 en una clase que sigue siendo un cajón de sastre; hay que revisar los motivos de cambio ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).
- **Mover código sin separar decisiones.** Se mueve a otro archivo y no mejora nada porque se separó la ubicación, no la decisión; la pregunta es qué cambio se volvió local ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).
- **Equiparar cohesión con tamaño.** Una clase de dos métodos que no se tocan es pequeña y tiene LCOM4 = 2 ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).

## Límites y cuándo no aplica

«No comparten atributos» es una aproximación a la falta de cohesión: dos métodos pueden estar cohesionados por el dominio sin tocar el mismo atributo, y un atributo compartido puede ser accidental ([SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md)). LCOM4 no distingue una clase con tres responsabilidades de una con tres métodos sencillos que simplemente no comparten atributos, y sube o baja con la densidad de uso de los atributos ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)). La medida orienta la conversación; la decisión se toma mirando un cambio probable y su costo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Módulo](../m/modulo.md), [Acoplamiento](../a/acoplamiento.md), [Ciclo de dependencias](./ciclo-de-dependencias.md), [Controlador](./controlador.md), [Creador](./creador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Therac-25](../../../casos/fallo/therac-25.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «aproximada».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stevens, Myers y Constantine, «Structured design» (IBM Systems Journal, 1974)](https://doi.org/10.1147/sj.132.0115) — cohesión y acoplamiento; autoridad: IBM Systems Journal.
- [Chidamber y Kemerer, «A metrics suite for object oriented design» (IEEE TSE, 1994)](https://doi.org/10.1109/32.295895) — métricas de cohesión y acoplamiento; autoridad: IEEE Transactions on Software Engineering.
- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — descomposición por decisiones ocultas; autoridad: Communications of the ACM.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis del árbol sintáctico usado para medir; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Coeficiente de variación](./coeficiente-de-variacion.md) · [Cola de cartas muertas →](./cola-de-cartas-muertas.md)
