# Secreto

[↑ Glosario](../../README.md) · [← Seccionamiento](./seccionamiento.md) · [Secreto centinela →](./secreto-centinela.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Dato cuya divulgación permite o facilita una acción no autorizada.

Definición de trabajo de [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md): Valor cuya divulgación da acceso o daña a alguien: contraseñas, tokens, claves.
- En [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md): Valor cuyo conocimiento concede una capacidad, como una contraseña, una clave de API o un token.

## Por qué importa

En [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), el tema «Secretos» importa porque una credencial en claro hace inútil cualquier otra barrera.

En [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), el tema «Secreto» importa porque exige ciclo de vida y redacción

En [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), el tema «Secretos» importa porque un secreto en un argumento es visible a otros procesos.

## Cómo funciona

Según [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), en la sección «Secretos»:

Un secreto, como una clave o un token, se usa para demostrar identidad y se vuelve una vulnerabilidad cuando se copia al lugar equivocado: el repositorio, un registro, una imagen, un mensaje de chat. OWASP recomienda centralizarlos en un almacén con control de acceso y auditoría, rotarlos, no incluirlos en el código y preferir credenciales de vida corta emitidas a cada servicio. La razón es la contención: un secreto en un solo lugar y con caducidad corta limita cuánto tiempo y a quién sirve si se filtra.

## Ejemplo

Ejemplo de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma dibuja el grafo de flujos permitidos a partir de las reglas reales, no de su diagrama, calcula los saltos a la base de datos y al almacén de secretos y encuentra que el monitoreo abre dos caminos de tres saltos. Quita la regla del monitoreo hacia la aplicación y la sustituye por una lectura de métricas que la aplicación publica.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una clave aparece en el repositorio** — causa: secreto copiado a un script. Corrección: mover al almacén, rotar la clave y activar el análisis en cada confirmación. ([SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md))
- **Se borró un secreto del último commit y se da por resuelto** — causa: se ignoraron copias e historial. Corrección: revocar/rotar primero y evaluar exposición. ([SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md))
- **Un secreto sigue vivo tras borrarlo del archivo** — causa: el historial lo conserva. Corrección: rotarlo; buscar en el historial. ([SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La razón es la contención: un secreto en un solo lugar y con caducidad corta limita cuánto tiempo y a quién sirve si se filtra. ([SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md))
- Una regla útil: un secreto sin dueño y sin fecha de caducidad es un incidente esperando. ([SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Token](../t/token.md), [Valor](../v/valor.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Esquema](../e/esquema.md), [Herencia](../h/herencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (116 clases más lo mencionan; las que más):

[SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Secretos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — gestión, rotación y auditoría de secretos; autoridad: proyecto OWASP.
- [CWE-214: Invocation of Process Using Visible Sensitive Information](https://cwe.mitre.org/data/definitions/214.html) — riesgo de secretos en argumentos; autoridad: MITRE.
- [Python: `subprocess`](https://docs.python.org/3/library/subprocess.html) — procesos hijo usados en la medición del secreto.
- [Meli et al., NDSS 2019](https://www.ndss-symposium.org/ndss-paper/how-bad-can-it-git-characterizing-secret-leakage-in-public-github-repositories/) — filtración de secretos en repositorios públicos; autoridad: Network and Distributed System Security Symposium.
- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — principios de confianza cero; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Seccionamiento](./seccionamiento.md) · [Secreto centinela →](./secreto-centinela.md)
