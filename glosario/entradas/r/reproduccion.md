# Reproducción

[↑ Glosario](../../README.md) · [← Representación](./representacion.md) · [Reproducción determinista →](./reproduccion-determinista.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Reenvío de un mensaje legítimo capturado para que el receptor lo acepte de nuevo.

Definición de trabajo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md): Que otra persona, con el mismo código y los mismos datos, obtenga un resultado equivalente dentro de una tolerancia declarada.
- En [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md): Procedimiento que vuelve a producir un síntoma bajo condiciones declaradas.
- En [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md): Repetición documentada del método.
- En [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md): Procedimiento capaz de volver a mostrar el comportamiento bajo condiciones declaradas.

## Por qué importa

En [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), el tema «Anti-reproducción» importa porque un mensaje firmado vale mientras no pueda reutilizarse.

## Cómo funciona

Según [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

Un mensaje firmado puede capturarse y enviarse de nuevo. Dos mecanismos lo evitan. Una **ventana de tiempo** acepta mensajes con marca reciente; exige relojes razonablemente sincronizados y deja una ventana en que la reproducción es posible. Un **contador monótono** exige que cada mensaje tenga un número mayor que el anterior; no depende del reloj, pero necesita memoria persistente: si el contador se reinicia con el dispositivo, un mensaje capturado vuelve a ser válido. La elección se documenta con el desfase que tolera y la memoria que exige.

Según [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

Compara con el esquema de flota: la extracción de una clave en la auditoría compromete a un nodo, no a 200, y el servidor puede revocarlo; los mensajes legítimos ya no se rechazan por el desfase del reloj y una reproducción falla por el contador. Una política es adecuada cuando cada ataque de la lista tiene una respuesta; es frágil cuando depende de un secreto que nadie debería poder extraer.

## Ejemplo

Ejemplo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sección «Ejemplo profesional»):

Compara con el esquema de flota: la extracción de una clave en la auditoría compromete a un nodo, no a 200, y el servidor puede revocarlo; los mensajes legítimos ya no se rechazan por el desfase del reloj y una reproducción falla por el contador. Una política es adecuada cuando cada ataque de la lista tiene una respuesta; es frágil cuando depende de un secreto que nadie debería poder extraer.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un mensaje capturado se acepta días después** — causa: sin anti-reproducción o contador reiniciado. Corrección: contador persistente y ventana acotada. ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un contador monótono que se reinicia sin memoria persistente acepta una reproducción en el **50,8 %** de los casos del modelo. ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md))
- Son promesas distintas y cada una falla por razones distintas: la repetición falla por estado oculto (una variable de entorno, un archivo sin versionar), la reproducción por diferencias numéricas o de dependencias, la replicación porque el efecto no existía o dependía de la muestra. ([SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Repetición](./repeticion.md), [Resultado](./resultado.md), [Cambio mínimo](../c/cambio-minimo.md), [Estado inicial](../e/estado-inicial.md), [Fixture](../f/fixture.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (62 clases más lo mencionan; las que más):

[SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Spotify](../../../casos/exito/spotify.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «replay».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Krawczyk, Bellare y Canetti, RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — autenticación de mensajes con hash y clave; autoridad: IETF.
- [Krawczyk y Eronen, RFC 5869: HKDF](https://www.rfc-editor.org/rfc/rfc5869) — derivación de claves; autoridad: IETF.
- [NIST SP 800-57 Parte 1 rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión de claves; autoridad: NIST.
- [Heninger et al., «Mining your Ps and Qs» (USENIX Security, 2012)](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/heninger) — claves débiles por entropía insuficiente; autoridad: USENIX Security.
- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos básicos de ciberseguridad para IoT de consumo; autoridad: ETSI.

---

[↑ Glosario](../../README.md) · [← Representación](./representacion.md) · [Reproducción determinista →](./reproduccion-determinista.md)
