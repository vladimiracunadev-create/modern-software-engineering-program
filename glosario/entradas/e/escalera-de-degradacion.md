# Escalera de degradación

[↑ Glosario](../../README.md) · [← Escalar](./escalar.md) · [Escalera de herramientas →](./escalera-de-herramientas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Secuencia ordenada de estados de menor servicio que adopta un sistema ante un fallo, cada uno con su límite declarado.

Definición de trabajo de [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-599 — Taller: elegir y degradar un patrón agéntico](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md): Secuencia ordenada de niveles de servicio.

## Por qué importa

En [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), el tema «Escalera de degradación» importa porque cambia un fallo visible por un estado declarado.

En [SE-599 — Taller: elegir y degradar un patrón agéntico](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), el tema «Escalera de degradación» importa porque define a qué se baja y en qué orden.

## Cómo funciona

Según [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), en la sección «Escalera de degradación»:

Cuando una dependencia cae, hay peldaños entre «todo funciona» y «error 500». Un primer peldaño es **servir lecturas obsoletas** de una caché, con una antigüedad máxima declarada y una etiqueta visible. Un segundo es **encolar las escrituras** localmente y reenviarlas al volver la dependencia, con un tamaño máximo de cola y una promesa honesta («tu entrega está recibida y se confirmará en unos minutos»). El último es **rechazar** con un mensaje claro. Cada peldaño cambia un fallo visible por un estado que hay que declarar, vigilar y limitar, y decidir cuál usar es una decisión de producto, no un interruptor técnico: aceptar una entrega que aún no está en la base es una promesa que hay que poder cumplir.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md):

El equipo ensambla el paquete. `GARANTIAS.md` declara, por operación, la garantía con su condición (por ejemplo, «el acuse se emite tras confirmar en dos de tres réplicas; sin mayoría se rechaza con un error reintentable») y lo que no garantiza. `PRESUPUESTOS.md` reparte 800 ms entre tres llamadas con un máximo de un reintento de 150 ms solo en la primera, con un máximo de 700 ms comprobado por una prueba.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md)) son:

- **El servicio tarda más que el plazo sin que nadie falle** — causa: tiempos límite que se suman por capa. Corrección: presupuesto de tiempo comprobado con una prueba.
- **Un estudiante tiene acuse y no entrega** — causa: acuse emitido al encolar sin distinguir estados. Corrección: estados «recibida» y «guardada» en la garantía.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos deterministas en Windows y Ubuntu (WSL2) con resultados idénticos. No se desplegó ningún servicio ni se midió una carga real: la caída de 60 s, la sobrecarga del 50 %, la proporción 30/70, la capacidad constante y las mutaciones del paquete son construcciones del autor, y el validador se escribió conociendo las mutaciones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite declarado](../l/limite-declarado.md), [Estado](./estado.md), [Límite](../l/limite.md), [Secuencia](../s/secuencia.md), [Archivo de límites](../a/archivo-de-limites.md), [Cobertura de un nivel](../c/cobertura-de-un-nivel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-599 — Taller: elegir y degradar un patrón agéntico](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: manejo de sobrecarga](https://sre.google/sre-book/handling-overload/) — descarte y prioridad; autoridad: Google.
- [AWS Builders' Library: load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) — rechazo de carga; autoridad: Amazon Web Services.
- [Little, «A proof for the queuing formula»](https://doi.org/10.1287/opre.9.3.383) — `L = λ · W`; autoridad: artículo original (1961).
- [Microsoft Azure: patrón de interruptor](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — protección de dependencias; autoridad: Microsoft.
- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) — estados del interruptor; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Escalar](./escalar.md) · [Escalera de herramientas →](./escalera-de-herramientas.md)
