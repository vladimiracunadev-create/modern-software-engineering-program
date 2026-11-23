# Firmantes permitidos

[↑ Glosario](../../README.md) · [← Firma digital](./firma-digital.md) · [Firmware →](./firmware.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Archivo que asocia identidades con claves públicas aceptadas para verificar firmas SSH.

Definición de trabajo de [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md).

## Por qué importa

La clase donde se define, [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), existe con este propósito: la clase existe para que lo que un repositorio publica pueda atribuirse a quien dice haberlo escrito y no haya cambiado desde entonces, y para que las reglas que lo protegen (revisión obligatoria, comprobaciones, firmas) sean una política explícita y no una expectativa.

## Cómo funciona

Según [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md):

Verificar una firma comprueba que fue hecha por la clave y sobre ese contenido. Para que sea útil hay que decidir qué claves se aceptan: con firmas SSH, un archivo de firmantes permitidos asocia identidades con claves públicas. Una firma válida de una clave que no está en la lista no es de confianza. Y que la clave esté en la lista no prueba que la persona no haya sido engañada o que la clave no se haya filtrado.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md):

La plataforma exige PR, una aprobación del propietario de código (`SE-199`), comprobaciones superadas, commits firmados en la rama principal y prohíbe el push forzado. Las claves de firma están asociadas a identidades en un archivo de firmantes versionado y revisado como cualquier otro cambio; un procedimiento documenta qué hacer si una clave se compromete (revocar, revisar los commits firmados con ella, avisar). El bypass de administración está desactivado y las excepciones se registran.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md)) son:

- **Un commit firmado no verifica** — causa: el archivo de firmantes no contiene la clave. Corrección: añadir la clave al archivo tras verificar la identidad.
- **Se confía en «verificado» como revisión** — causa: se confunde atribución con aprobación. Corrección: exigir PR y aprobación además de firma.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos de firma. La clave es desechable, los eventos y proporciones son del autor y no se probó ninguna infraestructura de claves, plataforma ni artefacto. La siguiente clase aplica todo lo anterior a un caso de rescate: una integración mal resuelta sobre una rama que otras personas ya tienen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bypass de administración](../b/bypass-de-administracion.md), [Firma de commit](./firma-de-commit.md), [Procedencia](../p/procedencia.md), [Rama protegida](../r/rama-protegida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ssh-keygen (OpenBSD)](https://man.openbsd.org/ssh-keygen) — firmantes permitidos y firmas SSH; autoridad: OpenBSD.
- [Pro Git: Signing Your Work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work) — firma de commits y etiquetas; autoridad: Pro Git.
- [git-verify-commit](https://git-scm.com/docs/git-verify-commit) — verificación de firmas; autoridad: documentación de Git.
- [GitHub: verificación de firmas de commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification) — qué muestra el alojamiento como verificado; autoridad: GitHub Docs.
- [GitHub: ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) — reglas de protección disponibles; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Firma digital](./firma-digital.md) · [Firmware →](./firmware.md)
