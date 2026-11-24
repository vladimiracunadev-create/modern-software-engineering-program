# Tablas de decisión

[↑ Glosario](../../README.md) · [← Tabla de diferencias](./tabla-de-diferencias.md) · [Táctica →](./tactica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Una **tabla de decisión** es una enumeración de combinaciones de condiciones con la acción de cada una, que permite comprobar completitud y consistencia ([SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md)). Es una técnica de especificación para reglas que dependen de varias condiciones.

## Por qué importa

Muestra huecos y contradicciones que el texto corrido oculta. Cuando una regla depende de varias condiciones, la prosa invita a describir los casos felices y olvidar el resto. La tabla obliga a mirar cada combinación y asignarle una acción o reconocer que no la tiene. Cambia el momento en que se descubre «¿qué pasa si…?»: en la mesa y no en producción.

## Cómo funciona

Se listan las condiciones (columnas de entrada) y las acciones; cada fila es una combinación de valores de las condiciones con la acción resultante. [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) destaca dos propiedades que la tabla permite comprobar:

- **Completitud**: ninguna combinación queda sin acción.
- **Consistencia**: ninguna combinación recibe acciones contradictorias.

El costo es exponencial: **n condiciones binarias dan 2ⁿ filas**. Por eso se limita a reglas con pocas condiciones o se complementa con técnicas de reducción (combinar filas que comparten acción, o aplicar cobertura combinatoria). La tabla de la plataforma de entregas es de penalización: condiciones como «¿hay gracia?», «¿hay prórroga?» y «¿se pasó del tope?», con la acción de cada combinación. La clase propone cambiar una sola regla (por ejemplo, que la prórroga se sume a la gracia) y revisar qué filas cambian.

Dos fallos que la clase prevé, con su causa: dos módulos calculan una nota distinta para la misma entrega porque la regla vive duplicada en el código y cada copia evolucionó por su lado (se extrae la regla a un único punto con identificador y responsable); el comité de política pregunta «¿qué pasa si…?» y nadie lo sabe porque se redactaron solo los casos felices (se enumeran combinaciones y se asigna a cada una una acción o una decisión pendiente).

## Ejemplo

Condiciones: **A** = entrega dentro de gracia; **B** = prórroga concedida. Acciones: nota completa, descuento, descuento reducido.

| A | B | Acción |
| --- | --- | --- |
| sí | sí | nota completa |
| sí | no | nota completa |
| no | sí | descuento reducido |
| no | no | descuento |

Cuatro filas cubren las dos condiciones binarias. Si alguien añade una tercera condición («¿pasó el tope?»), la tabla crece a ocho filas y aparecen combinaciones que la prosa no había considerado. (Tabla ilustrativa, no la de [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).)

## Errores y confusiones comunes

- **Dos módulos calculan notas distintas**: regla duplicada; corrección: único punto con identificador y responsable.
- **Nadie sabe qué pasa en un caso raro**: solo casos felices; corrección: enumerar y asignar acción o decisión pendiente.
- **Dejar filas «imposibles» sin declarar por qué lo son.**
- **Tablas enormes que nadie lee**: demasiadas condiciones.

## Límites y cuándo no aplica

El crecimiento exponencial las vuelve impracticables con muchas condiciones; ahí se descompone la regla o se usan otras técnicas. No expresan bien secuencias o estados (para eso, máquinas de estados). Con condiciones continuas, hay que discretizarlas en rangos, y la discretización es una decisión que debe justificarse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Condición](../c/condicion.md), [Enumeración](../e/enumeracion.md), [Estados e invariantes](../e/estados-e-invariantes.md), [Regla de negocio](../r/regla-de-negocio.md), [Requisito funcional](../r/requisito-funcional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-146 — Requisitos funcionales y reglas de negocio](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

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

[↑ Glosario](../../README.md) · [← Tabla de diferencias](./tabla-de-diferencias.md) · [Táctica →](./tactica.md)
