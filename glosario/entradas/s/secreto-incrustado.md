# Secreto incrustado

[↑ Glosario](../../README.md) · [← Secreto centinela](./secreto-centinela.md) · [Secretos y configuración →](./secretos-y-configuracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Credencial o clave guardada dentro del paquete de un cliente; es recuperable por quien tenga el paquete.

Definición de trabajo de [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md).

## Por qué importa

La clase donde se define, [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), existe con este propósito: la clase existe para que razones sobre la seguridad de un cliente que corre en un dispositivo ajeno: quién puede recalcular una comprobación de integridad, qué confina realmente el sandbox, qué comprobación de rutas es correcta y qué secretos no pueden vivir en el cliente.

## Cómo funciona

[SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md):

El equipo del cliente escribe su modelo de amenazas con una fila por activo (borrador local, token de sesión, paquete de actualización, adjuntos) y una columna por capacidad del atacante (lee el paquete, modifica archivos, observa el tráfico, controla el dispositivo). De la tabla salen reglas: el servidor valida todo, el cliente solo guarda tokens de corta duración emitidos por el servidor, los adjuntos se confinan a una carpeta con normalización y la actualización se verifica con una firma asimétrica cuya clave privada solo existe en el sistema de compilación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md)) son:

- **El cliente acepta un paquete modificado con su hash correcto** — causa: el hash viaja con el paquete y el atacante lo recalcula. Corrección: firma asimétrica con clave pública en el cliente.
- **Una ruta con dos puntos lee un archivo de configuración** — causa: se filtró por prefijo en lugar de normalizar. Corrección: normalizar y comparar con la raíz y un separador.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos ficticios en Windows y Ubuntu (WSL2) con resultados idénticos. No se firmó ningún paquete con criptografía asimétrica, no se analizó ningún binario real y las doce rutas no agotan las variantes. La siguiente clase aplica todo esto al adaptar el producto a dos plataformas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Paquete](../p/paquete.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Firma digital](../f/firma-digital.md), [Modelo de amenazas](../m/modelo-de-amenazas.md), [Sandbox](./sandbox.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Android Open Source Project, «Application Sandbox»](https://source.android.com/docs/security/app-sandbox) — aislamiento de aplicaciones por usuario de sistema; autoridad: Google.
- [Android Developers, «Sign your app»](https://developer.android.com/studio/publish/app-signing) — firma de aplicaciones Android; autoridad: Google.
- [Microsoft, «Package signing overview»](https://learn.microsoft.com/en-us/windows/msix/package/signing-package-overview) — firma de paquetes MSIX; autoridad: Microsoft.
- [Electron, «Security»](https://www.electronjs.org/docs/latest/tutorial/security) — prácticas de seguridad en aplicaciones de escritorio; autoridad: OpenJS Foundation.
- [OWASP, «MASVS»](https://mas.owasp.org/MASVS/) — requisitos de seguridad para aplicaciones móviles; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Secreto centinela](./secreto-centinela.md) · [Secretos y configuración →](./secretos-y-configuracion.md)
