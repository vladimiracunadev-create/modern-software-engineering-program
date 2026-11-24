# Escalera de degradación

[↑ Glosario](../../README.md) · [← Escalar](./escalar.md) · [Escalera de herramientas →](./escalera-de-herramientas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Una **escalera de degradación** es la secuencia ordenada de estados de menor servicio que adopta un sistema ante un fallo, cada uno con su límite declarado ([SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md)). [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) la usa en el sentido más amplio de secuencia ordenada de niveles de servicio, aplicada a sistemas con modelos de lenguaje.

## Por qué importa

Cuando una dependencia cae, entre «todo funciona» y «error 500» hay peldaños intermedios. Sin escalera, el sistema salta del servicio completo al fallo. La decisión que cambia es que la degradación se diseña de antemano, con límites y mensajes honestos, en vez de improvisarse durante el incidente. Y es una decisión de producto, no un interruptor técnico.

## Cómo funciona

[SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) describe tres peldaños:

1. **Servir lecturas obsoletas** de una caché, con una antigüedad máxima declarada y una etiqueta visible.
2. **Encolar las escrituras** localmente y reenviarlas al volver la dependencia, con un tamaño máximo de cola y una promesa honesta («tu entrega está recibida y se confirmará en unos minutos»).
3. **Rechazar** con un mensaje claro.

Cada peldaño cambia un fallo visible por un estado que hay que **declarar, vigilar y limitar**. Por eso cada nivel lleva su límite: cuánto tiempo, cuántos elementos, qué se promete. Sin límite, un nivel degradado se convierte en un fallo silencioso: la cola crece sin tope o la caché sirve datos arbitrariamente viejos.

La parte delicada es la promesa. Aceptar una entrega que aún no está en la base obliga a poder cumplirla. Por eso la clase distingue estados de garantía («recibida» y «guardada»): un acuse emitido al encolar sin distinguir estados genera estudiantes con acuse y sin entrega.

## Ejemplo

La base de entregas cae durante 60 s. Peldaño 1: la lista de entregas se sirve desde caché con una etiqueta «datos de hace 90 s». Peldaño 2: las nuevas entregas se encolan hasta un máximo de elementos y se responde «recibida». Si la cola se llena, peldaño 3: se rechaza con un mensaje claro. Escenario sintético de [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) (la caída de 60 s es una construcción del autor).

## Errores y confusiones comunes

- **El servicio tarda más que el plazo sin que nadie falle**: tiempos límite que se suman por capa; se corrige con un presupuesto de tiempo comprobado con una prueba.
- **Un estudiante tiene acuse y no entrega**: acuse emitido al encolar sin distinguir estados.
- **Degradar sin declarar el límite**: el nivel intermedio se vuelve indefinido.
- **Tratarla como detalle técnico**: aceptar trabajo bajo degradación es una promesa de producto.

## Límites y cuándo no aplica

[SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) indica que sus experimentos son deterministas, sin servicio desplegado ni carga real: la caída de 60 s, la sobrecarga del 50 %, la proporción 30/70 y las mutaciones del paquete son construcciones del autor, y el validador se escribió conociendo las mutaciones. La escalera exige que la degradación sea aceptable para el negocio; donde no lo es (por ejemplo, ciertos datos que no pueden estar obsoletos), el único peldaño válido es rechazar.

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
