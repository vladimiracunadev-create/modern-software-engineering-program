# Identificador de sesión

[↑ Glosario](../../README.md) · [← Identificador de correlación](./identificador-de-correlacion.md) · [Identificadores y expresiones spdx →](./identificadores-y-expresiones-spdx.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Valor que el servidor reconoce como prueba de una autenticación previa y que vale lo mismo que ella mientras sea válido.

Definición de trabajo de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

## Por qué importa

La clase donde se define, [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), existe con este propósito: la clase existe para que puedas decir, con números y no con adjetivos, qué costaría a una persona atacante hacerse pasar por otra en la plataforma: adivinar su contraseña si se filtra la base, reutilizar una contraseña de otro sitio, quedarse con su sesión.

## Cómo funciona

[SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md):

El equipo de la plataforma sustituye SHA-256 por Argon2id con los parámetros de OWASP, migra al iniciar sesión (verifica con el hash antiguo, vuelve a guardar con el nuevo), exige quince caracteres para contraseñas sin segundo factor, rechaza contraseñas presentes en una lista de valores comunes y exige segundo factor a docentes y administración. Mide el tiempo de verificación en su propio entorno y comprueba que con el límite de peticiones del endpoint no se convierte en un punto de denegación: el costo del hash lo paga también el servidor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md)) son:

- **Una filtración rompe la mayoría de las cuentas** — causa: hash rápido o sal única global. Corrección: argon2id, scrypt o PBKDF2 con costo alto y sal por usuario.
- **El límite por IP no frena el relleno** — causa: el ataque reparte un intento por cuenta y cuenta con miles de direcciones. Corrección: segundo factor y rechazo de contraseñas comprometidas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): relleno y sesión con cifras idénticas; los tiempos de las funciones de derivación son lecturas de reloj de cada equipo y difieren.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autenticación](../a/autenticacion.md), [Valor](../v/valor.md), [Fijación de sesión](../f/fijacion-de-sesion.md), [Relleno de credenciales](../r/relleno-de-credenciales.md), [Sal](../s/sal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) — requisitos de autenticación y de contraseñas; autoridad: NIST.
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — algoritmos y parámetros de almacenamiento; autoridad: OWASP.
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) — identificadores y ciclo de vida de la sesión; autoridad: OWASP.
- [OWASP: relleno de credenciales](https://owasp.org/www-community/attacks/Credential_stuffing) — descripción del ataque; autoridad: OWASP.
- [W3C WebAuthn Nivel 2](https://www.w3.org/TR/webauthn-2/) — credenciales de clave pública ligadas al origen; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Identificador de correlación](./identificador-de-correlacion.md) · [Identificadores y expresiones spdx →](./identificadores-y-expresiones-spdx.md)
