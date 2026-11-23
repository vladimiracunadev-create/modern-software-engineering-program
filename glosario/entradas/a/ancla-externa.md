# Ancla externa

[↑ Glosario](../../README.md) · [← Ancla del ciclo](./ancla-del-ciclo.md) · [Anclaje →](./anclaje.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Huella de un registro publicada fuera del alcance de quien puede escribir en él.

Definición de trabajo de [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md): Copia del último resumen de una bitácora guardada fuera de ella.

## Por qué importa

La clase donde se define, [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), existe con este propósito: la clase existe para que puedas demostrar a una tercera persona, con evidencia y no con afirmaciones, que un control existe, funciona y sigue funcionando, y para que sepas dónde termina lo que la ingeniería puede demostrar y empieza lo que decide una norma, un contrato o un tribunal.

## Cómo funciona

Según [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md):

Un registro es evidencia solo si no puede alterarse sin dejar rastro. Una tabla modificable por la aplicación no lo es: quien compromete la aplicación puede editarla. Un registro con **cadena de huellas** (cada entrada incluye el hash de la anterior) detecta la modificación, el borrado y el reordenamiento de entradas intermedias, porque cualquier cambio rompe la huella siguiente. No detecta dos ataques: el **truncamiento** de las últimas entradas (la cadena que queda es válida) y la **reescritura** desde un punto con huellas recalculadas (quien puede escribir puede recalcular).

Según [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** la verificación del registro dice «íntegro» y faltan los accesos de las últimas horas. **Hipótesis rivales:** (a) la verificación está mal implementada; (b) los eventos no se registraron; (c) se eliminó el final del registro. **Prueba:** compara la huella final con la publicada fuera del sistema; si no coincide y la cadena restante es válida, la causa es un truncamiento. **Conclusión:** la cadena detecta eslabones rotos, no ausencias al final; sin ancla externa el truncamiento es invisible. **Regresión:** publica la huella final cada hora en un servicio externo y añade una prueba que simule truncamiento y reescritura y exija que la comparación los detecte.

## Ejemplo

Ejemplo de [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) (sección «Preguntas frecuentes»):

No. Detecta alteraciones y fija el orden, pero no prueba quién escribió las entradas ni cuándo. Para eso se añaden firmas y sellos de tiempo, y el ancla externa.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El registro de accesos se puede editar** — causa: tabla modificable por la aplicación. Corrección: solo anexado, cadena de huellas y ancla externa. ([SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md))
- **La cadena verifica pero el contenido fue alterado** — causa: sin ancla externa. Corrección: guardar el último resumen fuera de la bitácora. ([SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Conclusión:** la cadena detecta eslabones rotos, no ausencias al final; sin ancla externa el truncamiento es invisible. ([SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](./alcance.md), [Huella](../h/huella.md), [Registro](../r/registro.md), [Bitácora encadenada](../b/bitacora-encadenada.md), [Compuerta](../c/compuerta.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — responsabilidad proactiva; autoridad: Unión Europea.
- [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — protección y tratamiento de datos personales en Chile; autoridad: Biblioteca del Congreso Nacional de Chile.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — catálogo de controles; autoridad: NIST.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — métodos estadísticos; autoridad: NIST.
- [Schneier y Kelsey, 1999](https://doi.org/10.1145/317087.317089) — registros de auditoría seguros; autoridad: ACM Transactions on Information and System Security.

---

[↑ Glosario](../../README.md) · [← Ancla del ciclo](./ancla-del-ciclo.md) · [Anclaje →](./anclaje.md)
