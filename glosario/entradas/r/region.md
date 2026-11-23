# Región

[↑ Glosario](../../README.md) · [← Regeneración incremental](./regeneracion-incremental.md) · [Registro →](./registro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Zona con un propósito semántico (principal, navegación, cabecera) que se puede alcanzar por atajos.

Definición de trabajo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md).

## Por qué importa

La clase donde se define, [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), existe con este propósito: la clase existe para que construyas la interfaz con los elementos y atributos que expresan su significado, de modo que el teclado, el foco y las tecnologías de apoyo tengan algo fiable que usar, y para que midas lo que cuesta y lo que se rompe cuando se imita con elementos genéricos.

## Cómo funciona

Según [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md):

En la plataforma, cada componente tiene una ficha con su elemento nativo, su nombre accesible, su comportamiento de teclado y su gestión de foco; una prueba recorre el árbol de la página y falla si un control interactivo no tiene nombre, si un elemento con clic no es enfocable o si el orden de foco difiere del visual. Cada página lleva un enlace de salto, una región `main` y encabezados que reflejan la estructura; el modal de confirmación lleva el foco a su primer control, cierra con Escape y devuelve el foco a quien lo abrió.

## Ejemplo

Ejemplo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada componente tiene una ficha con su elemento nativo, su nombre accesible, su comportamiento de teclado y su gestión de foco; una prueba recorre el árbol de la página y falla si un control interactivo no tiene nombre, si un elemento con clic no es enfocable o si el orden de foco difiere del visual. Cada página lleva un enlace de salto, una región `main` y encabezados que reflejan la estructura; el modal de confirmación lleva el foco a su primer control, cierra con Escape y devuelve el foco a quien lo abrió.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md)) son:

- **Un control funciona con ratón y no con teclado** — causa: un div con clic sin foco ni teclas. Corrección: usar el elemento nativo o reproducir rol, foco y teclas.
- **El lector anuncia «botón» sin más** — causa: falta nombre accesible. Corrección: texto visible, etiqueta nativa o `aria-label` si no hay otra opción.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres modelos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún lector de pantalla, navegador automatizado ni persona usuaria de tecnologías de apoyo, y el modelo de foco, el cálculo de nombre y el analizador son subconjuntos de las especificaciones. La siguiente clase aplica el diseño visual sobre esta estructura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Principal](../p/principal.md), [Zona](../z/zona.md), [Enlace de salto](../e/enlace-de-salto.md), [Nombre accesible](../n/nombre-accesible.md), [Orden de foco](../o/orden-de-foco.md), [Rol](./rol.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (58 clases más lo mencionan; las que más):

[SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) — cálculo del nombre accesible; autoridad: W3C.
- [W3C: ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — patrones de interacción y regla de usar HTML nativo primero; autoridad: W3C.
- [W3C: Comprender 2.1.1 Teclado](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) — funcionalidad operable con teclado; autoridad: W3C.
- [W3C: Comprender 2.4.3 Orden del foco](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — orden del foco con sentido; autoridad: W3C.
- [W3C: Comprender 4.1.2 Nombre, función, valor](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) — rol, nombre y estado de los componentes; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Regeneración incremental](./regeneracion-incremental.md) · [Registro →](./registro.md)
