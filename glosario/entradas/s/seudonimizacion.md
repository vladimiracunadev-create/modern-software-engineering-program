# Seudonimización

[↑ Glosario](../../README.md) · [← Sesgo entre entrenamiento y servicio](./sesgo-entre-entrenamiento-y-servicio.md) · [Severidad →](./severidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **seudonimización** sustituye un identificador (un nombre, un correo, un número) por un seudónimo, de modo que la persona solo pueda reidentificarse con información adicional que se guarda aparte. Es el sentido de [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) y [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md); [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) la presenta, en el dominio de salud y datos sensibles, como sustitución de un identificador por un código reversible para quien posea la tabla de equivalencias. Lo decisivo es la **reversibilidad controlada**: el vínculo existe, pero vive en otro lugar y bajo otro control de acceso.

## Por qué importa

Permite trabajar con datos sin mostrar a quién pertenecen: analizar, depurar o probar sin exponer identidades. Pero tiene una consecuencia legal que [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) y [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) repiten: para la normativa de protección de datos (el RGPD, citado por las clases), el dato seudonimizado **sigue siendo dato personal**, porque la reidentificación es posible con la información adicional. Es una medida de reducción de riesgo, no una salida del ámbito de la norma.

## Cómo funciona

El mecanismo importa porque hay formas de seudonimizar que no protegen:

- **Hash sin clave.** [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) muestra por qué falla: un hash de un identificador de siete dígitos no protege, porque quien conozca el formato puede calcular el hash de los diez millones de valores posibles y comparar. [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) lo repite para correos: con una lista de candidatos, se calculan los hashes y se comparan.
- **HMAC con clave secreta.** Un código de autenticación con clave obliga a conocer la clave; esta se guarda aparte, con acceso restringido, y se destruye cuando la finalidad termina ([SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md)).
- **Clave por conjunto.** [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) advierte que una clave única para todos los conjuntos hace que los seudónimos coincidan entre conjuntos y se puedan **enlazar**; con una clave por conjunto, cada uno tiene seudónimos distintos y solo quien tiene las claves puede cruzarlos.

La causa común es la información adicional: la protección es exactamente tan fuerte como la separación y el control de esa clave o tabla de equivalencias.

## Ejemplo

En [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), un identificador de siete dígitos tiene diez millones de valores posibles. Con un hash sin clave, calcular los diez millones de hashes y compararlos es trivial; con HMAC y una clave guardada aparte, quien tiene los hashes pero no la clave no puede reconstruir los identificadores. [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) añade que los entornos de prueba merecen la misma disciplina: datos sintéticos o enmascarados, nunca una copia de producción.

## Errores y confusiones comunes

- **Creer que un hash simple basta.** Sin clave, el espacio de valores posibles se enumera ([SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md)).
- **Creer que seudonimizar es anonimizar.** El dato sigue siendo personal para la norma porque se puede reidentificar con la información adicional ([SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md)).
- **Usar la misma clave en todos los conjuntos.** Los seudónimos coinciden y permiten enlazar registros entre conjuntos ([SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md)).
- **Guardar la clave junto a los datos.** Anula la separación que define la técnica.

## Límites y cuándo no aplica

La seudonimización no impide la reidentificación por otros atributos: para ese riesgo, [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) y [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) tratan el k-anonimato sobre los cuasi-identificadores, que es una técnica distinta. Tampoco elimina las obligaciones legales sobre el dato. Y su fuerza depende de gestionar la clave: si se pierde el control de la clave o de la tabla, el seudónimo deja de proteger. Las clases citan el RGPD y normas nacionales como fuente; la aplicación legal concreta debe consultarse con la norma vigente y con asesoría competente, no con este glosario.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reemplazo](../r/reemplazo.md), [Sustitución](./sustitucion.md), [Valor](../v/valor.md), [Consentimiento y finalidad](../c/consentimiento-y-finalidad.md), [Cuasi-identificador](../c/cuasi-identificador.md), [Daño, retiro y revisión](../d/dano-retiro-y-revision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-129 — Ética del descubrimiento y protección de participantes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-463 — Privacidad por diseño y minimización](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679 (RGPD)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — minimización, limitación de la conservación, seudonimización y consentimiento; autoridad: Unión Europea.
- [The Menlo Report (U.S. Department of Homeland Security)](https://www.dhs.gov/publication/menlo-report) — principios éticos para la investigación en tecnologías de la información; autoridad: U.S. Department of Homeland Security.
- [U.S. eCFR, 45 CFR Part 46: Protection of Human Subjects](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-50) — normas federales de protección de sujetos humanos, incluido el consentimiento informado; autoridad: Electronic Code of Federal Regulations.
- [Sweeney: Simple Demographics Often Identify People Uniquely](https://dataprivacylab.org/projects/identifiability/paper1.pdf) — identificación única a partir de pocos atributos demográficos; autoridad: Data Privacy Lab, Carnegie Mellon University.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — marco para gestionar el riesgo de privacidad; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Sesgo entre entrenamiento y servicio](./sesgo-entre-entrenamiento-y-servicio.md) · [Severidad →](./severidad.md)
