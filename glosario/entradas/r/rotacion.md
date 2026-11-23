# Rotación

[↑ Glosario](../../README.md) · [← Roofline](./roofline.md) · [Rotación declarada →](./rotacion-declarada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Reemplazo de una credencial y retiro de la anterior.

Definición de trabajo de [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md).

## Por qué importa

En [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), el tema «Rotación» importa porque la ventana de exposición de un secreto filtrado depende del plazo y de la detección.

## Cómo funciona

Según [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md):

Si un secreto se filtra en un instante al azar entre dos rotaciones, la exposición media hasta la siguiente rotación es la mitad del plazo. Con detección a los 14 días, que obliga a rotar de inmediato, la exposición se acota por el menor de los dos tiempos. Se calculó con 20 000 filtraciones simuladas por celda.

Según [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md):

La rotación acota la ventana, pero no evita la filtración ni sustituye la detección: con un plazo de 90 días, una filtración dura 45 días de media si nadie la detecta. Rotar, detectar y emitir credenciales de vida corta se complementan.

## Ejemplo

Ejemplo de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) (sección «Preguntas frecuentes»):

La rotación acota la ventana, pero no evita la filtración ni sustituye la detección: con un plazo de 90 días, una filtración dura 45 días de media si nadie la detecta. Rotar, detectar y emitir credenciales de vida corta se complementan.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md)) son:

- **«La base de datos no es accesible desde internet» y alguien llega a ella** — causa: se miró la exposición directa y no el grafo. Corrección: calcular saltos mínimos desde la configuración real.
- **Un rol de servicio puede borrar o listar todo** — causa: política de servicio completo sobre todos los recursos. Corrección: generar la política desde el uso y añadir denegaciones explícitas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Límite y decisión.** El experimento no mide una malla de servicios ni el coste de operar certificados, que es real: autoridad certificadora, rotación, observabilidad y un nuevo punto de fallo si el proxy cae. ([SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reemplazo](./reemplazo.md), [Retiro](./retiro.md), [Confianza cero](../c/confianza-cero.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Entropía de Shannon](../e/entropia-de-shannon.md), [Escalada de privilegios](../e/escalada-de-privilegios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (36 clases más lo mencionan; las que más):

[SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — gestión, rotación y auditoría de secretos; autoridad: proyecto OWASP.
- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — principios de confianza cero; autoridad: NIST.
- [AWS IAM: lógica de evaluación de políticas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) — denegación por defecto y denegación explícita; autoridad: documentación del proveedor.
- [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) — direcciones privadas; autoridad: IETF.
- [RFC 4632](https://www.rfc-editor.org/rfc/rfc4632) — notación CIDR y agregación de prefijos; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Roofline](./roofline.md) · [Rotación declarada →](./rotacion-declarada.md)
