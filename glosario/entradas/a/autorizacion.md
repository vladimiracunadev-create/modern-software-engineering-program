# Autorización

[↑ Glosario](../../README.md) · [← Autoritativo](./autoritativo.md) · [Autorización a nivel de objeto →](./autorizacion-a-nivel-de-objeto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

La **autorización** es la decisión sobre si una identidad ya autenticada puede realizar una acción sobre un recurso. [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) la define como decisión sobre una acción solicitada por una identidad; [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) y [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) la precisan: si un sujeto puede hacer una acción sobre un recurso, y [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) añade «en un momento dado». No es identificar a la persona (eso es la autenticación), sino evaluar acción sobre objeto bajo reglas.

## Por qué importa

Decide qué datos ve y qué cambios hace cada persona. Su fallo no produce errores visibles: produce una respuesta correcta para la persona equivocada. [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) recuerda que OWASP sitúa la autorización rota a nivel de objeto como el riesgo número uno de las API. La decisión profesional que cambia es dónde se comprueba (en el servidor, en cada petición) y qué se comprueba (la relación del sujeto con ese recurso concreto, no solo su rol).

## Cómo funciona

La sesión responde «quién es»; la autorización, «qué puede hacer sobre qué». Son decisiones separadas y la segunda se repite en cada petición, en el servidor, porque el cliente puede enviar cualquier identificador, rol o campo oculto. Saltzer y Schroeder lo llamaron **mediación completa**: cada acceso a cada objeto se comprueba, sin atajos por caché ni por «ya se comprobó en la pantalla anterior» ([SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)). Ocultar un botón mejora la experiencia, no la seguridad.

La regla práctica es un único punto de decisión, invocado en cada acceso, que deniega salvo que una regla permita. Cuando un endpoint recibe un identificador (`/entregas/4521`), el servidor busca el recurso y verifica que el sujeto tiene la relación requerida con *ese* recurso. En un sistema operativo ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md)) la decisión depende de más que el nombre: grupos, credenciales, propietario del objeto y política aplicable.

## Ejemplo

Ilustración mínima, no código de una clase:

```python
entrega = repo.obtener(id)
if entrega is None or entrega.autor_id != sujeto.id:
    raise Denegado()
```

En [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), un estudiante lee la entrega de otro porque el endpoint comprobaba el rol («estudiante») y no el dueño. Cambiar el número en la dirección es la prueba más simple del atacante y la que menos recursos exige.

## Errores y confusiones comunes

- **Acceso universal.** Se confunde disponibilidad con autorización; corrección: definir quién necesita qué acción y limitar el alcance ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md)).
- **Comprobar el rol y no el dueño.** Un estudiante lee la entrega de otro; corrección: autorización por objeto en cada endpoint con identificador ([SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)).
- **Confiar en el cliente.** Ocultar la opción no impide enviar la petición.

## Límites y cuándo no aplica

Una autorización correcta presupone una autenticación válida: si la identidad es falsa, la decisión se aplica a quien no corresponde. Las reglas deben revisarse con el tiempo, porque permisos concedidos se acumulan; [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) lo vincula al mínimo privilegio. Y una decisión bien tomada no impide el abuso por quien sí tiene permiso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Sobre](../s/sobre.md), [Sujeto](../s/sujeto.md), [ACL](./acl.md), [Audiencia](./audiencia.md), [Autenticación](./autenticacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (143 clases más lo mencionan; las que más):

[SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) — delimita el contrato técnico que debe cumplirse al explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.
- [OWASP API Security Top 10 2023: API1](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/) — autorización a nivel de objeto; autoridad: OWASP.
- [The Open Group — File Access Permissions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_05) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — How User Account Control works](https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Autoritativo](./autoritativo.md) · [Autorización a nivel de objeto →](./autorizacion-a-nivel-de-objeto.md)
