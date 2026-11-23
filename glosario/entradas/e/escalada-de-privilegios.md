# Escalada de privilegios

[↑ Glosario](../../README.md) · [← Escalada](./escalada.md) · [Escalado programado →](./escalado-programado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Obtención de más permisos de los concedidos, por ejemplo modificando las propias políticas.

Definición de trabajo de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md).

## Por qué importa

La clase donde se define, [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), existe con este propósito: la clase existe para que puedas responder, sobre cualquier despliegue en la nube, tres preguntas que suelen contestarse con una impresión: qué puede hablar con qué, quién puede hacer qué y dónde viven las credenciales que lo permiten.

## Cómo funciona

[SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. Cada proveedor usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md):

El equipo de la plataforma dibuja el grafo de flujos permitidos a partir de las reglas reales, no de su diagrama, calcula los saltos a la base de datos y al almacén de secretos y encuentra que el monitoreo abre dos caminos de tres saltos. Quita la regla del monitoreo hacia la aplicación y la sustituye por una lectura de métricas que la aplicación publica.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md)) son:

- **«La base de datos no es accesible desde internet» y alguien llega a ella** — causa: se miró la exposición directa y no el grafo. Corrección: calcular saltos mínimos desde la configuración real.
- **Un rol de servicio puede borrar o listar todo** — causa: política de servicio completo sobre todos los recursos. Corrección: generar la política desde el uso y añadir denegaciones explícitas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada proveedor usa estos términos con matices y debe contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ningún proveedor, política real ni repositorio real: la red, los roles, el registro de uso y los secretos son fabricados por el autor, el detector se escribió conociendo sus datos y la rotación supone filtraciones uniformes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Permiso](../p/permiso.md), [Confianza cero](../c/confianza-cero.md), [Entropía de Shannon](./entropia-de-shannon.md), [Menor privilegio](../m/menor-privilegio.md), [Política de permisos](../p/politica-de-permisos.md), [Rotación](../r/rotacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

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

[↑ Glosario](../../README.md) · [← Escalada](./escalada.md) · [Escalado programado →](./escalado-programado.md)
