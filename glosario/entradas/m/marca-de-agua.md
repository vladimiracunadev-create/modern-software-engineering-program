# Marca de agua

[↑ Glosario](../../README.md) · [← Máquina virtual](./maquina-virtual.md) · [Margen →](./margen.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Instante de llegada hasta el que se espera a los rezagados de una ventana.

Definición de trabajo de [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md): Estimación del tiempo del evento hasta el cual se espera que hayan llegado todos los datos.

## Por qué importa

En [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), el tema «Marca de agua» importa porque fija cuánto se espera y qué se declara tardío.

## Cómo funciona

Según [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md):

Un flujo no sabe si ya llegó todo lo de una ventana. La marca de agua es el instante hasta el que se decide esperar rezagados: «la ventana de las 10:00 se cierra cuando el reloj de llegada pasa de las 11:10». Lo que llega después es tardío. En el laboratorio, un flujo sin tolerancia dejó fuera de su ventana a 315 de 10 000 eventos (3,15 % del total); con 1 minuto de tolerancia, 262; con 10 minutos, 257; con 1 hora, 229; con 6 horas, 0. La curva es plana mientras la tolerancia es menor que el retraso típico de los rezagados y cae de golpe cuando la supera: los tardíos no se reparten, están concentrados entre 1 y 6 horas.

Según [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md):

Cada evento tiene dos tiempos: cuándo ocurrió y cuándo llegó. Contar «entregas por minuto» con el tiempo de llegada mezcla minutos; contarlas con el tiempo del evento exige decidir cuándo una ventana está completa. La **marca de agua** es la estimación de hasta qué tiempo del evento se espera que hayan llegado todos los datos; los que llegan después son **tardíos** y se descartan, se aplican como corrección o se envían a un canal aparte. La tolerancia de retraso fija ese compromiso: esperar más da resultados más completos y más tardíos. No existe una tolerancia correcta general: depende de la distribución de retrasos y de lo que cueste mostrar un número que luego cambia.

## Ejemplo

Caso medido en la sección «La marca de agua es una apuesta declarada» de [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md):

Un flujo no sabe si ya llegó todo lo de una ventana. La marca de agua es el instante hasta el que se decide esperar rezagados: «la ventana de las 10:00 se cierra cuando el reloj de llegada pasa de las 11:10». Lo que llega después es tardío. En el laboratorio, un flujo sin tolerancia dejó fuera de su ventana a 315 de 10 000 eventos (3,15 % del total); con 1 minuto de tolerancia, 262; con 10 minutos, 257; con 1 hora, 229; con 6 horas, 0.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los informes mezclan minutos** — causa: se agrupa por tiempo de llegada. Corrección: usar el tiempo del evento y declarar la marca de agua. ([SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md)) son: La mezcla de retrasos, el 3 % de tardíos y el 2 % de reentregas son construcciones del autor; la simulación procesa los eventos en orden de llegada con ventanas de una hora y no reproduce un motor de flujo con estado, activadores ni ventanas por sesión. No se midió ninguna fuente real ni ningún corredor de mensajes.

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
