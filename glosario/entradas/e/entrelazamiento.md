# Entrelazamiento

[↑ Glosario](../../README.md) · [← Entrega continua](./entrega-continua.md) · [Entrevista como método →](./entrevista-como-metodo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

El **entrelazamiento** (*entanglement*) es una correlación entre qubits que impide describirlos por separado. Es el sentido de [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) (computación cuántica para ingenieros de software). La clase lo trata con simulaciones didácticas, no con hardware cuántico: lo importante para un ingeniero es qué consecuencia tiene para el modelo de cómputo.

## Por qué importa

Explica por qué el cómputo cuántico no es solo «probar muchas respuestas a la vez» y por qué simularlo en un computador clásico es caro. [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) resume la consecuencia: es de modelo, no de uso. El estado de un registro no se puede describir qubit por qubit, y por eso simularlo cuesta una cantidad exponencial de memoria.

## Cómo funciona

[SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) construye el caso más simple: se aplica la puerta H al primer qubit y después una puerta CNOT (que invierte el segundo si el primero vale 1). El resultado es el **estado de Bell**: amplitud 0,7071 en `00` y en `11`, y cero en `01` y `10`.

Al medir:

- Cada resultado individual es aleatorio.
- Pero las dos medidas coinciden siempre: no hay forma de que salgan `01` o `10`.

En 1 000 mediciones con semilla 48, salió `00` 514 veces y `11` 486; nunca `01` ni `10`. Un estado GHZ de 5 qubits dio `00000` 492 veces y `11111` 508. El conjunto está correlacionado de una forma que no se reproduce con valores predefinidos independientes.

## Ejemplo

El resultado de [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) con el estado de Bell es el ejemplo mismo: dos qubits cuyas mediciones coinciden siempre, aunque cada una por separado sea una moneda al aire. Una descripción por qubit («el primero vale 0 con probabilidad ½, el segundo con probabilidad ½») pierde la información clave: que son iguales. Esa pérdida es la razón de que la memoria necesaria crezca exponencialmente con el número de qubits en una simulación.

## Errores y confusiones comunes

- **Pensar que el entrelazamiento transmite información más rápido que la luz:** las mediciones individuales siguen siendo aleatorias.
- **Creer que los valores estaban «predefinidos»:** la clase señala que la correlación no se reproduce con valores predefinidos independientes.
- **Confundirlo con una correlación clásica,** como dos monedas que se guardaron iguales.
- **Esperar que acelere cualquier programa.**

## Límites y cuándo no aplica

Las cifras de [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md) son de un simulador con semilla fija, no de un equipo cuántico real, donde el ruido y la decoherencia degradan el estado. La clase da el concepto con un nivel de modelo para ingenieros de software; no sustituye el tratamiento físico ni matemático completo. Para el desarrollo habitual, no interviene.

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
