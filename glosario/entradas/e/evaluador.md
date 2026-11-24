# Evaluador

[↑ Glosario](../../README.md) · [← Evaluación sumativa](./evaluacion-sumativa.md) · [Evasión →](./evasion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Un **evaluador** es el componente que juzga un resultado y devuelve las fallas concretas ([SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md)). En el patrón generador-evaluador, un generador produce, el evaluador revisa y devuelve *qué falló*, y el generador corrige.

## Por qué importa

Convierte una puerta de «pasa o no pasa» en un bucle de mejora. Pero un evaluador es una fuente de verdad solo en la medida de su acierto: un resultado general de la clase.

## Cómo funciona

Funciona cuando hay un criterio de evaluación claro y la iteración mejora el resultado. En el experimento de [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), el aviso tiene cuatro restricciones comprobables y el generador sintético corrige cada falla señalada con probabilidad 0,80 y estropea con 0,03 lo que estaba bien; sin revisión pasan el 35,5 %. El diagnóstico de la clase muestra qué ocurre con un evaluador malo: un modelo juez acepta «URGENTE» si la fecha es correcta y ordena cambios en lo que estaba bien, y el generador oscila (las vueltas por aviso suben de 1,6 a 3,4). El verificador programático detecta el tono en el 100 % de los casos.

## Ejemplo

Para criterios comprobables por código (formato, tono, fecha) conviene un verificador programático; el modelo juez se reserva para lo que el código no decide.

## Errores y confusiones comunes

Usar un juez sin medir su acierto; permitir que el evaluador ordene cambios sobre lo que estaba bien.

## Límites y cuándo no aplica

Sin criterio claro, la iteración no converge. El número de vueltas necesita una condición de parada.

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
