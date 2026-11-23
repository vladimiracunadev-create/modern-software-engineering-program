# Confianza cero

[↑ Glosario](../../README.md) · [← Confianza](./confianza.md) · [Confianza y extensiones →](./confianza-y-extensiones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Conjunto de principios que niegan confianza implícita por ubicación de red y evalúan cada solicitud.

Definición de trabajo de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md).

## Por qué importa

La clase donde se define, [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), existe con este propósito: la clase existe para que puedas responder, sobre cualquier despliegue en la nube, tres preguntas que suelen contestarse con una impresión: qué puede hablar con qué, quién puede hacer qué y dónde viven las credenciales que lo permiten.

## Cómo funciona

Según [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), en la sección «Confianza cero»:

NIST SP 800-207 describe una arquitectura que no concede confianza por estar «dentro» de la red: cada solicitud se autentica y se autoriza según identidad, estado del dispositivo y contexto, con el menor acceso posible. El principio es el contrario de la red privada como frontera. No elimina la segmentación, la complementa: la red reduce los caminos y la identidad decide quién los recorre. Es una orientación de diseño y no un producto, y adoptarla es sobre todo un trabajo de inventario de flujos y de identidades.

## Ejemplo

Caso medido en la sección «Confianza cero» de [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md):

NIST SP 800-207 describe una arquitectura que no concede confianza por estar «dentro» de la red: cada solicitud se autentica y se autoriza según identidad, estado del dispositivo y contexto, con el menor acceso posible. El principio es el contrario de la red privada como frontera. No elimina la segmentación, la complementa: la red reduce los caminos y la identidad decide quién los recorre. Es una orientación de diseño y no un producto, y adoptarla es sobre todo un trabajo de inventario de flujos y de identidades.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md)) son:

- **«La base de datos no es accesible desde internet» y alguien llega a ella** — causa: se miró la exposición directa y no el grafo. Corrección: calcular saltos mínimos desde la configuración real.
- **Un rol de servicio puede borrar o listar todo** — causa: política de servicio completo sobre todos los recursos. Corrección: generar la política desde el uso y añadir denegaciones explícitas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **confianza cero** (*zero trust*) es un modelo de seguridad que no concede acceso por estar «dentro» de una red: cada solicitud se autentica, se autoriza y se evalúa en el momento, con la identidad de quien la hace y el contexto en que ocurre. ([SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confianza](./confianza.md), [Conjunto](./conjunto.md), [Audiencia](../a/audiencia.md), [Credencial de vida corta](./credencial-de-vida-corta.md), [Entropía de Shannon](../e/entropia-de-shannon.md), [Escalada de privilegios](../e/escalada-de-privilegios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-401 — Redes, identidad y secretos en cloud](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md).

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

[↑ Glosario](../../README.md) · [← Confianza](./confianza.md) · [Confianza y extensiones →](./confianza-y-extensiones.md)
