# Desigualdad de Mosca

[↑ Glosario](../../README.md) · [← Desfase de reloj](./desfase-de-reloj.md) · [Desintermediación →](./desintermediacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Riesgo si vida del secreto más tiempo de migración supera el tiempo hasta un ordenador cuántico capaz.

Definición de trabajo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Por qué importa

La clase donde se define, [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), existe con este propósito: la clase existe para que puedas planificar y ejecutar una migración criptográfica sin esperar a que exista un ordenador cuántico capaz de romper la criptografía actual.

## Cómo funciona

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

Para decidir urgencia sin una fecha del ordenador cuántico, la desigualdad de Mosca compara tres cantidades en años: `x`, cuánto debe permanecer secreto el dato; `y`, cuánto tardas en migrar; `z`, cuánto falta para un ordenador cuántico capaz. Hay riesgo si `x + y > z`. Con valores de ejemplo del autor (no pronósticos): `x = 1`, `y = 3`, `z = 15`: 4 años, sin riesgo. `x = 15`, `y = 5`, `z = 15`: 20, riesgo. `x = 25`, `y = 5`, `z = 15`: 30, riesgo. `x = 10`, `y = 8`, `z = 15`: 18, riesgo, aun con datos de vida media, porque la migración es lenta. `x = 30`, `y = 6`, `z = 25`: 36, riesgo.

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

El equipo de *Avisos* hace el inventario y encuentra 31 usos de criptografía de clave pública: TLS entre cliente y servicio, TLS entre servicios, firmas de artefactos, tokens de sesión, certificados de dispositivos de aulas, cifrado de copias de seguridad con una clave pública y la firma de los informes que se entregan a las universidades. Clasifica por vida útil: las copias de seguridad y los historiales (25 años) son lo más urgente por la amenaza de almacenar ahora; los tokens de sesión (minutos) son lo menos urgente. El primer cambio es de agilidad: el formato de las copias identifica el algoritmo en una cabecera.

## Ejemplo

Ejemplo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* hace el inventario y encuentra 31 usos de criptografía de clave pública: TLS entre cliente y servicio, TLS entre servicios, firmas de artefactos, tokens de sesión, certificados de dispositivos de aulas, cifrado de copias de seguridad con una clave pública y la firma de los informes que se entregan a las universidades. Clasifica por vida útil: las copias de seguridad y los historiales (25 años) son lo más urgente por la amenaza de almacenar ahora; los tokens de sesión (minutos) son lo menos urgente. El primer cambio es de agilidad: el formato de las copias identifica el algoritmo en una cabecera.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para decidir urgencia sin una fecha del ordenador cuántico, la desigualdad de Mosca compara tres cantidades en años: ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))
- Para tres usos, calcula la desigualdad de Mosca con tus valores, decide si hace falta un híbrido, escribe qué tamaño nuevo aparece (clave, texto cifrado, firma, certificado) y qué límite conocido podría romper. ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Secreto](../s/secreto.md).
- **Ver también:** [Migración](../m/migracion.md), [Riesgo](../r/riesgo.md), [Agilidad criptográfica](../a/agilidad-criptografica.md), [Criptografía poscuántica](../c/criptografia-poscuantica.md), [Híbrido](../h/hibrido.md), [ML-DSA](../m/ml-dsa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Desfase de reloj](./desfase-de-reloj.md) · [Desintermediación →](./desintermediacion.md)
