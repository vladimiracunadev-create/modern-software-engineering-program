# Mínimo privilegio

[↑ Glosario](../../README.md) · [← Mínimo necesario](./minimo-necesario.md) · [Mirada repetida →](./mirada-repetida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

El **mínimo privilegio** es el principio de conceder a cada sujeto (persona, programa, cuenta de servicio, flujo o agente) solo los permisos que necesita para su función y solo mientras los necesita. Las clases lo formulan en cuatro contextos con el mismo núcleo: [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) lo define como autoridad mínima acotada en acción, alcance y duración; [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) como concesión estricta a la función y al tiempo; [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) y [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) lo aplican a cada flujo y trabajo de una canalización de integración continua; y [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) lo traslada a los agentes de IA. La formulación clásica es de Saltzer y Schroeder (1975): cada programa y cada usuario deben operar con el menor conjunto de privilegios necesario para su trabajo.

## Por qué importa

Un permiso que nadie usa sigue siendo un permiso que alguien puede abusar. Según [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), limitar los privilegios acota el daño que puede resultar de un accidente o de un error y reduce el número de programas con privilegios que hay que revisar. No evita el fallo: reduce su radio. Por eso es la defensa que más rinde cuando el control de entrada ya falló, sea por una credencial filtrada, un trabajo de compilación comprometido o un agente que interpreta mal una instrucción.

## Cómo funciona

El principio se aplica en tres dimensiones que [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) nombra juntas: **acción** (qué operaciones), **alcance** (sobre qué recursos) y **duración** (por cuánto tiempo). En la práctica, las clases lo concretan así:

- **Quitar** lo que la tarea no necesita: un agente que corrige un error no necesita enviar correos ([SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md)).
- **Confinar** lo que queda: escribir solo dentro del espacio de trabajo, leer solo el repositorio del trabajo ([SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md)).
- **Exigir aprobación humana** para lo que no se puede acotar ([SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md)).
- **Conceder con caducidad** y renovar solo lo necesario, para que el permiso no sobreviva a la tarea ([SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)).

La causa de que no basta configurarlo una vez la explica [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md): el mínimo privilegio **se pierde con el tiempo**. Cada cambio de función añade permisos y rara vez retira los anteriores; tras unos meses, la persona tiene todo lo que alguna vez necesitó. Las tres respuestas son revisar periódicamente y retirar (cuesta trabajo humano y deja residuo), conceder con caducidad (cuesta solicitudes y fricción) o reasignar el conjunto completo al cambiar de función (exige un registro de qué se concedió y por qué). Cuanto más sensible el permiso, más corta debe ser la concesión. Las cuentas de servicio siguen la misma regla.

## Ejemplo

En la canalización de [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) y [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), cada flujo y cada trabajo recibe solo los permisos que necesita. Como ilustración (no es un caso de las clases): un trabajo que solo ejecuta pruebas no necesita permiso para publicar, de modo que si una dependencia comprometida corre en él, el daño queda limitado a lo que ese trabajo podía tocar. En [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) el mismo razonamiento se aplica a un agente: se le retiran las herramientas que no necesita, se confina el espacio donde escribe y se pide aprobación para lo irreversible.

## Errores y confusiones comunes

- **Configurarlo una vez y olvidarlo.** Los permisos se acumulan con los cambios de función ([SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)); sin revisión o caducidad, el mínimo se convierte en el máximo histórico.
- **Confundir mínimo privilegio con denegar todo.** El principio pide los permisos que la función necesita, no ninguno; una función sin los permisos que requiere no se puede ejecutar y acaba compartiendo credenciales.
- **Dar permisos amplios «por si acaso» a cuentas de servicio y flujos.** Las cuentas de servicio y los trabajos automáticos también son sujetos y se rigen por la misma regla.
- **Tratar la aprobación humana como sustituto del confinamiento.** [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) los trata como capas distintas: aprobar cada acción no reemplaza limitar lo que el agente puede tocar.

## Límites y cuándo no aplica

El mínimo privilegio reduce el daño, no lo elimina: un permiso legítimo mal usado sigue causando daño dentro de su alcance. Tiene costos operativos que las clases reconocen: revisar cuesta trabajo humano, caducar cuesta solicitudes y fricción, y cuanto más fino el control, más permisos que administrar. Exige conocer qué necesita realmente cada función, y esa información suele estar incompleta; por eso se afina con el uso observado. Y no sustituye a la autenticación, a la separación de funciones ni a la detección: es una capa más de defensa en profundidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Componente](../c/componente.md), [Conjunto](../c/conjunto.md), [Flujo](../f/flujo.md), [ACL](../a/acl.md), [Autenticación](../a/autenticacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (24 clases más lo mencionan; las que más):

[SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md).

**Aparece en los casos de estudio:** [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder](https://doi.org/10.1109/PROC.1975.9939) — mínimo privilegio y protección de la información; autoridad: Proceedings of the IEEE, 1975.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — denegar por defecto, mínimo privilegio y pruebas; autoridad: OWASP.
- [Claude Code: permisos](https://code.claude.com/docs/en/permissions) — orden de evaluación, órdenes compuestas y fragilidad de los patrones sobre argumentos; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red a nivel del sistema operativo; autoridad: documentación de Anthropic.
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/) — riesgos, entre ellos la agencia excesiva; autoridad: proyecto OWASP GenAI.

---

[↑ Glosario](../../README.md) · [← Mínimo necesario](./minimo-necesario.md) · [Mirada repetida →](./mirada-repetida.md)
