# Confinamiento de rutas

[↑ Glosario](../../README.md) · [← Confinamiento](./confinamiento.md) · [Confirmación →](./confirmacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Comprobación de que una ruta resuelta queda dentro de una carpeta permitida, tras normalizarla.

Definición de trabajo de [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md): Comprobación de que una ruta resuelta queda dentro de un directorio base.
- En [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md): Resolver una ruta y comprobar que queda dentro de la raíz permitida.

## Por qué importa

En [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), el tema «Confinamiento de rutas» importa porque una ruta recibida de fuera debe normalizarse y compararse con la raíz, no filtrarse por apariencia.

En [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), el tema «Confinamiento de rutas» importa porque es el control más repetido y el que más se escribe mal.

## Cómo funciona

Según [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), en la sección «Confinamiento de rutas»:

La debilidad CWE-22 consiste en construir una ruta con entrada externa sin limitarla a una carpeta. Las defensas ingenuas (comprobar el prefijo, rechazar los dos puntos) fallan ante carpetas con nombre parecido, separadores distintos y rutas absolutas. La defensa correcta normaliza la ruta resultante y comprueba que está dentro de la raíz con el separador, y se prueba con una lista de casos. En un disco real, los enlaces simbólicos exigen una comprobación adicional del destino.

## Ejemplo

Ejemplo de [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (sección «Caso conductor»):

El servicio *Avisos* es el caso conductor de la [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md). Esta clase deja el sexto artefacto: los controles del agente —ganchos con modo de fallo, habilidades con descripciones probadas y confinamiento de rutas— y la declaración del entorno donde se ejecuta. `SE-571` examina los servidores de herramientas y recursos que el agente consume a través del protocolo MCP y qué confianza merecen. Cambia después un solo dato, el número de caídas del gancho, y observa a partir de cuántas el modo abierto deja de ser una opción razonable para tu proyecto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md)) son:

- **El cliente acepta un paquete modificado con su hash correcto** — causa: el hash viaja con el paquete y el atacante lo recalcula. Corrección: firma asimétrica con clave pública en el cliente.
- **Una ruta con dos puntos lee un archivo de configuración** — causa: se filtró por prefijo en lugar de normalizar. Corrección: normalizar y comparar con la raíz y un separador.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos ficticios en Windows y Ubuntu (WSL2) con resultados idénticos. No se firmó ningún paquete con criptografía asimétrica, no se analizó ningún binario real y las doce rutas no agotan las variantes. La siguiente clase aplica todo esto al adaptar el producto a dos plataformas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Raíz](../r/raiz.md), [Resolver](../r/resolver.md), [Ruta](../r/ruta.md), [Entorno aislado](../e/entorno-aislado.md), [Extensión](../e/extension.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md).

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

[↑ Glosario](../../README.md) · [← Confinamiento](./confinamiento.md) · [Confirmación →](./confirmacion.md)
