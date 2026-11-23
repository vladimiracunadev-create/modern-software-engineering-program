# Registro de intención

[↑ Glosario](../../README.md) · [← Registro de eventos](./registro-de-eventos.md) · [Registro de metadatos →](./registro-de-metadatos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Anotación previa de que se va a crear un recurso, que permite reconocerlo si el proceso se corta.

Definición de trabajo de [SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md).

## Por qué importa

La clase donde se define, [SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), existe con este propósito: el taller existe para que practiques lo que las clases anteriores solo describieron: crear un entorno entero, interrumpirlo, destruirlo y comprobar que no quedó nada.

## Cómo funciona

[SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. Cada herramienta y cada proveedor usan estos términos con matices y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Caso medido en la sección «Estado tras cada recurso y registro de intención» de [SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md):

Si el estado se guarda tras cada recurso, un corte entre recursos deja el estado exacto. Queda un caso: el corte entre crear el recurso y anotarlo, que deja un recurso real que el estado no conoce. Una técnica de escritura previa anota «voy a crear el recurso 7» antes de crearlo y «recurso 7 creado» después; al recuperarse, el recurso con intención y sin confirmación es un sospechoso que se comprueba contra la realidad y se adopta o se elimina. No evita el corte, hace que no sea invisible.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md)) son:

- **Un reintento falla con «ya existe»** — causa: la creación se cortó y el estado no registró lo creado. Corrección: registrar tras cada recurso y reconciliar los sospechosos.
- **La destrucción reintenta varias veces y tarda** — causa: orden equivocado con dependencias vivas. Corrección: destruir en orden topológico inverso y registrar los rechazos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada herramienta y cada proveedor usan estos términos con matices y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos con carpetas locales en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún proveedor, red, credencial ni herramienta de infraestructura: los fallos son excepciones inyectadas, el grafo de doce recursos es del autor y la cobertura de etiquetas y el costo por resto son supuestos. La siguiente clase integra todo en un proyecto: una plataforma mínima y reproducible.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Recurso](./recurso.md), [Barrido por etiqueta](../b/barrido-por-etiqueta.md), [Orden topológico inverso](../o/orden-topologico-inverso.md), [Prueba de destrucción](../p/prueba-de-destruccion.md), [Recurso huérfano](./recurso-huerfano.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-407 — Taller: desplegar y destruir un entorno seguro](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Terraform: destroy](https://developer.hashicorp.com/terraform/cli/commands/destroy) — destrucción de objetos gestionados en orden de dependencias; autoridad: documentación oficial de HashiCorp.
- [Terraform: estado](https://developer.hashicorp.com/terraform/language/state) — relación entre recursos declarados y reales; autoridad: documentación oficial de HashiCorp.
- [AWS: Tagging Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) — estrategia de etiquetas para dueño, entorno y costos; autoridad: documentación del proveedor.
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html) — directorios temporales de los experimentos; autoridad: documentación de Python.
- [Python: shutil](https://docs.python.org/3/library/shutil.html) — eliminación de árboles de archivos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Registro de eventos](./registro-de-eventos.md) · [Registro de metadatos →](./registro-de-metadatos.md)
