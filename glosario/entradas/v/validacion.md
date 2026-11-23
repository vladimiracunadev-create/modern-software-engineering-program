# Validación

[↑ Glosario](../../README.md) · [← Utilización](../u/utilizacion.md) · [Validación del paquete →](./validacion-del-paquete.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Comprobación, con las personas que tienen la necesidad, de que lo especificado es lo que se necesita.

Definición de trabajo de [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md): Utilidad en contexto.

## Por qué importa

En [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), el tema «Validación» importa porque comprueba que lo especificado es lo que se necesita, no solo que está bien escrito.

En [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), el tema «Validación» importa porque aplica tipo, rango y relaciones

## Cómo funciona

Según [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), en la sección «Validación»:

Validar es preguntar si el requisito es el correcto; verificar es preguntar si el sistema cumple el requisito. Boehm los resume como construir lo correcto frente a construirlo correctamente. La validación ocurre con las personas que tienen la necesidad (revisión, prototipo, ejemplos concretos), mientras que la verificación ocurre contra el texto (pruebas, inspecciones). Un requisito puede estar perfectamente escrito, perfectamente verificado y perfectamente equivocado. Por eso un acta de validación debe decir con quién se revisó, qué se mostró y qué se decidió, no solo «aprobado».

## Ejemplo

Ejemplo de [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sección «Ejemplo mínimo»):

El archivo declara `timeout=10`, el entorno `DIAGNOSTIC_KIT_TIMEOUT=0` y la CLI no lo cambia. La procedencia muestra entorno, pero la validación rechaza cero. La ejecución no sustituye silenciosamente otro valor ni inicia trabajo parcial.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)) son:

- **La especificación está completa y el sistema decepciona a quienes lo usan** — causa: solo se entrevistó a quien paga; el conocimiento tácito no se elicitó. Corrección: añadir observación del trabajo real y validar con la persona usuaria, no solo con el cliente.
- **Dos equipos discuten una frase durante una hora** — causa: la frase mezcla un requisito y una solución, y los interesados entienden cosas distintas. Corrección: separar necesidad, requisito y supuesto, y registrar el origen de cada uno.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso un acta de validación debe decir con quién se revisó, qué se mostró y qué se decidió, no solo «aprobado». ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Necesidades](../n/necesidades.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Esquema](../e/esquema.md), [Herencia](../h/herencia.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (142 clases más lo mencionan; las que más):

[SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Boehm: Verifying and validating software requirements and design specifications (1984)](https://doi.org/10.1109/MS.1984.233702) — validación frente a verificación; autoridad: IEEE Software.
- [Nuseibeh y Easterbrook: Requirements engineering, a roadmap (2000)](https://doi.org/10.1145/336512.336523) — panorama de las actividades de la disciplina; autoridad: ACM, The Future of Software Engineering.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — relación entre requisitos, supuestos del dominio y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.
- [Fagan: Design and code inspections to reduce errors in program development (1976)](https://doi.org/10.1147/sj.153.0182) — inspección estructurada con roles; autoridad: IBM Systems Journal.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — procesos y elementos de información de la ingeniería de requisitos; autoridad: ISO, IEC e IEEE.

---

[↑ Glosario](../../README.md) · [← Utilización](../u/utilizacion.md) · [Validación del paquete →](./validacion-del-paquete.md)
