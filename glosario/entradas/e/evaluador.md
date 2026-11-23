# Evaluador

[↑ Glosario](../../README.md) · [← Evaluación sumativa](./evaluacion-sumativa.md) · [Evasión →](./evasion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Componente que juzga un resultado y devuelve las fallas concretas.

Definición de trabajo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md).

## Por qué importa

En [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), el tema «Evaluador exacto» importa porque devuelve fallas que el generador sabe corregir.

## Cómo funciona

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

El patrón añade un bucle: un generador produce, un evaluador revisa y devuelve **qué falló**, y el generador corrige. Es una puerta (`SE-590`) con retroalimentación. Funciona cuando hay un criterio de evaluación claro y la iteración mejora el resultado. En el experimento, el aviso tiene cuatro restricciones comprobables y el generador sintético corrige cada falla señalada con probabilidad 0,80 y estropea con 0,03 lo que estaba bien. Sin revisión, pasan el 35,5 %. Con un evaluador **programático** que ve exactamente las fallas, una vuelta lleva al 77,3 %, dos al 92,8 % y tres al 97,9 %, con 1,92 generaciones por aviso. El rendimiento marginal decrece: cada vuelta corrige una fracción de lo que queda.

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

**Diagnóstico paso a paso.** (1) Se mide el número de vueltas por aviso: sube de 1,6 a 3,4. (2) Se revisa el evaluador: es un modelo juez que acepta «URGENTE» si la fecha es correcta. (3) Se compara con el verificador programático: detecta el tono en el 100 % de los casos. (4) Se identifica que el juez deja pasar lo que debía corregir y que ordena cambios en lo que estaba bien, de modo que el generador oscila.

## Ejemplo

Ejemplo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sección «Caso conductor»):

El repaso semanal de entregas de *Avisos* se vuelve orquestador-trabajadores y la redacción de los avisos, evaluador-optimizador con verificador. En `SE-592` se estudiará el bucle del agente que sigue cuando el trabajo no se puede dividir de antemano y, en `SE-597`, cómo se evalúan estos componentes con puertas estadísticas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es un resultado general: un evaluador es una fuente de verdad solo en la medida de su acierto. ([SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Resultado](../r/resultado.md), [LPT](../l/lpt.md), [Orquestador](../o/orquestador.md), [Síntesis](../s/sintesis.md), [Tope de vueltas](../t/tope-de-vueltas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Evaluación sumativa](./evaluacion-sumativa.md) · [Evasión →](./evasion.md)
