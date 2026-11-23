# Permiso efectivo

[↑ Glosario](../../README.md) · [← Permiso](./permiso.md) · [Permiso mínimo →](./permiso-minimo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Autoridad resultante después de reglas, grupos, herencia y contexto.

Definición de trabajo de [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md).

## Por qué importa

La clase donde se define, [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), existe con este propósito: la clase existe para explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.

## Cómo funciona

Según [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md):

El permiso efectivo puede depender de identidad efectiva, grupos suplementarios, máscara de ACL y de cada directorio padre. `chmod 777` ignora intención y amplía autoridad indiscriminadamente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md):

Un servicio fue instalado por una cuenta administrativa y su configuración quedó inaccesible a la identidad de servicio. En vez de ejecutar el servicio como administrador, se asigna lectura al sujeto específico sobre el objeto específico y se valida que no obtuvo escritura ni acceso a otros secretos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md)) son:

- **“Funciona como administrador” se declara solución** — causa: se ocultó la regla que denegó acceso. Corrección: reproducir sin elevar e identificar capacidad mínima.
- **Se aplica acceso universal** — causa: se confunde disponibilidad con autorización. Corrección: definir quién necesita qué acción y limitar alcance.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El permiso efectivo puede depender de identidad efectiva, grupos suplementarios, máscara de ACL y de cada directorio padre. ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Herencia](../h/herencia.md), [Regla](../r/regla.md), [ACL](../a/acl.md), [Autenticación](../a/autenticacion.md), [Autorización](../a/autorizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — File Access Permissions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_05) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — How User Account Control works](https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) — delimita el contrato técnico que debe cumplirse al explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.

---

[↑ Glosario](../../README.md) · [← Permiso](./permiso.md) · [Permiso mínimo →](./permiso-minimo.md)
