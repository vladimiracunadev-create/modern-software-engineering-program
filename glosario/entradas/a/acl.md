# ACL

[↑ Glosario](../../README.md) · [← Acierto@k](./acierto-k.md) · [Acoplamiento →](./acoplamiento.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Lista de reglas que asocia identidades o grupos con derechos sobre un objeto.

Definición de trabajo de [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md).

## Por qué importa

En [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), el tema «ACL y permisos» importa porque expresan derechos e herencia

## Cómo funciona

Según [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md):

Los bits clásicos expresan lectura, escritura y ejecución para propietario, grupo y otros. En un directorio, estos bits tienen semánticas distintas de un archivo: lectura enumera nombres, escritura modifica entradas y ejecución permite atravesar la ruta. Bits especiales y ACL agregan reglas que requieren análisis adicional.

Según [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md):

Con las ACL: `icacls ruta` las lista y las propiedades de seguridad del Explorador las muestran. Los resultados contienen SIDs y cuentas, por lo que una ficha pública debe describirlos de forma genérica (por ejemplo, «el propietario y el grupo de administradores tienen control total») y no copiarlos.

## Ejemplo

Ejemplo de [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) (sección «Preguntas frecuentes»):

Con las ACL: `icacls ruta` las lista y las propiedades de seguridad del Explorador las muestran. Los resultados contienen SIDs y cuentas, por lo que una ficha pública debe describirlos de forma genérica (por ejemplo, «el propietario y el grupo de administradores tienen control total») y no copiarlos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se revisa solo el archivo** — causa: se ignoran directorios padre, ACL o montaje. Corrección: trazar la ruta completa y la política efectiva. ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md))
- **El informe publica usuarios o ACL completas** — causa: se confundió evidencia con exposición. Corrección: minimizar y redactar datos sin perder la relación causal. ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El permiso efectivo puede depender de identidad efectiva, grupos suplementarios, máscara de ACL y de cada directorio padre. ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Derecho](../d/derecho.md), [Objeto](../o/objeto.md), [Regla](../r/regla.md), [Sobre](../s/sobre.md), [Autenticación](./autenticacion.md), [Autorización](./autorizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) — delimita el contrato técnico que debe cumplirse al explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.
- [The Open Group — File Access Permissions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_05) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — How User Account Control works](https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Acierto@k](./acierto-k.md) · [Acoplamiento →](./acoplamiento.md)
