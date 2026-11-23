# Rama protegida

[↑ Glosario](../../README.md) · [← Rama por abstracción](./rama-por-abstraccion.md) · [Range-diff →](./range-diff.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Rama cuyas reglas de integración se imponen técnicamente.

Definición de trabajo de [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md).

## Por qué importa

La clase donde se define, [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), existe con este propósito: la clase existe para que lo que un repositorio publica pueda atribuirse a quien dice haberlo escrito y no haya cambiado desde entonces, y para que las reglas que lo protegen (revisión obligatoria, comprobaciones, firmas) sean una política explícita y no una expectativa.

## Cómo funciona

Según [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md):

Una rama protegida convierte reglas en condiciones técnicas: exigir PR, un número de aprobaciones, comprobaciones superadas, commits firmados y no permitir push forzado ni borrado. Cada regla cierra una clase de problema. Una política también tiene excepciones: las cuentas con permisos de administración pueden saltar reglas si la plataforma lo permite, y esas excepciones deben registrarse o desactivarse.

## Ejemplo

Ejemplo de [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) (sección «Caso conductor»):

El repositorio de la plataforma de entregas es el caso conductor de la [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md). Esta clase deja la política de protección y el procedimiento de claves. `SE-203` rescata una integración mal resuelta sobre una rama protegida y `SE-204` entrega una contribución con firma y procedencia. Cambia después un solo dato, desactivar el bypass de administración, y revisa qué eventos dejan de pasar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md)) son:

- **Un commit firmado no verifica** — causa: el archivo de firmantes no contiene la clave. Corrección: añadir la clave al archivo tras verificar la identidad.
- **Se confía en «verificado» como revisión** — causa: se confunde atribución con aprobación. Corrección: exigir PR y aprobación además de firma.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una rama protegida convierte reglas en condiciones técnicas: exigir PR, un número de aprobaciones, comprobaciones superadas, commits firmados y no permitir push forzado ni borrado. ([SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](./regla.md), [Bypass de administración](../b/bypass-de-administracion.md), [Firma de commit](../f/firma-de-commit.md), [Firmantes permitidos](../f/firmantes-permitidos.md), [Procedencia](../p/procedencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) — reglas de protección disponibles; autoridad: GitHub Docs.
- [Pro Git: Signing Your Work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work) — firma de commits y etiquetas; autoridad: Pro Git.
- [git-verify-commit](https://git-scm.com/docs/git-verify-commit) — verificación de firmas; autoridad: documentación de Git.
- [ssh-keygen (OpenBSD)](https://man.openbsd.org/ssh-keygen) — firmantes permitidos y firmas SSH; autoridad: OpenBSD.
- [GitHub: verificación de firmas de commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification) — qué muestra el alojamiento como verificado; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Rama por abstracción](./rama-por-abstraccion.md) · [Range-diff →](./range-diff.md)
