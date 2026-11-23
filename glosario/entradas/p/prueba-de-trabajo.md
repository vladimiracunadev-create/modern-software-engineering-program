# Prueba de trabajo

[↑ Glosario](../../README.md) · [← Prueba de restauración](./prueba-de-restauracion.md) · [Prueba discriminante →](./prueba-discriminante.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Mecanismo por el cual un bloque solo es válido si su hash cumple una condición que exige muchos intentos.

Definición de trabajo de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md).

## Por qué importa

En [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), el tema «Prueba de trabajo» importa porque convierte el coste de cómputo en una medida de esfuerzo.

## Cómo funciona

Según [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), en la sección «Prueba de trabajo»:

En la prueba de trabajo, un bloque es válido solo si su hash, interpretado como un número, es menor que un objetivo. Como el hash no se puede dirigir, la única forma de hallar uno es probar valores (el *nonce*) hasta acertar. Con `b` ceros iniciales, la probabilidad de acertar en un intento es `2^−b`, de modo que el número de intentos sigue una distribución geométrica de media `2^b`; la mediana es menor que la media (alrededor de 0,69 veces) y la dispersión es grande. Rehacer un bloque pasado exige repetir el trabajo de ese bloque y el de todos los posteriores, y hacerlo antes de que la red añada más. Ese coste es la base de la garantía.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md):

El equipo de la plataforma compara tres diseños para los certificados. (1) Un registro propio con firma digital de la plataforma y la clave pública publicada: cualquiera verifica sin llamar a la plataforma, el coste es mínimo y se puede revocar. (2) Una cadena pública donde se escribe el hash de cada certificado: añade un sello de fecha que la plataforma no puede alterar, a cambio de comisiones, latencia y un registro permanente. (3) Un contrato que emite certificados: añade lógica y un riesgo de error permanente.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md)) son:

- **Se trata un registro como verdadero «porque está en la cadena»** — causa: se confunde integridad con veracidad. Corrección: firmar en origen y verificar el dato fuera de la cadena.
- **Un pago se revierte tras darlo por definitivo** — causa: pocas confirmaciones para el poder del atacante. Corrección: calcular las confirmaciones con la fórmula y el supuesto declarado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la prueba de trabajo, un bloque es válido solo si su hash, interpretado como un número, es menor que un objetivo. ([SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Huella](../h/huella.md), [Mecanismo](../m/mecanismo.md), [Bloque huérfano](../b/bloque-huerfano.md), [Confirmación](../c/confirmacion.md), [Contrato inteligente](../c/contrato-inteligente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nakamoto, «Bitcoin: A Peer-to-Peer Electronic Cash System» (2008)](https://bitcoin.org/bitcoin.pdf) — cadena de bloques con prueba de trabajo y análisis de la probabilidad de reversión; autoridad: autor del documento.
- [Lamport, Shostak y Pease, «The Byzantine Generals Problem» (ACM TOPLAS, 1982)](https://doi.org/10.1145/357172.357176) — acuerdo entre procesos con fallos arbitrarios; autoridad: ACM Transactions on Programming Languages and Systems.
- [Atzei, Bartoletti y Cimoli, «A Survey of Attacks on Ethereum Smart Contracts (SoK)» (2017)](https://doi.org/10.1007/978-3-662-54455-6_8) — catálogo de ataques a contratos; autoridad: Lecture Notes in Computer Science.
- [Solidity, consideraciones de seguridad](https://docs.soliditylang.org/en/latest/security-considerations.html) — reentrada y el patrón comprobar–efectos–interacciones; autoridad: documentación de Solidity.
- [Ethereum.org, seguridad de contratos inteligentes](https://ethereum.org/en/developers/docs/smart-contracts/security/) — prácticas y vulnerabilidades habituales; autoridad: Ethereum.org.

---

[↑ Glosario](../../README.md) · [← Prueba de restauración](./prueba-de-restauracion.md) · [Prueba discriminante →](./prueba-discriminante.md)
