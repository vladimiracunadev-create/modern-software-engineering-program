# Contrato inteligente

[↑ Glosario](../../README.md) · [← Contrato entre equipos](./contrato-entre-equipos.md) · [Contrato multicapa →](./contrato-multicapa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Un **contrato inteligente** (*smart contract*) es un programa desplegado en una cadena de bloques que se ejecuta de forma determinista cuando se invoca. Es la definición de [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) (blockchain, consenso y contratos inteligentes). Ni es un contrato en el sentido legal ni es «inteligente»: es código cuya ejecución replican todos los nodos de la red.

## Por qué importa

En un contrato inteligente el código es la regla, y un error es permanente. Por eso la decisión profesional no es solo cómo escribirlo, sino *si* hace falta. [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) compara tres diseños para certificados: un registro propio firmado, una cadena pública con el hash de cada certificado, y un contrato que emite certificados; el tercero añade lógica y un riesgo de error permanente.

## Cómo funciona

Según [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), un contrato tiene tres rasgos:

- **Determinista:** todos los nodos deben llegar al mismo resultado, así que no puede depender de fuentes no replicables.
- **Público:** cualquiera puede leerlo y atacarlo.
- **Inmutable** una vez desplegado, salvo mecanismos de actualización diseñados de antemano.

Su error característico es la **reentrada**: el contrato llama a código ajeno antes de actualizar su propio estado, y ese código vuelve a invocar al contrato, que encuentra el estado viejo. La defensa es ordenar: comprobar condiciones, actualizar el estado y solo después interactuar con otros. La encuesta de Atzei et al., que cita la clase, cataloga esta y otras clases de ataque.

## Ejemplo

En [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), el equipo de la plataforma evalúa certificados de dos maneras ligeras antes del contrato: (1) un registro propio con firma digital y clave pública publicada, que cualquiera verifica sin llamar a la plataforma y que puede revocarse; (2) un hash de cada certificado en una cadena pública, que añade un sello de fecha que la plataforma no puede alterar, a cambio de comisiones, latencia y un registro permanente. Ilustración del patrón de reentrada (esbozo, no de la clase):

```text
retirar(): enviar fondos al llamante; luego poner saldo = 0   # incorrecto
retirar(): poner saldo = 0; luego enviar fondos al llamante   # orden correcto
```

## Errores y confusiones comunes

- **Tratar un registro como verdadero «porque está en la cadena»:** se confunde integridad con veracidad. Corrección: firmar en origen y verificar el dato fuera de la cadena ([SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md)).
- **Dar un pago por definitivo con pocas confirmaciones:** puede revertirse; hay que calcular las confirmaciones según el poder del atacante.
- **Suponer que se puede corregir tras desplegar:** salvo mecanismo previsto, no se puede.

## Límites y cuándo no aplica

No conviene cuando hay una parte de confianza razonable, cuando se necesita corregir errores, o cuando el dato debe ser privado (el contrato es público). Los costos (comisiones, latencia, permanencia) pueden superar el beneficio frente a un registro firmado. La clase trabaja con modelos y datos sintéticos; no audita ningún contrato real.

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
