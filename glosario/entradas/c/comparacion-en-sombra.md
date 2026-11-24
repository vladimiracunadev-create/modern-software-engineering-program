# Comparación en sombra

[↑ Glosario](../../README.md) · [← Comparación diferencial](./comparacion-diferencial.md) · [Comparación pareada →](./comparacion-pareada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

La **comparación en sombra** es la ejecución del sistema nuevo con una copia del tráfico real, sin servir su respuesta, para compararla con la del sistema antiguo. Es la definición de [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), donde aparece como paso de una migración gradual (estrangulamiento, rama por abstracción, capa anticorrupción). También se conoce como *shadowing*, tráfico en sombra o ejecución en paralelo; [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) la nombra además «lanzamiento oscuro».

## Por qué importa

Una migración se decide con pruebas, pero las pruebas solo cubren lo que alguien imaginó. El tráfico real contiene casos que nadie escribió. La comparación en sombra permite descubrir diferencias de comportamiento *antes* de servir a nadie, de modo que el corte deja de ser un acto de fe. Cambia la decisión «¿cambiamos?» por «¿cuántas diferencias quedan sin explicar?».

## Cómo funciona

Cada petición real llega al sistema antiguo, que responde a la persona como siempre. Una copia se envía al sistema nuevo; su respuesta no se entrega, se compara con la antigua y la diferencia se registra. [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) pide tres cautelas:

1. **Efectos secundarios no duplicados.** La copia no puede escribir en la base real ni enviar correos; el sistema en sombra necesita sus propios almacenes o modos sin efecto.
2. **Regla de equivalencia.** Hay que decidir de antemano qué diferencias importan: los décimos de una nota, sí; el orden de los campos o la hora de generación, no. Sin regla, todo es diferencia y no se aprende nada.
3. **Ventana representativa.** El tráfico raro (cierres de mes, picos) debe estar en el periodo observado.

La causa de su valor es que compara contra el comportamiento *vigente*, que es el contrato real aunque nunca se haya documentado.

## Ejemplo

[SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) plantea el caso de un equipo que ejecuta la comparación en sombra durante cuatro semanas en las que no hay cierre y observa que no hay diferencias. Es el escenario de alerta de la clase: esas cuatro semanas no incluyeron el tráfico del cierre, así que «sin diferencias» solo vale para lo observado y el corte posterior quedaría sin verificar justo en el caso más exigente (ilustración propia: un redondeo distinto en los promedios solo asomaría entonces). La lección es doble: la ausencia de diferencias solo vale para el tráfico observado, y la ventana se elige por calendario, o se reproduce tráfico grabado del periodo crítico.

## Errores y confusiones comunes

- **«La sombra no muestra diferencias, luego es seguro».** Solo para la ventana observada; corrección de [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md): elegir la ventana por calendario y reproducir tráfico grabado.
- **Duplicar efectos.** Si la copia escribe o notifica, la sombra deja de ser sombra.
- **Comparar byte a byte.** Sin regla de equivalencia el ruido (marcas de tiempo, orden) tapa las diferencias reales.
- **Confundirla con una prueba A/B o un despliegue canario.** En esos, una parte de las personas recibe la respuesta nueva; en la sombra nadie.
- **Cortar todo de una vez.** [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) insiste en rebanadas con retroceso independiente.

## Límites y cuándo no aplica

No sirve donde los efectos externos no se pueden aislar (pagos, correos) salvo que existan modos de simulación; duplica la carga sobre las dependencias compartidas y su coste debe presupuestarse; y no valida el rendimiento bajo carga real si el sistema en sombra corre con menos recursos. Tampoco prueba la experiencia de usuario, porque nadie ve la respuesta nueva. Se complementa con una señal de equivalencia explícita y un canario, no los reemplaza.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa anticorrupción](./capa-anticorrupcion.md), [Estrangulamiento](../e/estrangulamiento.md), [Rama por abstracción](../r/rama-por-abstraccion.md), [Rebanada](../r/rebanada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón de estrangulamiento; autoridad: autor del texto.
- [Microsoft Azure Architecture Center: Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — fachada y migración incremental; autoridad: documentación de Microsoft.
- [Microsoft Azure Architecture Center: Anti-corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — traducción entre modelos; autoridad: documentación de Microsoft.
- [Fowler, «DarkLaunching»](https://martinfowler.com/bliki/DarkLaunching.html) — ejecutar con tráfico real sin exponer el resultado; autoridad: autor del texto.
- [Fowler, «FeatureToggle»](https://martinfowler.com/bliki/FeatureToggle.html) — banderas de funcionalidad y su costo; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Comparación diferencial](./comparacion-diferencial.md) · [Comparación pareada →](./comparacion-pareada.md)
