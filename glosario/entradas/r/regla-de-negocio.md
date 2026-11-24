# Regla de negocio

[↑ Glosario](../../README.md) · [← Regla de las tres condiciones](./regla-de-las-tres-condiciones.md) · [Regla de permisos →](./regla-de-permisos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Una **regla de negocio** es una decisión de la organización, independiente del sistema, sobre qué se acepta, se calcula o se rechaza ([SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)). Existiría aunque no hubiera software: «una entrega en gracia pierde el 10 % de la nota» es una regla de la institución, no del sistema.

## Por qué importa

Pertenece a la organización y cambia con la política, no con el código. Distinguirla del requisito funcional importa por **quién puede cambiarla**: la coordinación académica cambia la regla; el equipo cambia el modo de aplicarla. Si la regla vive solo en el código, cada cambio de política es un cambio de software y solo el equipo lo entiende.

## Cómo funciona

[SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) separa dos cosas. La **regla** dice qué se aplica («una entrega en gracia pierde el 10 %»). El **requisito funcional** dice cómo el sistema la aplica («calculará la nota final aplicando BR-07»). Esa separación permite que quien decide la política la cambie sin tocar el código, y que el requisito cambie solo cuando cambia **cómo** se aplica la regla.

La práctica de la clase es darle a la regla **identificador, texto, responsable y fecha**, registrada aparte del requisito que la aplica. El identificador permite referirla desde requisitos, pruebas y código; el responsable dice a quién preguntar; la fecha, desde cuándo rige. Y vive en **un solo punto**: el síntoma de lo contrario es que dos módulos calculan una nota distinta para la misma entrega porque la regla vive duplicada y cada copia evolucionó por su lado. La corrección es extraerla a un único lugar con identificador y responsable.

Las reglas con varias condiciones se especifican con tablas de decisión, para enumerar las combinaciones y detectar huecos: otro síntoma que la clase señala es que el comité de política pregunta «¿qué pasa si…?» y nadie lo sabe, porque se redactaron solo los casos felices. La regla también se conecta con las obligaciones externas, que son reglas impuestas desde fuera y no se negocian.

## Ejemplo

BR-07: «Una entrega en gracia pierde el 10 % de la nota». Responsable: coordinación académica. Vigente desde: inicio del semestre. Requisito que la aplica: «Cuando una estudiante envíe una entrega después del plazo y dentro de la gracia, el sistema calculará la nota final aplicando BR-07 y mostrará el descuento». Si la coordinación cambia el 10 % al 15 %, cambia la regla; el requisito no cambia. (Ejemplo basado en [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).)

## Errores y confusiones comunes

- **Dos módulos calculan notas distintas**: regla duplicada.
- **Mezclar regla y requisito** en la misma frase.
- **Reglas sin responsable**: nadie decide cuando hay duda.
- **Confundirla con una restricción técnica**: la regla viene de la organización.

## Límites y cuándo no aplica

No toda condición del sistema es una regla de negocio; las restricciones técnicas (límites de memoria) son otra cosa. En organizaciones sin proceso de decisión claro, la regla puede no tener responsable real. Y una regla muy volátil puede justificar sacarla a configuración.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Organización](../o/organizacion.md), [Sobre](../s/sobre.md), [Estados e invariantes](../e/estados-e-invariantes.md), [Requisito funcional](./requisito-funcional.md), [Tablas de decisión](../t/tablas-de-decision.md), [Tiempo, plazos y zonas](../t/tiempo-plazos-y-zonas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (31 clases más lo mencionan; las que más):

[SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de frase para requisitos; autoridad: IEEE International Requirements Engineering Conference.
- [Sitio de EARS (Alistair Mavin)](https://alistairmavin.com/ears/) — descripción de las plantillas por su autor.
- [Business Rules Manifesto](https://www.businessrulesgroup.org/brmanifesto.htm) — reglas como requisito de primer nivel; autoridad: Business Rules Group.
- [RFC 3339: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc3339) — formato de instantes con desplazamiento; autoridad: IETF.
- [IANA: Time Zone Database](https://www.iana.org/time-zones) — origen de las reglas de zona y de sus cambios; autoridad: IANA.

---

[↑ Glosario](../../README.md) · [← Regla de las tres condiciones](./regla-de-las-tres-condiciones.md) · [Regla de permisos →](./regla-de-permisos.md)
