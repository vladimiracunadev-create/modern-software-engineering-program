# Cadena de hashes

[↑ Glosario](../../README.md) · [← Cache-aside](./cache-aside.md) · [Cadena de huellas →](./cadena-de-huellas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Cada bloque contiene el hash del anterior; cambiar un dato altera el hash de su bloque, lo que invalida el siguiente, y así hasta el final. Por eso una cadena de hashes hace **detectable** una alteración del historial. No la hace imposible, no valida el contenido y no dice quién escribió. Un certificado falso escrito en la cadena queda tan registrado como uno verdadero.

Explicación de la sección «Cadena de hashes» de [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md).

## Por qué importa

En [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), el tema «Cadena de hashes» importa porque explica qué integridad aporta y qué no.

En [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), el tema «Cadena de hashes» importa porque reescribir un commit cambia todos sus descendientes.

## Cómo funciona

Según [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), en la sección «Cadena de hashes»:

Cada bloque contiene el hash del anterior; cambiar un dato altera el hash de su bloque, lo que invalida el siguiente, y así hasta el final. Por eso una cadena de hashes hace **detectable** una alteración del historial. No la hace imposible, no valida el contenido y no dice quién escribió. Un certificado falso escrito en la cadena queda tan registrado como uno verdadero. La integridad se refiere al orden y a la no alteración posterior, no a la veracidad del dato original; para esa hace falta una firma de quien emite o una verificación fuera de la cadena.

Según [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), en la sección «Cadena de hashes»:

Cada commit incluye el identificador de su padre. Si se cambia el mensaje de un commit antiguo, ese commit tiene otro identificador, su hijo apunta ahora a un padre distinto y cambia también, y así hasta la punta. Por eso reescribir historia es detectable para quien conserva la punta antigua, y por eso las firmas de todos los descendientes dejan de valer. No impide reescribir: lo hace visible.

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

- **Prerrequisito:** las clases previas [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bloque huérfano](../b/bloque-huerfano.md), [Bypass de administración](../b/bypass-de-administracion.md), [Confirmación](./confirmacion.md), [Contrato inteligente](./contrato-inteligente.md), [Firma de commit](../f/firma-de-commit.md), [Firmantes permitidos](../f/firmantes-permitidos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-296 — Blockchain, consenso y contratos inteligentes](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

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

[↑ Glosario](../../README.md) · [← Cache-aside](./cache-aside.md) · [Cadena de huellas →](./cadena-de-huellas.md)
