# Invariante

[↑ Glosario](../../README.md) · [← Invalidación](./invalidacion.md) · [Invariante de bucle →](./invariante-de-bucle.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Un **invariante** es una propiedad que permanece verdadera en puntos definidos de un proceso, de la vida de un objeto o de un modelo. El programa lo usa en cuatro escalas que comparten una misma idea, la de escribir de forma comprobable qué significa «estado válido»: en un procedimiento, [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) lo define como propiedad preservada en puntos definidos; en una clase, [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) como condición que se cumple antes y después de cada operación pública; en un modelo de estados, [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) como propiedad que debe cumplirse en todos los estados alcanzables; y en un agregado de dominio, [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) como regla que debe cumplirse siempre dentro de esa unidad. En datos, [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) lo formula como afirmación verdadera siempre que no haya una operación en curso. El sentido que usa el programa es el de la frase «lo que es verdad entre operaciones», no el de una lista de comprobaciones sueltas.

## Por qué importa

Sin un invariante escrito, «estado válido» vive en la cabeza de quien programó y cada persona lo reconstruye distinto. Escribirlo concentra la definición en un solo lugar y cambia dos decisiones profesionales: dónde comprobar y a quién culpar cuando algo falla. [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) lo plantea así: un invariante bien elegido permite localizar un defecto por el primer invariante que falla, en vez de descubrir la corrupción lejos de donde ocurrió. En el producto SaaS mínimo de [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) los invariantes son lo que el producto promete mantener siempre, y por eso se pide al menos un caso de prueba por invariante más uno que no esperes.

## Cómo funciona

Un invariante se sostiene con tres argumentos que [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) pide demostrar: que se cumple al **inicializar**, que cada **paso preserva** la propiedad (si era verdadera antes del paso, lo es después) y que, al **terminar**, la propiedad junto con la condición de parada da el resultado buscado. Es el mismo razonamiento de la inducción: base, paso y conclusión.

En una clase, el mecanismo es comprobarlo en las **fronteras** de las operaciones públicas, no en medio de ellas. Dentro de una operación el estado puede estar transitoriamente roto (se actualizó un campo y falta el otro); lo que importa es que, al devolver el control, la clase vuelva a un estado válido. En la plataforma de [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) un método `inv()` se llama al terminar cada operación, y las pruebas con un conductor aleatorio ejecutan secuencias válidas hasta que algún invariante salta.

En un modelo de estados, [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) explora todos los estados alcanzables con una búsqueda y comprueba el invariante en cada uno; si se rompe, entrega la traza más corta que lo produce. En un agregado de dominio ([SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md)), el invariante es la razón de existir del agregado: dos comandos que leen el mismo estado y escriben después pueden violarlo si no hay control, por lo que el tamaño del agregado es una decisión de concurrencia. En datos ([SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md)), la pregunta es quién vigila el invariante: el motor mediante restricciones o la aplicación, y cuántos datos inválidos deja pasar cada capa.

## Ejemplo

En [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), una calificación tiene tres invariantes: la nota está entre 0 y el máximo, una calificación publicada tiene nota y la prórroga no supera 72 horas. Cada operación pública de `Calificacion` termina llamando a `inv()`. Si `publicar()` se ejecuta sobre una calificación sin nota, el invariante «publicada implica nota» falla en esa misma operación y la traza apunta a `publicar()`, no a un informe semanas después.

En [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), un invariante de agregado: «una entrega admite como máximo tres reenvíos». Si dos comandos de reenvío leen que hay dos reenvíos y ambos escriben, el invariante se rompe aunque cada comando, por separado, fuera correcto. El invariante explica por qué hace falta un control de concurrencia en el agregado.

## Errores y confusiones comunes

- **Comprobar al final o cada muchas operaciones.** El invariante falla lejos de donde se corrompió el estado y no se sabe qué operación lo rompió. Corrección según [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md): comprobar en la frontera de cada operación pública, al menos en pruebas.
- **Contrato implícito.** La función falla sin decir quién se equivocó. Corrección según [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md): escribir precondición, invariante y poscondición; la precondición obliga al llamador, la poscondición a quien implementa y el invariante a ambos entre operaciones.
- **Confiar en el diagrama.** Un diagrama de estados que parece correcto no recorre combinaciones de transiciones y deja pasar un estado ilegal. Según [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), se explora el modelo con una búsqueda y se comprueba el invariante en integración continua.
- **Confundir invariante con validación de entrada.** Validar una entrada decide si se acepta un dato; el invariante describe qué debe seguir siendo verdad sobre el estado que ya existe.

## Límites y cuándo no aplica

Un invariante solo es tan fuerte como las operaciones que lo comprueban: si una ruta de código modifica el estado sin pasar por la frontera, el invariante no la protege. Comprobar un invariante en producción cuesta tiempo, por eso [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) distingue qué contratos se mantienen en producción (nota en rango, publicada con nota) y cuáles se retiran después de las pruebas. En un modelo, la exploración exhaustiva deja de ser viable cuando el número de estados crece demasiado ([SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) lo mide con una tabla de crecimiento). Y un invariante expresa lo que la persona que lo escribió supo ver: no sustituye a las pruebas con casos que no esperaba.

## Relación con otros conceptos

- **Prerrequisito:** [Estado](../e/estado.md).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Agregado](../a/agregado.md), [Condición](../c/condicion.md), [Operación](../o/operacion.md), [Composición](../c/composicion.md), [Dominio](../d/dominio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-161 — Máquinas de estado y model checking introductorio](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (113 clases más lo mencionan; las que más):

[SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Stripe](../../../casos/exito/stripe.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Invariantes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [Meyer, «Applying design by contract» (IEEE Computer, 1992)](https://doi.org/10.1109/2.161279) — formulación del diseño por contrato; autoridad: IEEE Computer.
- [Liskov y Wing, «A behavioral notion of subtyping» (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipado conductual y reglas de sustitución; autoridad: ACM TOPLAS.
- [Hoare, «An axiomatic basis for computer programming» (CACM, 1969)](https://doi.org/10.1145/363235.363259) — tripleta precondición–instrucción–postcondición; autoridad: Communications of the ACM.
- [Eiffel: Design by Contract](https://www.eiffel.com/values/design-by-contract/) — descripción del mecanismo en el lenguaje que lo introdujo; autoridad: Eiffel Software.

---

[↑ Glosario](../../README.md) · [← Invalidación](./invalidacion.md) · [Invariante de bucle →](./invariante-de-bucle.md)
