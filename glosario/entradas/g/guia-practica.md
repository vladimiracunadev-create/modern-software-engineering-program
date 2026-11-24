# Guía práctica

[↑ Glosario](../../README.md) · [← Guardrail o barrera](./guardrail-o-barrera.md) · [Guion de inyección →](./guion-de-inyeccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Una **guía práctica** (*how-to guide*) es, en [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), una página orientada a un objetivo de trabajo concreto que supone competencia previa y admite bifurcaciones. Es uno de los cuatro tipos de documentación que distingue la clase: tutorial, guía práctica, referencia y explicación. No debe confundirse con el uso coloquial de «guía» como manual general.

## Por qué importa

Resuelve un problema de quien ya sabe lo básico y necesita hacer algo específico. Si se mezcla con un tutorial, quien tiene prisa debe leer lecciones; si se mezcla con una explicación, el procedimiento se pierde entre justificaciones. Cambia la decisión de qué entra en la página: solo lo que lleva de la situación inicial al objetivo.

## Cómo funciona

Una guía responde a un objetivo del trabajo («cambiar el tope de penalización de un curso»), da por sentado que quien la lee sabe lo básico y evita enseñar. Es una receta con **precondiciones**, **pasos** y una **forma de comprobar** que funcionó. Se distingue del tutorial porque admite bifurcaciones («si el curso tiene prórrogas activas, antes haz esto») y porque no garantiza que sea la primera vez de nadie: el tutorial guía a un principiante por un camino único y seguro.

El error típico que describe [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) es que la guía **crece**: se le añaden definiciones, el porqué del tope, una tabla de parámetros, y deja de ser una guía. La regla es que lo que sobra se enlaza: las definiciones y el porqué van a la explicación y los parámetros a la referencia. Empezar la guía con la historia de la política es la mezcla de contexto con procedimiento, y se corrige moviendo esa historia a la explicación y enlazándola desde el primer párrafo.

## Ejemplo

En la plataforma de entregas, la guía «Cambiar el tope de penalización de un curso» lista las precondiciones (permiso de administración del curso), los pasos, la comprobación (una entrega de prueba con retraso muestra el nuevo descuento) y una bifurcación para cursos con prórrogas. Enlaza al tutorial, a la referencia «Parámetros de penalización» y a la explicación «Por qué la penalización es diaria y con tope» en una línea cada una. La clase añade que la guía se ejecuta en integración continua, de modo que si el procedimiento deja de funcionar, la compilación lo detecta.

## Errores y confusiones comunes

- **Empezar con la historia de la política**: mezcla de contexto y procedimiento.
- **Convertirla en tutorial**: explicar lo básico a quien ya lo sabe.
- **Sin comprobación de éxito**: la lectora no sabe si terminó.
- **Dejarla sin ejecutar**: una guía que nadie prueba se desactualiza.

## Límites y cuándo no aplica

No sirve a quien aún no sabe lo básico (necesita un tutorial) ni a quien quiere entender por qué (necesita una explicación). Para tareas muy simples, una línea en la referencia puede bastar. Una guía solo es fiable mientras el sistema no cambie; por eso conviene que sea comprobable automáticamente o tenga fecha de revisión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Competencia](../c/competencia.md), [Página](../p/pagina.md), [Trabajo](../t/trabajo.md), [Explicación](../e/explicacion.md), [Página mixta](../p/pagina-mixta.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.
- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.
- [Diátaxis: explicación](https://diataxis.fr/explanation/) — contexto y alternativas; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Guardrail o barrera](./guardrail-o-barrera.md) · [Guion de inyección →](./guion-de-inyeccion.md)
