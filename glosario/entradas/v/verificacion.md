# Verificación

[↑ Glosario](../../README.md) · [← Verificabilidad](./verificabilidad.md) · [Verificación de comportamiento →](./verificacion-de-comportamiento.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **verificación** es la comprobación de que el sistema, o un artefacto, cumple lo especificado. El programa lo precisa en varios niveles:

- **Conformidad con la especificación** ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md)).
- **Comprobación observable de que un paso dejó el sistema en el estado esperado** ([SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md)).
- **Comprobación de que la evidencia de un release es coherente con valores esperados fijados de antemano** ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md)).

Contrasta con la **validación** ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)): verificar es «¿lo hicimos bien?»; validar es «¿es lo correcto?».

## Por qué importa

Sin verificación, un procedimiento «funciona» y nadie sabe si resolvió. En agentes, la diferencia es operativa: un asistente puede declarar terminado un trabajo sin comprobar nada ([SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md)). Cambia qué se considera «hecho»: no cuando se ejecutó el paso, sino cuando una comprobación observable lo confirma.

## Cómo funciona

El principio de [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md): la verificación compara contra **valores esperados fijados de antemano**; si el valor esperado se toma del propio objeto verificado, la verificación pasa siempre. [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) lo traduce a documentación: tras cada paso de un procedimiento se añade un comando de comprobación con la salida esperada.

En el harness de un agente ([SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md)), la verificación es una de las decisiones que lo definen, junto con los permisos y la parada: lo que define al harness es qué decide, no qué biblioteca usa. Una configuración sin verificación resuelve tres tareas y declara terminadas las otras tres. La corrección del caso de [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md): restaurar la línea de verificación y añadir una compuerta ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)) que rechaza la terminación sin pruebas en verde.

## Ejemplo

```bash
./migrar.sh && psql -c "select count(*) from entregas" | grep -q 5231 || { echo "verificación fallida"; exit 1; }
```

El número esperado (5 231) se fijó antes de ejecutar el paso; no se lee del resultado de la propia migración.

## Errores y confusiones comunes

- **El procedimiento «funciona» y nadie sabe si resolvió.** Causa: no hay verificación por paso; corrección: añadir un comando de comprobación con la salida esperada ([SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md)).
- **Verificación que pasa siempre.** Causa: valores esperados tomados del propio documento; corrección: fijarlos de antemano ([SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md)).
- **Confundir verificar con validar.** Pasar pruebas no demuestra que se construyó lo necesario.

## Límites y cuándo no aplica

Verificar prueba conformidad con una especificación, no que la especificación sea correcta. Una verificación cubre lo que comprueba: un conjunto de pruebas en verde no implica ausencia de defectos. Y el uso de «verificación» en [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) es el de la cadena de suministro de un release; en otros contextos el término cubre técnicas distintas (inspección, análisis estático, pruebas formales).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor esperado](./valor-esperado.md), [Conformidad](../c/conformidad.md), [Especificación](../e/especificacion.md), [Estado](../e/estado.md), [Idempotencia](../i/idempotencia.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-479 — Taller: verificar la procedencia de un release](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (173 clases más lo mencionan; las que más):

[SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SLSA v1.0: niveles](https://slsa.dev/spec/v1.0/levels) — garantías de la construcción y verificación de procedencia; autoridad: proyecto SLSA, OpenSSF.
- [OpenSSL: pkeyutl](https://docs.openssl.org/3.0/man1/openssl-pkeyutl/) — firma y verificación en el taller; autoridad: proyecto OpenSSL.
- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.
- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — reconstrucción independiente; autoridad: proyecto Reproducible Builds.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro de software; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Verificabilidad](./verificabilidad.md) · [Verificación de comportamiento →](./verificacion-de-comportamiento.md)
