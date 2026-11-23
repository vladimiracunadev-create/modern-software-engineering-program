# Reentrada

[↑ Glosario](../../README.md) · [← Reemplazo atómico](./reemplazo-atomico.md) · [Reescribir historia →](./reescribir-historia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Llamada que vuelve a entrar en una función antes de que esta haya actualizado su estado.

Definición de trabajo de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md).

## Por qué importa

La clase donde se define, [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), existe con este propósito: la clase existe para que distingas lo que una cadena de bloques garantiza (que un historial no se altera sin que se note, bajo ciertos supuestos de poder de cómputo) de lo que no garantiza (que el dato registrado sea verdad, que el código sea correcto o que un atacante no pueda ganar con probabilidad pequeña), y para que decidas con evidencia si un problema necesita una cadena o una base de datos con auditoría.

## Cómo funciona

Según [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md):

Un contrato inteligente es un programa que vive en la cadena y se ejecuta cuando se le invoca. Es **determinista** (todos los nodos deben llegar al mismo resultado), **público** (cualquiera puede leerlo y atacarlo) e **inmutable** una vez desplegado (salvo mecanismos de actualización diseñados de antemano). Sus errores son por eso costosos. La **reentrada** ocurre cuando el contrato llama a código ajeno antes de actualizar su propio estado: ese código puede volver a invocar al contrato y encontrar el estado viejo. La defensa es ordenar: comprobar condiciones, actualizar el estado y solo después interactuar con otros. La encuesta de Atzei et al. cataloga esta y otras clases de ataque.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md):

El equipo de la plataforma compara tres diseños para los certificados. (1) Un registro propio con firma digital de la plataforma y la clave pública publicada: cualquiera verifica sin llamar a la plataforma, el coste es mínimo y se puede revocar. (2) Una cadena pública donde se escribe el hash de cada certificado: añade un sello de fecha que la plataforma no puede alterar, a cambio de comisiones, latencia y un registro permanente. (3) Un contrato que emite certificados: añade lógica y un riesgo de error permanente.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md)) son:

- **Se trata un registro como verdadero «porque está en la cadena»** — causa: se confunde integridad con veracidad. Corrección: firmar en origen y verificar el dato fuera de la cadena.
- **Un pago se revierte tras darlo por definitivo** — causa: pocas confirmaciones para el poder del atacante. Corrección: calcular las confirmaciones con la fórmula y el supuesto declarado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **reentrada** ocurre cuando el contrato llama a código ajeno antes de actualizar su propio estado: ese código puede volver a invocar al contrato y encontrar el estado viejo. ([SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Función](../f/funcion.md), [Bloque huérfano](../b/bloque-huerfano.md), [Confirmación](../c/confirmacion.md), [Contrato inteligente](../c/contrato-inteligente.md), [Prueba de trabajo](../p/prueba-de-trabajo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Solidity, consideraciones de seguridad](https://docs.soliditylang.org/en/latest/security-considerations.html) — reentrada y el patrón comprobar–efectos–interacciones; autoridad: documentación de Solidity.
- [Nakamoto, «Bitcoin: A Peer-to-Peer Electronic Cash System» (2008)](https://bitcoin.org/bitcoin.pdf) — cadena de bloques con prueba de trabajo y análisis de la probabilidad de reversión; autoridad: autor del documento.
- [Lamport, Shostak y Pease, «The Byzantine Generals Problem» (ACM TOPLAS, 1982)](https://doi.org/10.1145/357172.357176) — acuerdo entre procesos con fallos arbitrarios; autoridad: ACM Transactions on Programming Languages and Systems.
- [Atzei, Bartoletti y Cimoli, «A Survey of Attacks on Ethereum Smart Contracts (SoK)» (2017)](https://doi.org/10.1007/978-3-662-54455-6_8) — catálogo de ataques a contratos; autoridad: Lecture Notes in Computer Science.
- [Ethereum.org, seguridad de contratos inteligentes](https://ethereum.org/en/developers/docs/smart-contracts/security/) — prácticas y vulnerabilidades habituales; autoridad: Ethereum.org.

---

[↑ Glosario](../../README.md) · [← Reemplazo atómico](./reemplazo-atomico.md) · [Reescribir historia →](./reescribir-historia.md)
