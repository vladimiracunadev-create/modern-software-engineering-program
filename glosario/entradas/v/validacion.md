# Validación

[↑ Glosario](../../README.md) · [← Utilización](../u/utilizacion.md) · [Validación del paquete →](./validacion-del-paquete.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **validación** es la comprobación, con las personas que tienen la necesidad, de que lo especificado es lo que se necesita ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)). [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) la resume como utilidad en contexto. Contrasta con la **verificación**: validar es preguntar si el requisito es el correcto; verificar es preguntar si el sistema cumple el requisito.

## Por qué importa

Boehm lo resume como construir lo *correcto* frente a construirlo *correctamente* ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)). Un requisito puede estar perfectamente escrito, perfectamente verificado y perfectamente equivocado. Sin validación, un equipo entrega con rigor algo que nadie necesita. Cambia con quién se habla y qué se muestra antes de construir.

## Cómo funciona

La validación ocurre **con las personas que tienen la necesidad**: revisión de requisitos, prototipos, ejemplos concretos y observación del trabajo real. La verificación ocurre **contra el texto**: pruebas e inspecciones. [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) pide un acta de validación que diga con quién se revisó, qué se mostró y qué se decidió, no solo «aprobado»; así se puede saber después si se validó con quien paga o con quien usa.

Una causa de fallo frecuente: solo se entrevistó a quien paga y el conocimiento tácito no se elicitó. La corrección es añadir observación del trabajo real y validar con la persona usuaria, no solo con el cliente. Otra: dos equipos discuten una frase durante una hora porque mezcla un requisito y una solución; se separan necesidad, requisito y supuesto y se registra el origen de cada uno.

## Ejemplo

```text
Acta de validación — REQ-12 "avisar antes del vencimiento"
Con: 3 docentes y 5 estudiantes | Se mostró: prototipo de avisos y 4 ejemplos reales
Se decidió: aviso a 48 h y 12 h; sin aviso nocturno | Pendiente: canal para estudiantes sin correo institucional
```

En contraste, `verificar` sería: la prueba automática confirma que se envía un aviso 48 h antes.

## Errores y confusiones comunes

- **La especificación está completa y el sistema decepciona.** Causa: solo se entrevistó a quien paga; corrección: observar el trabajo real y validar con la persona usuaria ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)).
- **Dos equipos discuten una frase durante una hora.** Causa: la frase mezcla requisito y solución; corrección: separar necesidad, requisito y supuesto y registrar el origen ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)).
- **Confundir validar con verificar.** Pasar todas las pruebas no valida nada sobre la necesidad.

## Límites y cuándo no aplica

No toda validación es posible antes de construir: algunas necesidades solo aparecen al usar el producto ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md): la operación informa nuevos requisitos). Validar con una muestra pequeña o no representativa da falsa seguridad. Y la palabra tiene otro uso técnico, la validación de entradas (formato, tipo), que es verificación contra reglas y no la validación de necesidades.

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

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Discord](../../../casos/exito/discord.md), [Cloudflare](../../../casos/exito/cloudflare.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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
