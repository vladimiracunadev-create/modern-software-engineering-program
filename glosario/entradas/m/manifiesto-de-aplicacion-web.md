# Manifiesto de aplicación web

[↑ Glosario](../../README.md) · [← Manifiesto](./manifiesto.md) · [Manifiesto de operabilidad →](./manifiesto-de-operabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Archivo JSON que declara el nombre, los iconos, la URL de inicio y el alcance de una aplicación instalable.

Definición de trabajo de [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md).

## Por qué importa

La clase donde se define, [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), existe con este propósito: el proyecto existe para que entregues una aplicación web de entregas accesible y utilizable sin conexión **junto con un paquete de evidencia que otra persona pueda revisar**: el manifiesto, las estrategias de caché, la tabla de estados, las URLs, las cabeceras, el presupuesto, el informe de accesibilidad con sus dos columnas y una matriz de pruebas con sus límites.

## Cómo funciona

[SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md):

La entrega del proyecto es un repositorio con la aplicación y una carpeta `evidence/` que contiene: el manifiesto con su validación, la tabla de estrategias por recurso, la tabla de estados con un escenario por transición, la tabla de URLs con sus redirecciones, el informe de cabeceras generado contra un servidor local, el presupuesto con su comprobador, el informe de accesibilidad con las columnas «lo vio una regla» y «lo vio una persona» y la matriz de pruebas con su cobertura de pares y la lista de casos añadidos a mano.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md)) son:

- **El manifiesto valida pero la aplicación no es instalable** — causa: iconos inexistentes o de tamaño distinto al declarado. Corrección: comprobar que los archivos existen y miden lo declarado.
- **Una versión nueva no llega a los dispositivos** — causa: `sw.js` servido con caché larga. Corrección: servirlo con `no-cache` y añadir una regla al comprobador.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El manifiesto, el servidor de ocho respuestas y los 60 defectos de tres factores son construcciones del autor; no se instaló la aplicación, no se ejecutó un service worker en un navegador y no se evaluó con personas con discapacidad. Este proyecto cierra la [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md); la siguiente parte del programa cambia de superficie.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Declaración de límites](../d/declaracion-de-limites.md), [Paquete de evidencia](../p/paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-240 — Proyecto: aplicación web accesible y offline](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Web Application Manifest (W3C)](https://www.w3.org/TR/appmanifest/) — campos y semántica del manifiesto; autoridad: W3C.
- [MDN: hacer instalables las PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable) — requisitos de instalación de una aplicación web progresiva; autoridad: MDN.
- [MDN: Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) — directivas de caché y su efecto; autoridad: MDN.
- [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — frescura y revalidación; autoridad: IETF.
- [NIST SP 800-142: Practical Combinatorial Testing](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias de pares y t factores; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Manifiesto](./manifiesto.md) · [Manifiesto de operabilidad →](./manifiesto-de-operabilidad.md)
