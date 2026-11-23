# Relleno de credenciales

[↑ Glosario](../../README.md) · [← Relleno](./relleno.md) · [Relleno por lotes →](./relleno-por-lotes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Ataque que prueba en un sitio pares usuario-contraseña filtrados de otros sitios, normalmente un intento por cuenta.

Definición de trabajo de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

## Por qué importa

La clase donde se define, [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), existe con este propósito: la clase existe para que puedas decir, con números y no con adjetivos, qué costaría a una persona atacante hacerse pasar por otra en la plataforma: adivinar su contraseña si se filtra la base, reutilizar una contraseña de otro sitio, quedarse con su sesión.

## Cómo funciona

Según [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md):

Hay tres ataques diferentes que se confunden. La **fuerza bruta** prueba muchas contraseñas contra una cuenta; un bloqueo por cuenta la frena y a la vez crea una arma de denegación de servicio: cualquiera puede bloquear a un docente con cinco intentos fallidos. La **pulverización** (password spraying) prueba una o unas pocas contraseñas comunes contra muchas cuentas, de modo que ninguna cuenta acumula fallos. El **relleno de credenciales** usa pares reales de otros sitios, un intento por cuenta; funciona porque las personas reutilizan contraseñas, y como cada intento es plausible, parece tráfico legítimo. El límite por dirección IP pierde sentido cuando el atacante dispone de miles de direcciones; el bloqueo por cuenta no se activa con un intento.

## Ejemplo

Caso medido en la sección «El relleno de credenciales» de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md):

La plataforma tiene 5 000 cuentas; 100 de ellas (2 %) reutilizan una contraseña que figura en la lista del atacante, que contiene un par por cuenta. El atacante dispone de 2 000 direcciones y envía un intento por par. Se miden seis configuraciones de defensa.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md)) son:

- **Una filtración rompe la mayoría de las cuentas** — causa: hash rápido o sal única global. Corrección: argon2id, scrypt o PBKDF2 con costo alto y sal por usuario.
- **El límite por IP no frena el relleno** — causa: el ataque reparte un intento por cuenta y cuenta con miles de direcciones. Corrección: segundo factor y rechazo de contraseñas comprometidas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **relleno de credenciales** usa pares reales de otros sitios, un intento por cuenta; funciona porque las personas reutilizan contraseñas, y como cada intento es plausible, parece tráfico legítimo. ([SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autenticación](../a/autenticacion.md), [Fijación de sesión](../f/fijacion-de-sesion.md), [Identificador de sesión](../i/identificador-de-sesion.md), [Sal](../s/sal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP: relleno de credenciales](https://owasp.org/www-community/attacks/Credential_stuffing) — descripción del ataque; autoridad: OWASP.
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) — requisitos de autenticación y de contraseñas; autoridad: NIST.
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — algoritmos y parámetros de almacenamiento; autoridad: OWASP.
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) — identificadores y ciclo de vida de la sesión; autoridad: OWASP.
- [W3C WebAuthn Nivel 2](https://www.w3.org/TR/webauthn-2/) — credenciales de clave pública ligadas al origen; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Relleno](./relleno.md) · [Relleno por lotes →](./relleno-por-lotes.md)
