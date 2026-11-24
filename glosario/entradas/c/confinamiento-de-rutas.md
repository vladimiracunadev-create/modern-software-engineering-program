# Confinamiento de rutas

[↑ Glosario](../../README.md) · [← Confinamiento](./confinamiento.md) · [Confirmación →](./confirmacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

El **confinamiento de rutas** (*path confinement*) es la comprobación de que una ruta resuelta queda dentro de una carpeta permitida, tras normalizarla. [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) (firma, sandbox y seguridad del cliente) lo presenta como defensa de la debilidad CWE-22 (recorrido de rutas); [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) y [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) lo reutilizan para el agente: resolver la ruta y comprobar que queda dentro de la raíz permitida.

## Por qué importa

Cuando una aplicación construye una ruta con una entrada externa (un nombre de archivo, un parámetro de una herramienta), esa entrada puede escapar de la carpeta prevista. [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) insiste en que una ruta recibida de fuera debe normalizarse y compararse con la raíz, no filtrarse por apariencia. [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) lo llama el control más repetido y el que más se escribe mal.

## Cómo funciona

La debilidad CWE-22 consiste en construir una ruta con entrada externa sin limitarla a una carpeta. Las defensas ingenuas fallan:

- **Comprobar el prefijo:** `/datos/curso` también es prefijo de `/datos/curso-secreto`; la carpeta con nombre parecido pasa.
- **Rechazar `..`:** no cubre separadores distintos (`\` frente a `/`) ni rutas absolutas que reemplazan la base.

La defensa correcta, según [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md):

1. **Normalizar** la ruta resultante (resolver `.`, `..` y separadores).
2. **Comprobar que está dentro de la raíz usando el separador**, es decir, que la raíz seguida del separador es prefijo, o que la ruta es la propia raíz.
3. **Probar con una lista de casos** de entradas hostiles.

En un disco real, los **enlaces simbólicos** exigen una comprobación adicional: hay que resolver el destino real del enlace y comprobarlo, porque un enlace dentro de la carpeta puede apuntar fuera.

## Ejemplo

Esbozo ilustrativo en Python (no es código de la clase):

```python
from pathlib import Path

def confinar(raiz: str, pedida: str) -> Path:
    base = Path(raiz).resolve()
    destino = (base / pedida).resolve()
    if destino != base and base not in destino.parents:
        raise ValueError("ruta fuera de la raíz")
    return destino
```

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) lo aplica a los controles del agente del servicio *Avisos*: ganchos, habilidades y confinamiento de rutas, junto con la declaración del entorno donde se ejecuta.

## Errores y confusiones comunes

- **Comprobar solo el prefijo de texto**, que acepta carpetas de nombre parecido.
- **Filtrar «..» como cadena**, que ignora rutas absolutas y otros separadores.
- **Olvidar los enlaces simbólicos** en un disco real ([SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md)).
- **Creer que el confinamiento reemplaza al sandbox:** es una capa, no el aislamiento del proceso.

## Límites y cuándo no aplica

La comprobación se hace en un momento y el sistema de archivos puede cambiar después (una condición de carrera entre comprobar y usar). No protege contra lo que la propia carpeta permitida ya contiene. En la clase se probó con una lista de casos, no sobre un disco con enlaces reales; esa parte la advierte la clase como comprobación adicional.

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
