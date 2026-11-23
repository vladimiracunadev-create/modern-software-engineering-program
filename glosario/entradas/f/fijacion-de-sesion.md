# Fijación de sesión

[↑ Glosario](../../README.md) · [← Fidelidad](./fidelidad.md) · [Fijar por SHA →](./fijar-por-sha.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Ataque en el que el atacante impone a la víctima un identificador conocido antes de que se autentique.

Definición de trabajo de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

## Por qué importa

La clase donde se define, [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), existe con este propósito: la clase existe para que puedas decir, con números y no con adjetivos, qué costaría a una persona atacante hacerse pasar por otra en la plataforma: adivinar su contraseña si se filtra la base, reutilizar una contraseña de otro sitio, quedarse con su sesión.

## Cómo funciona

Según [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md):

Tras la autenticación el servidor entrega un identificador que, mientras sea válido, vale lo mismo que la contraseña. Debe tener entropía real (OWASP pide al menos 64 bits), generarse con el generador criptográfico del sistema y no derivarse de datos predecibles como la hora, un contador o el nombre. Se renueva en cada cambio de privilegio (inicio de sesión, elevación) para impedir la fijación de sesión, en la que el atacante conoce el identificador antes de que la víctima se autentique. Tiene dos plazos: **inactividad** (minutos para datos de alto valor, decenas para bajo riesgo) y **absoluto** (cuánto puede durar aunque se use). Se invalida en el servidor al cerrar sesión; borrar la cookie del navegador no cierra la sesión si el servidor la sigue aceptando.

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
- **Ver también:** [Autenticación](../a/autenticacion.md), [Identificador de sesión](../i/identificador-de-sesion.md), [Relleno de credenciales](../r/relleno-de-credenciales.md), [Sal](../s/sal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

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

[↑ Glosario](../../README.md) · [← Fidelidad](./fidelidad.md) · [Fijar por SHA →](./fijar-por-sha.md)
