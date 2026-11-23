# Entrelazamiento

[↑ Glosario](../../README.md) · [← Entrega continua](./entrega-continua.md) · [Entrevista como método →](./entrevista-como-metodo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Correlación entre qubits que impide describirlos por separado.

Definición de trabajo de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

## Por qué importa

En [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), el tema «Entrelazamiento» importa porque correlaciones que no tienen análogo clásico simple.

## Cómo funciona

Según [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), en la sección «Entrelazamiento»:

Aplicar H al primer qubit y después una puerta CNOT (que invierte el segundo si el primero es 1) produce el estado de Bell: amplitud 0,7071 en `00` y en `11`, y cero en `01` y `10`. En 1 000 mediciones con semilla 48 salió `00` 514 veces y `11` 486; nunca `01` ni `10`. Un estado GHZ de 5 qubits dio `00000` 492 veces y `11111` 508. Cada resultado individual es aleatorio, pero el conjunto está correlacionado de una forma que no se reproduce con valores predefinidos independientes. Para un ingeniero de software la consecuencia es de modelo, no de uso: el estado de un registro no se puede describir qubit por qubit, y por eso simularlo cuesta una cantidad exponencial de memoria.

## Ejemplo

Caso medido en la sección «Entrelazamiento» de [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md):

Aplicar H al primer qubit y después una puerta CNOT (que invierte el segundo si el primero es 1) produce el estado de Bell: amplitud 0,7071 en `00` y en `11`, y cero en `01` y `10`. En 1 000 mediciones con semilla 48 salió `00` 514 veces y `11` 486; nunca `01` ni `10`. Un estado GHZ de 5 qubits dio `00000` 492 veces y `11111` 508. Cada resultado individual es aleatorio, pero el conjunto está correlacionado de una forma que no se reproduce con valores predefinidos independientes.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md)) son: Todo se simuló de forma clásica con NumPy; no hubo acceso a hardware cuántico ni se ejecutó ningún SDK; la búsqueda de periodo es la de un número de dos cifras y el modelo de ruido es básico.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Correlación](../c/correlacion.md), [Qubit](../q/qubit.md), [Amplitud](../a/amplitud.md), [Cosechar ahora, descifrar después](../c/cosechar-ahora-descifrar-despues.md), [Interferencia](../i/interferencia.md), [NISQ](../n/nisq.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-284 — Computación cuántica para ingenieros de software](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Entrega continua](./entrega-continua.md) · [Entrevista como método →](./entrevista-como-metodo.md)
