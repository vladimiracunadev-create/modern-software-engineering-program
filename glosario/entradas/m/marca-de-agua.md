# Marca de agua

[↑ Glosario](../../README.md) · [← Máquina virtual](./maquina-virtual.md) · [Margen →](./margen.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

La **marca de agua** (*watermark*) es el instante hasta el que se decide esperar a los rezagados de una ventana de un flujo de datos. [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) (ingesta batch y streaming) la presenta como «la ventana de las 10:00 se cierra cuando el reloj de llegada pasa de las 11:10»; [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) la define como la estimación del tiempo del evento hasta el cual se espera que hayan llegado todos los datos. No es la marca de agua de imágenes ni de documentos.

## Por qué importa

Un flujo no sabe si ya llegó todo lo de una ventana. La marca de agua fija cuánto se espera y qué se declara tardío. Es una decisión de compromiso entre resultados completos y resultados a tiempo, no un detalle técnico.

## Cómo funciona

Cada evento tiene dos tiempos: cuándo *ocurrió* y cuándo *llegó* ([SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md)). Contar «entregas por minuto» con el tiempo de llegada mezcla minutos; contarlas con el tiempo del evento exige decidir cuándo una ventana está completa. Los eventos que llegan después de la marca son **tardíos** y se descartan, se aplican como corrección o se envían a un canal aparte. La **tolerancia de retraso** fija el compromiso: esperar más da resultados más completos y más tardíos.

El laboratorio de [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) muestra la forma de la curva: un flujo sin tolerancia dejó fuera de su ventana 315 de 10 000 eventos (3,15 %); con 1 minuto de tolerancia, 262; con 10 minutos, 257; con 1 hora, 229; con 6 horas, 0. La curva es plana mientras la tolerancia sea menor que el retraso típico de los rezagados y cae de golpe cuando lo supera, porque los tardíos están concentrados entre 1 y 6 horas.

## Ejemplo

Con los datos de la clase, una tolerancia de 10 minutos casi no mejora lo que logra la de 1 minuto (257 frente a 262 tardíos), y cuesta diez veces más latencia; subir a 6 horas elimina los tardíos pero retrasa cada resultado seis horas. La decisión depende de quién consume el número y cuánto vale la exactitud frente a la frescura.

## Errores y confusiones comunes

- **Usar el tiempo de llegada como tiempo del evento.**
- **Elegir una tolerancia sin mirar la distribución de retrasos reales.**
- **Descartar los tardíos sin registrarlos,** perdiendo la evidencia de que ocurrieron.
- **Esperar que exista una tolerancia universal correcta:** [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) dice que no existe.

## Límites y cuándo no aplica

La marca de agua es una *estimación*; un evento puede llegar después de cualquier tolerancia. Los datos de [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) son sintéticos, con retrasos concentrados entre 1 y 6 horas por construcción. En procesamiento por lotes, donde la ventana se cierra por calendario y se reprocesa, el problema se aborda con reprocesos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tiempo del evento](../t/tiempo-del-evento.md), [Espera](../e/espera.md), [Evento](../e/evento.md), [Instante](../i/instante.md), [Dato tardío](../d/dato-tardio.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Akidau et al., «The Dataflow Model» (VLDB, 2015)](https://doi.org/10.14778/2824032.2824076) — tiempo del evento, ventanas y marcas de agua; autoridad: Proceedings of the VLDB Endowment.
- [Apache Beam, guía de programación](https://beam.apache.org/documentation/programming-guide/) — marcas de agua y datos tardíos en un modelo unificado; autoridad: Apache Software Foundation.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — fundamentos de sistemas de datos, reintentos y procesamiento por flujo; autoridad: autor del libro.
- [Dean y Ghemawat, «MapReduce» (Communications of the ACM, 2008)](https://doi.org/10.1145/1327452.1327492) — reparto por clave y reejecución de tareas; autoridad: Communications of the ACM.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: Enterprise Integration Patterns.

---

[↑ Glosario](../../README.md) · [← Máquina virtual](./maquina-virtual.md) · [Margen →](./margen.md)
