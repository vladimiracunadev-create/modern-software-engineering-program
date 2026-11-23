# Cosechar ahora, descifrar después

[↑ Glosario](../../README.md) · [← Cortocircuito](./cortocircuito.md) · [Coste de una consulta →](./coste-de-una-consulta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Almacenar hoy datos cifrados para descifrarlos cuando exista hardware capaz.

Definición de trabajo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

## Por qué importa

La clase donde se define, [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), existe con este propósito: la clase existe para que un ingeniero de software pueda leer una afirmación sobre computación cuántica (un titular, una propuesta de un proveedor, una exigencia de cumplimiento) y decidir qué parte es verificable, qué parte es especulación y qué decisión concreta le cambia.

## Cómo funciona

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Qué sí: un ordenador cuántico suficientemente grande y con corrección de errores rompería RSA, Diffie-Hellman y las curvas elípticas con el algoritmo de Shor; debilitaría la criptografía simétrica y las funciones de resumen con Grover (se compensa con más bits); y podría simular sistemas cuánticos (química, materiales), que es el uso para el que fue propuesto. Qué no: no acelera la mayoría de las cargas de software (bases de datos, web, procesamiento de texto, entrenamiento de modelos de lenguaje), no «prueba todas las posibilidades a la vez» y no existe hoy un dispositivo que ejecute Shor contra claves reales.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Qué hacer ya: porque un adversario puede guardar hoy datos cifrados con claves que se romperían después (la amenaza llamada «cosechar ahora, descifrar después»), la decisión es de inventario y de migración criptográfica, no de comprar hardware cuántico. ([SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Amplitud](../a/amplitud.md), [Entrelazamiento](../e/entrelazamiento.md), [Interferencia](../i/interferencia.md), [NISQ](../n/nisq.md), [Puerta](../p/puerta.md), [Qubit](../q/qubit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cortocircuito](./cortocircuito.md) · [Coste de una consulta →](./coste-de-una-consulta.md)
