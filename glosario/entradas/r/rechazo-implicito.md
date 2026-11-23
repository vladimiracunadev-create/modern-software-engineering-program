# Rechazo implícito

[↑ Glosario](../../README.md) · [← Receptor idempotente](./receptor-idempotente.md) · [Recomendación condicionada →](./recomendacion-condicionada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Devolver un secreto distinto en lugar de un error ante un texto cifrado inválido.

Definición de trabajo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Por qué importa

En [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), el tema «Rechazo implícito» importa porque evita señales por errores de descifrado.

## Cómo funciona

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), en la sección «Rechazo implícito»:

En ML-KEM, descapsular un texto cifrado alterado no devuelve un error: devuelve otro secreto aparentemente válido. En el laboratorio, un bit cambiado en el primer byte del texto cifrado produjo un secreto distinto del original sin ninguna excepción. La razón es de seguridad: si el descifrado fallara con un error observable, un atacante podría usar esos fallos como oráculo para aprender información sobre la clave privada. El rechazo implícito vuelve inobservable la diferencia. Consecuencia para el software: la integración no puede apoyarse en «si falla, lo sabré»; la detección ocurre más adelante, cuando los dos extremos derivan claves distintas y la autenticación del canal falla. Es una razón para usar siempre los protocolos que autentican el canal y no inventar los propios.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md)) son: Se ejecutaron implementaciones de estudio de ML-KEM y ML-DSA con sus tamaños reales, una firma de Lamport y cálculos de Mosca con valores del autor; no se ejecutó SLH-DSA, ningún saludo TLS real ni rendimiento de producción. El siguiente paso, `SE-286`, aplica la confianza cero: decidir cada petición con identidad, contexto y política en lugar de confiar en la red, con tokens de vida corta y credenciales limitadas.

## Relación con otros conceptos

- **Prerrequisito:** [Secreto](../s/secreto.md).
- **Ver también:** [Agilidad criptográfica](../a/agilidad-criptografica.md), [Criptografía poscuántica](../c/criptografia-poscuantica.md), [Desigualdad de Mosca](../d/desigualdad-de-mosca.md), [Híbrido](../h/hibrido.md), [ML-DSA](../m/ml-dsa.md), [ML-KEM](../m/ml-kem.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Receptor idempotente](./receptor-idempotente.md) · [Recomendación condicionada →](./recomendacion-condicionada.md)
