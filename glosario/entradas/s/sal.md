# Sal

[↑ Glosario](../../README.md) · [← Saga](./saga.md) · [Sal de una clave →](./sal-de-una-clave.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Valor aleatorio único por contraseña, almacenado junto al hash, que impide reutilizar cálculos entre cuentas.

Definición de trabajo de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md): Texto que se añade a la entrada del hash para que dos banderas produzcan asignaciones independientes.

## Por qué importa

La clase donde se define, [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), existe con este propósito: la clase existe para que puedas decir, con números y no con adjetivos, qué costaría a una persona atacante hacerse pasar por otra en la plataforma: adivinar su contraseña si se filtra la base, reutilizar una contraseña de otro sitio, quedarse con su sesión.

## Cómo funciona

Según [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md):

Una función de hash criptográfica rápida como SHA-256 se diseñó para ser rápida; un atacante con una base filtrada la aprovecha. Las funciones de derivación de claves de contraseña (PBKDF2, scrypt, bcrypt, Argon2id) añaden un **costo configurable**: iteraciones, o memoria y paralelismo, que encarece cada candidato. La **sal** es un valor aleatorio único por contraseña que se guarda junto al hash; su efecto es doble: dos usuarios con la misma contraseña tienen hashes distintos y el atacante no puede reutilizar una tabla precalculada ni comparar un solo cálculo con toda la tabla, de modo que el costo de probar un candidato contra todos los usuarios se multiplica por el número de usuarios.

Según [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md):

No, si el hash es rápido. La sal evita reutilizar cálculos entre cuentas; no encarece cada candidato. Con una función rápida un atacante prueba miles de millones de candidatos por segundo con hardware común. La defensa es una función con costo configurable y una contraseña larga.

## Ejemplo

Ejemplo de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra por qué la sal importa solo cuando se ataca a muchos. Antes de ejecutarlo, predice cuántos cálculos de hash hace falta para probar 1 000 candidatos contra 10 usuarios con y sin sal.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una filtración rompe la mayoría de las cuentas** — causa: hash rápido o sal única global. Corrección: argon2id, scrypt o PBKDF2 con costo alto y sal por usuario. ([SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md))
- **Dos experimentos se confunden** — causa: misma huella sin sal. Corrección: usar la bandera como sal. ([SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La sal no frena al atacante que se concentra en una cuenta: contra una sola, probar mil candidatos sigue costando mil cálculos. ([SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md))
- La sal evita reutilizar cálculos entre cuentas; no encarece cada candidato. ([SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](../h/huella.md), [Valor](../v/valor.md), [Autenticación](../a/autenticacion.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Cubrimiento de pares](../c/cubrimiento-de-pares.md), [Deuda de banderas](../d/deuda-de-banderas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

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

[↑ Glosario](../../README.md) · [← Saga](./saga.md) · [Sal de una clave →](./sal-de-una-clave.md)
