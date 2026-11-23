# Registro de solo anexado

[↑ Glosario](../../README.md) · [← Registro de reparación](./registro-de-reparacion.md) · [Registro encadenado →](./registro-encadenado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Registro en el que solo se pueden añadir entradas y cualquier modificación posterior es detectable.

Definición de trabajo de [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md).

## Por qué importa

La clase donde se define, [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), existe con este propósito: la clase existe para que puedas demostrar a una tercera persona, con evidencia y no con afirmaciones, que un control existe, funciona y sigue funcionando, y para que sepas dónde termina lo que la ingeniería puede demostrar y empieza lo que decide una norma, un contrato o un tribunal.

## Cómo funciona

[SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md):

El equipo de la plataforma crea en el repositorio un archivo `trazabilidad.csv` con 40 requisitos y las columnas control, prueba, última evidencia (fecha, versión y huella) y responsable. Una tarea de la integración continua ejecuta las pruebas de cada control en cada versión, guarda el resultado con su huella y recalcula el embudo de cobertura, y falla si un requisito crítico pasa de 30 días sin evidencia.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md)) son:

- **Un requisito no tiene control** — causa: sin matriz de trazabilidad. Corrección: matriz versionada con las celdas vacías visibles.
- **La evidencia es de hace seis meses** — causa: pruebas manuales y esporádicas. Corrección: automatizar y guardar resultado con fecha y huella por versión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se auditó ninguna organización ni se verificó conformidad con ninguna norma; el embudo, la población de 2 000 eventos y la cadena de 1 000 eventos son construcciones del autor, y la clase no da asesoría legal ni interpreta ninguna ley.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](./registro.md), [Ancla externa](../a/ancla-externa.md), [Evidencia](../e/evidencia.md), [Muestreo de auditoría](../m/muestreo-de-auditoria.md), [Trazabilidad](../t/trazabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

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

[↑ Glosario](../../README.md) · [← Registro de reparación](./registro-de-reparacion.md) · [Registro encadenado →](./registro-encadenado.md)
