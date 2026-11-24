# Prueba de trabajo

[↑ Glosario](../../README.md) · [← Prueba de restauración](./prueba-de-restauracion.md) · [Prueba discriminante →](./prueba-discriminante.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

La **prueba de trabajo** (*proof of work*) es el mecanismo por el cual un bloque solo es válido si su hash cumple una condición que exige muchos intentos. Es el sentido de [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) (blockchain, consenso y contratos inteligentes). El «trabajo» es cómputo gastado en probar valores; la «prueba» es que cualquiera puede comprobar en un solo cálculo que ese gasto ocurrió.

## Por qué importa

Convierte el costo de cómputo en una medida de esfuerzo, y de ese costo se deriva la garantía de la cadena: reescribir el pasado exige rehacer el trabajo. Entender el mecanismo permite razonar cuántas confirmaciones son razonables para dar un pago por definitivo, en vez de aceptarlo como dogma.

## Cómo funciona

[SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md): un bloque es válido solo si su hash, interpretado como un número, es menor que un objetivo. Como el hash no se puede dirigir, la única forma de hallar uno es probar valores, el *nonce*, hasta acertar. Con `b` ceros iniciales exigidos, la probabilidad de acertar en un intento es 2⁻ᵇ. Consecuencias:

- El número de intentos sigue una **distribución geométrica** de media 2ᵇ.
- La mediana es menor que la media (alrededor de 0,69 veces) y la dispersión es grande: unas veces se acierta pronto y otras tarda mucho más.
- Verificar es barato (un solo hash), producir es caro.
- **Rehacer un bloque pasado** exige repetir el trabajo de ese bloque y el de todos los posteriores, y hacerlo antes de que la red añada más. Ese costo es la base de la garantía.

Al subir `b` en uno, el trabajo esperado se duplica; la red ajusta el objetivo para mantener el ritmo de bloques.

## Ejemplo

Cálculo propio con la fórmula de la clase: con `b = 20` ceros iniciales, la media es 2²⁰ ≈ 1,05 millones de intentos y la mediana ronda 0,69 × 2²⁰ ≈ 725 000. Con `b = 24`, 16 veces más. Un atacante que quiera rehacer cuatro bloques debe repetir el trabajo de los cuatro y superar a la red que sigue añadiendo.

## Errores y confusiones comunes

- **Creer que el trabajo «resuelve un problema útil»:** su valor es el costo verificable, no el resultado.
- **Pensar que un bloque confirmado es irreversible:** es cuestión de probabilidad y de la potencia del atacante; se calculan las confirmaciones según ella ([SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md)).
- **Confundirla con consenso:** es un mecanismo para dar peso a bloques, no el consenso entero.
- **Esperar tiempos regulares:** la dispersión es grande.

## Límites y cuándo no aplica

El gasto energético es la contrapartida de la garantía, y existen otros mecanismos de consenso que no lo exigen. El modelo de [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) es de simulación; no mide una red real. No aporta nada a sistemas con participantes conocidos y confiables, donde un registro firmado basta.

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
