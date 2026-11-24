# Confinamiento

[↑ Glosario](../../README.md) · [← Configuración y precedencia](./configuracion-y-precedencia.md) · [Confinamiento de rutas →](./confinamiento-de-rutas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

El **confinamiento** restringe las rutas (o la región) que un agente puede tocar: la limitación de lo que una operación puede tocar a una región resuelta, como un directorio o un dominio ([SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md)).

## Por qué importa

Acota el daño que un agente puede hacer con sus herramientas. Es un control barato y exacto en lo que cubre, pero no cubre todo, y la diferencia importa.

## Cómo funciona

El confinamiento por rutas **resuelve** cada ruta que el agente quiere leer o escribir (siguiendo `..` y enlaces simbólicos) y la compara con la raíz permitida. En el laboratorio de [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), bloquea dos de las cinco acciones (el borrado con `../home/config.txt` y la escritura con una ruta absoluta) y deja los dos archivos «personales» intactos. No cubre un proceso hijo lanzado con una herramienta permitida: ese proceso no pasa por la comprobación de rutas.

## Ejemplo

```python
from pathlib import Path
raiz = Path("/proyecto").resolve()
def permitido(ruta):
    return Path(ruta).resolve().is_relative_to(raiz)
```

Resolver antes de comparar evita que `../` o un enlace escapen de la raíz.

## Errores y confusiones comunes

Comparar texto sin resolver la ruta; creer que el confinamiento por rutas aísla procesos.

## Límites y cuándo no aplica

Un contenedor lo cubre y lo supera para procesos hijos y red: [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) explica que el confinamiento es un control del arnés que decide qué *llamadas* acepta, y el contenedor decide qué puede *ocurrir*; se complementan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Dominio](../d/dominio.md), [Operación](../o/operacion.md), [Región](../r/region.md), [Aislamiento del sistema operativo](../a/aislamiento-del-sistema-operativo.md), [Alcance](../a/alcance.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder](https://doi.org/10.1109/PROC.1975.9939) — mínimo privilegio y protección de la información; autoridad: Proceedings of the IEEE, 1975.
- [Claude Code: permisos](https://code.claude.com/docs/en/permissions) — orden de evaluación, órdenes compuestas y fragilidad de los patrones sobre argumentos; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red a nivel del sistema operativo; autoridad: documentación de Anthropic.
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/) — riesgos, entre ellos la agencia excesiva; autoridad: proyecto OWASP GenAI.

---

[↑ Glosario](../../README.md) · [← Configuración y precedencia](./configuracion-y-precedencia.md) · [Confinamiento de rutas →](./confinamiento-de-rutas.md)
