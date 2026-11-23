# Menor privilegio

[↑ Glosario](../../README.md) · [← Memoria virtual](./memoria-virtual.md) · [Mensaje accionable →](./mensaje-accionable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Principio de conceder a cada identidad solo los permisos necesarios para su tarea.

Definición de trabajo de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md).

## Por qué importa

En [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), el tema «Menor privilegio y escalada» importa porque un permiso para cambiar permisos equivale a todos los permisos.

## Cómo funciona

Según [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md):

El menor privilegio concede solo lo necesario para la tarea. Su dificultad es práctica: lo necesario se descubre usando, y los permisos amplios ahorran el descubrimiento. Por eso es habitual conceder «todas las acciones de este servicio» y olvidarlo. El riesgo grave no es lo concedido sino la **escalada**: una identidad que puede modificar políticas, crear credenciales o asumir otros roles puede concederse el resto. Un rol con permiso para adjuntar políticas equivale, en la práctica, a un administrador aunque su lista de acciones parezca corta.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md):

El equipo de la plataforma dibuja el grafo de flujos permitidos a partir de las reglas reales, no de su diagrama, calcula los saltos a la base de datos y al almacén de secretos y encuentra que el monitoreo abre dos caminos de tres saltos. Quita la regla del monitoreo hacia la aplicación y la sustituye por una lectura de métricas que la aplicación publica.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md)) son:

- **«La base de datos no es accesible desde internet» y alguien llega a ella** — causa: se miró la exposición directa y no el grafo. Corrección: calcular saltos mínimos desde la configuración real.
- **Un rol de servicio puede borrar o listar todo** — causa: política de servicio completo sobre todos los recursos. Corrección: generar la política desde el uso y añadir denegaciones explícitas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El menor privilegio concede solo lo necesario para la tarea. ([SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Permiso](../p/permiso.md), [Tarea](../t/tarea.md), [Confianza cero](../c/confianza-cero.md), [Entropía de Shannon](../e/entropia-de-shannon.md), [Escalada de privilegios](../e/escalada-de-privilegios.md), [Política de permisos](../p/politica-de-permisos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — principios de confianza cero; autoridad: NIST.
- [AWS IAM: lógica de evaluación de políticas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) — denegación por defecto y denegación explícita; autoridad: documentación del proveedor.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — gestión, rotación y auditoría de secretos; autoridad: proyecto OWASP.
- [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) — direcciones privadas; autoridad: IETF.
- [RFC 4632](https://www.rfc-editor.org/rfc/rfc4632) — notación CIDR y agregación de prefijos; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Memoria virtual](./memoria-virtual.md) · [Mensaje accionable →](./mensaje-accionable.md)
