# Contrato inteligente

[↑ Glosario](../../README.md) · [← Contrato entre equipos](./contrato-entre-equipos.md) · [Contrato multicapa →](./contrato-multicapa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Programa desplegado en una cadena que se ejecuta de forma determinista cuando se invoca.

Definición de trabajo de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md).

## Por qué importa

En [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), el tema «Contratos inteligentes» importa porque fija que el código es la regla y que un error es permanente.

## Cómo funciona

Según [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), en la sección «Contratos inteligentes»:

Un contrato inteligente es un programa que vive en la cadena y se ejecuta cuando se le invoca. Es **determinista** (todos los nodos deben llegar al mismo resultado), **público** (cualquiera puede leerlo y atacarlo) e **inmutable** una vez desplegado (salvo mecanismos de actualización diseñados de antemano). Sus errores son por eso costosos. La **reentrada** ocurre cuando el contrato llama a código ajeno antes de actualizar su propio estado: ese código puede volver a invocar al contrato y encontrar el estado viejo. La defensa es ordenar: comprobar condiciones, actualizar el estado y solo después interactuar con otros. La encuesta de Atzei et al. cataloga esta y otras clases de ataque.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md):

El equipo de la plataforma compara tres diseños para los certificados. (1) Un registro propio con firma digital de la plataforma y la clave pública publicada: cualquiera verifica sin llamar a la plataforma, el coste es mínimo y se puede revocar. (2) Una cadena pública donde se escribe el hash de cada certificado: añade un sello de fecha que la plataforma no puede alterar, a cambio de comisiones, latencia y un registro permanente. (3) Un contrato que emite certificados: añade lógica y un riesgo de error permanente.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md)) son:

- **Se trata un registro como verdadero «porque está en la cadena»** — causa: se confunde integridad con veracidad. Corrección: firmar en origen y verificar el dato fuera de la cadena.
- **Un pago se revierte tras darlo por definitivo** — causa: pocas confirmaciones para el poder del atacante. Corrección: calcular las confirmaciones con la fórmula y el supuesto declarado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md)) son: Las definiciones son operativas para los certificados verificables. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se minó en ninguna red, no se desplegó ningún contrato ni se usó valor económico: los bloques, las dificultades, las tasas de propagación y el contrato son modelos del autor. La siguiente clase pasa a los sistemas geoespaciales y temporales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bloque huérfano](../b/bloque-huerfano.md), [Confirmación](./confirmacion.md), [Prueba de trabajo](../p/prueba-de-trabajo.md), [Reentrada](../r/reentrada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Contratos inteligentes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Ethereum.org, seguridad de contratos inteligentes](https://ethereum.org/en/developers/docs/smart-contracts/security/) — prácticas y vulnerabilidades habituales; autoridad: Ethereum.org.
- [Nakamoto, «Bitcoin: A Peer-to-Peer Electronic Cash System» (2008)](https://bitcoin.org/bitcoin.pdf) — cadena de bloques con prueba de trabajo y análisis de la probabilidad de reversión; autoridad: autor del documento.
- [Lamport, Shostak y Pease, «The Byzantine Generals Problem» (ACM TOPLAS, 1982)](https://doi.org/10.1145/357172.357176) — acuerdo entre procesos con fallos arbitrarios; autoridad: ACM Transactions on Programming Languages and Systems.
- [Atzei, Bartoletti y Cimoli, «A Survey of Attacks on Ethereum Smart Contracts (SoK)» (2017)](https://doi.org/10.1007/978-3-662-54455-6_8) — catálogo de ataques a contratos; autoridad: Lecture Notes in Computer Science.
- [Solidity, consideraciones de seguridad](https://docs.soliditylang.org/en/latest/security-considerations.html) — reentrada y el patrón comprobar–efectos–interacciones; autoridad: documentación de Solidity.

---

[↑ Glosario](../../README.md) · [← Contrato entre equipos](./contrato-entre-equipos.md) · [Contrato multicapa →](./contrato-multicapa.md)
