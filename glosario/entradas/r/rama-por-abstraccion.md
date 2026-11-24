# Rama por abstracción

[↑ Glosario](../../README.md) · [← Raíz de confianza](./raiz-de-confianza.md) · [Rama protegida →](./rama-protegida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

La **rama por abstracción** (*branch by abstraction*) es la técnica que introduce una abstracción para cambiar una implementación sin ramas largas de control de versiones, con una bandera que elige qué implementación se usa. Es la definición de trabajo de [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), donde es la técnica equivalente al estrangulamiento (*strangler*) cuando el código a reemplazar está dentro del mismo programa. Pese al nombre, no usa ramas de Git: lo que hace es sustituirlas.

## Por qué importa

Una rama larga acumula conflictos con cada integración del resto del equipo y retrasa el descubrimiento de problemas hasta el final. La rama por abstracción permite **integrar con frecuencia código que aún no está activo**: el trabajo grande se hace en la rama principal, en pasos pequeños, sin tocar el comportamiento que ve la persona usuaria. Cambia la decisión de cómo reemplazar un componente interno: no con una reescritura aislada, sino con una costura y un traspaso gradual.

## Cómo funciona

[SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) da la secuencia:

1. Se introduce una **abstracción** (una interfaz o una función) sobre el comportamiento a cambiar.
2. El código existente pasa a ser **una implementación** de esa abstracción.
3. Se desarrolla la **nueva implementación** detrás de la misma abstracción, con una **bandera** que decide cuál se usa.
4. Se cambia el valor de la bandera **gradualmente**.
5. Cuando la nueva es la única en uso, se **retira la antigua y la bandera**.

La abstracción es una **costura de objeto** ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)): un punto donde se puede cambiar el comportamiento sin editar el código que la usa. Y la **prueba de caracterización** es la que garantiza que ambas implementaciones se comportan igual: fija el comportamiento actual, incluso el defectuoso, para detectar toda diferencia no intencionada.

La causa de que funcione es que separa dos cosas que una rama larga mezcla: *desarrollar* (que ocurre a diario, en la rama principal) y *activar* (una decisión de configuración reversible).

## Ejemplo

El módulo de calificaciones calcula promedios con una función antigua. Se define una interfaz `CalculoDePromedio`; la función antigua pasa a ser su implementación `Heredada`; se escribe `Nueva` y se activa con una bandera.

```python
def promedio(notas, flags):
    impl = Nueva() if flags.get("promedio_nuevo") else Heredada()
    return impl.calcular(notas)
```

Una prueba de caracterización ejecuta ambas con las mismas entradas y exige el mismo resultado. Cuando la bandera está al 100 % y sin incidentes, se borra `Heredada` y la bandera. El código es una ilustración del mecanismo de [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

## Errores y confusiones comunes

- **El corte se pospone una y otra vez.** El paso es demasiado grande para verificarse; corrección: dividir en rebanadas con retroceso independiente.
- **La sombra no muestra diferencias y hay error en producción.** La ventana no incluía el tráfico raro; elegir la ventana por calendario y reproducir tráfico grabado.
- **Dejar la bandera para siempre.** Una bandera sin plan de retiro se convierte en deuda; el último paso es retirarla.
- **Confundirla con una rama de Git.** Es una técnica de diseño, no una operación de control de versiones.

## Límites y cuándo no aplica

Las definiciones de [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) son operativas para el módulo de calificaciones; sus experimentos usan datos sintéticos, no migraron ningún sistema ni compararon tráfico real, y varios parámetros (el 10 % de rutas con regresión, la eficacia de la sombra) son construcciones del autor. La técnica exige poder introducir una costura: si el código a reemplazar está enredado con sus llamadores y no admite abstracción sin una refactorización previa, hay que hacer primero ese trabajo. Para reemplazar un sistema *externo* (otro proceso), la técnica equivalente es el estrangulamiento, no esta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abstracción](../a/abstraccion.md), [Capa anticorrupción](../c/capa-anticorrupcion.md), [Comparación en sombra](../c/comparacion-en-sombra.md), [Estrangulamiento](../e/estrangulamiento.md), [Rebanada](./rebanada.md).
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

[↑ Glosario](../../README.md) · [← Raíz de confianza](./raiz-de-confianza.md) · [Rama protegida →](./rama-protegida.md)
