# Presupuesto de privacidad

[↑ Glosario](../../README.md) · [← Presupuesto de pasos](./presupuesto-de-pasos.md) · [Presupuesto de recursos →](./presupuesto-de-recursos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Cantidad acumulada de pérdida de privacidad que consumen las respuestas con ruido de un mismo conjunto de datos.

Definición de trabajo de [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md).

## Por qué importa

La clase donde se define, [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), existe con este propósito: la clase existe para que puedas decidir qué datos de personas debe guardar un sistema, por cuánto tiempo y con qué grado de identificación, y para que demuestres con números que «anonimizar» no es borrar el nombre.

## Cómo funciona

Según [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md):

El equipo hace un inventario de 18 datos personales con finalidad, plazo y destino. Deja de guardar la dirección IP completa (guarda los dos primeros octetos para estadísticas y la completa solo siete días para investigar abusos), elimina el campo «teléfono de contacto» porque ninguna función lo usa y reduce la retención de registros de acceso de «indefinida» a 90 días con un trabajo programado que lo hace y una prueba que lo comprueba. Para el estudio sobre abandono entrega cifras agregadas con un presupuesto de privacidad y un conjunto generalizado con k mínimo declarado (no filas individuales). Los seudónimos para análisis se calculan con una clave por propósito. Los entornos de prueba reciben datos sintéticos. Atiende los derechos de acceso y supresión con una operación documentada y probada.

## Ejemplo

Ejemplo de [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) (sección «Ejemplo profesional»):

El equipo hace un inventario de 18 datos personales con finalidad, plazo y destino. Deja de guardar la dirección IP completa (guarda los dos primeros octetos para estadísticas y la completa solo siete días para investigar abusos), elimina el campo «teléfono de contacto» porque ninguna función lo usa y reduce la retención de registros de acceso de «indefinida» a 90 días con un trabajo programado que lo hace y una prueba que lo comprueba. Para el estudio sobre abandono entrega cifras agregadas con un presupuesto de privacidad y un conjunto generalizado con k mínimo declarado (no filas individuales). Los seudónimos para análisis se calculan con una clave por propósito.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md)) son:

- **Se reidentifica un conjunto sin nombres** — causa: combinación de cuasi-identificadores única. Corrección: medir unicidad y generalizar o publicar agregados.
- **Un hash de correo se invierte** — causa: hash sin clave de un dato adivinable. Corrección: HMAC con clave y clave por propósito.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún dato de personas reales; la población, las comunas, los 100 000 correos candidatos y la escala del ruido son construcciones del autor; la clase no implementa un sistema formal de privacidad diferencial ni da asesoría legal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Ruido](../r/ruido.md), [Cuasi-identificador](../c/cuasi-identificador.md), [K-anonimato](../k/k-anonimato.md), [Minimización de datos](../m/minimizacion-de-datos.md), [Seudonimización](../s/seudonimizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «ε».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — principios de minimización y plazo, protección desde el diseño y seudonimización; autoridad: Unión Europea.
- [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — protección y tratamiento de datos personales en Chile; autoridad: Biblioteca del Congreso Nacional de Chile.
- [Sweeney, 2002](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems.
- [Dwork y Roth, 2014](https://doi.org/10.1561/0400000042) — privacidad diferencial; autoridad: Foundations and Trends in Theoretical Computer Science.
- [Narayanan y Shmatikov, 2008](https://doi.org/10.1109/SP.2008.33) — reidentificación de conjuntos dispersos; autoridad: IEEE Symposium on Security and Privacy.

---

[↑ Glosario](../../README.md) · [← Presupuesto de pasos](./presupuesto-de-pasos.md) · [Presupuesto de recursos →](./presupuesto-de-recursos.md)
