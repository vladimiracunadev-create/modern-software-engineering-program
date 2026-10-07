# 🧰 Developer Experience Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Plataforma-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P08%20%C2%B7%20P09%20%C2%B7%20P34%20%C2%B7%20P37-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Reduce fricción cognitiva y tiempo de feedback mediante herramientas, flujos y
> documentación diseñados a partir de evidencia de quienes desarrollan.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** tooling, onboarding y feedback
> · **Evidencia central:** mejora medida de una tarea de desarrollo real

## 🧭 Qué es y por qué importa

Developer Experience no es “hacer feliz” sin restricciones. Estudia cómo una persona
descubre, configura, comprende, cambia y valida software; luego elimina esperas y
ambigüedad sin esconder decisiones críticas ni imponer métricas dañinas.

## 🗓️ Un día en el puesto

- observar onboarding o una tarea frecuente;
- analizar tiempos de build, test y revisión;
- diseñar CLI, plantilla, SDK o documentación;
- probar el flujo con usuarios no autores;
- medir adopción, satisfacción y regresiones.

## ✅ Responsabilidades y límites

- Responde por problemas de experiencia definidos y medidos.
- Distingue percepción, productividad, calidad y outcome.
- No usa DORA o SPACE para evaluar individuos.
- No automatiza una mala política sin cuestionarla.

## 🧠 Qué necesitas saber

Investigación de usuarios, CLI/SDK, build y test, CI, documentación, arquitectura de
información, plataformas internas, telemetría ética, accesibilidad, cognitive load,
DORA, SPACE, experimentación y gestión del cambio.

## 📚 Tu ruta en el programa

1. Partes 08–10 para herramientas y discovery.
2. Partes 14 y 16–18 para inclusión, colaboración y automatización.
3. Partes 29 y 33, [Parte 34 — CI/CD, IaC y platform engineering](../classes/part-34-ci-cd-iac-y-platform-engineering/README.md) y Parte 35 para cloud, supply chain, platform y feedback.
4. Parte 37 para organización; partes 38–39 para herramientas con agentes.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Fricción"] --> B
    B["🧠 Hipótesis"] --> C
    C["🛠️ Herramienta"] --> D
    D["🔎 Feedback"] --> E["📈 Adopción"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🧰 Developer Experience Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Reduce fricción cognitiva y tiempo de feedback mediante herramientas, flujos y documentación diseñados a partir de evidencia de quienes desarrollan. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Plataforma**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🛤️ Platform Engineer](platform-engineer.md); [✍️ Technical Writer / Documentation Engineer](technical-writer.md); [👥 Engineering Manager](engineering-manager.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **semi-senior → principal**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- |
| 1 | [Parte 08 · Entornos, herramientas y depuración](../classes/part-08-entornos-herramientas-y-depuracion/README.md) | [SE-097 · Editores, IDE y servidores de lenguaje](../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)<br>[SE-104 · Dev Containers y entornos desechables](../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md)<br>[SE-106 · Ergonomía, accesibilidad y productividad del entorno](../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md) | Profundiza **depuración, profiling y reproducción de fallos** desde la responsabilidad del rol. | Expediente de causa raíz. |
| 2 | [Parte 09 · Bibliotecas, paquetes, SDK y automatización](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) | [SE-113 · CLI, flags, configuración y códigos de salida](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md)<br>[SE-118 · Diseño de experiencia para desarrolladores](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md)<br>[SE-120 · Proyecto: SDK y CLI con compatibilidad verificada](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) | Profundiza **paquetes, SDK, dependencias y compatibilidad** desde la responsabilidad del rol. | Paquete versionado y consumible. |
| 3 | [Parte 34 · CI/CD, IaC y platform engineering](../classes/part-34-ci-cd-iac-y-platform-engineering/README.md) | [SE-409 · Integración continua y feedback temprano](../classes/part-34-ci-cd-iac-y-platform-engineering/se-409-integracion-continua-y-feedback-temprano/README.md)<br>[SE-417 · Developer portals y capacidades de plataforma](../classes/part-34-ci-cd-iac-y-platform-engineering/se-417-developer-portals-y-capacidades-de-plataforma/README.md)<br>[SE-418 · Métricas DORA y mejora sin gaming](../classes/part-34-ci-cd-iac-y-platform-engineering/se-418-metricas-dora-y-mejora-sin-gaming/README.md) | Profundiza **CI/CD, IaC, plataforma y DevEx** desde la responsabilidad del rol. | Camino autoservicio con rollback. |
| 4 | [Parte 37 · Gestión, liderazgo y práctica profesional](../classes/part-37-gestion-liderazgo-y-practica-profesional/README.md) | [SE-446 · Diseño de equipos y ownership](../classes/part-37-gestion-liderazgo-y-practica-profesional/se-446-diseno-de-equipos-y-ownership/README.md)<br>[SE-448 · Mentoría, feedback y crecimiento](../classes/part-37-gestion-liderazgo-y-practica-profesional/se-448-mentoria-feedback-y-crecimiento/README.md)<br>[SE-455 · Taller: conducir una revisión de decisión difícil](../classes/part-37-gestion-liderazgo-y-practica-profesional/se-455-taller-conducir-una-revision-de-decision-dificil/README.md) | Profundiza **liderazgo, organización y decisiones** desde la responsabilidad del rol. | Propuesta defendida ante conflicto. |

**Cómo recorrerla.** Empieza por [SE-097](../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md) para fijar el
primer mecanismo, usa [SE-409](../classes/part-34-ci-cd-iac-y-platform-engineering/se-409-integracion-continua-y-feedback-temprano/README.md) para integrar el
centro de la especialidad y llega a [SE-455](../classes/part-37-gestion-liderazgo-y-practica-profesional/se-455-taller-conducir-una-revision-de-decision-dificil/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo previsto. Las Partes 00–05 están desarrolladas; las
> posteriores conservan borradores o estructuras que deben superar revisión
> cualitativa. Esta ruta no declara terminadas esas clases ni reemplaza el
> [roadmap](../ROADMAP.md).

## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Automatizar o enseñar** | Eliminar trabajo accidental sin ocultar modelos que se deben comprender. | Observación de onboarding y soporte. |
| **Velocidad o comprensión** | Acortar feedback conservando diagnóstico accionable. | Tiempo hasta causa no sólo hasta rojo. |
| **Uniformidad o autonomía** | Estandarizar interfaces y seguridad dejando decisiones de dominio. | Encuesta cualitativa más datos de uso. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Automatizar o enseñar**, **Velocidad o comprensión**
y **Uniformidad o autonomía** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Una plantilla acelera el inicio pero produce servicios imposibles de depurar

**Síntoma.** El camino feliz omitió telemetría y límites operativos. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

```mermaid
flowchart LR
    S["⚠️ Síntoma"] --> H["🔎 Hipótesis"]
    H --> C["🧯 Contención"]
    C --> D["🧠 Diagnóstico"]
    D --> R["🛠️ Recuperación"]
    R --> P["📚 Prevención"]
```

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Observar uso real configuración errores feedback y handoff. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Corregir golden path migrar consumidores y medir comprensión. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Tiempo hasta primer cambio** | Capacidad de contribuir con contexto mínimo. | Medir sólo clon a build. |
| **Tiempo de feedback** | Duración hasta señal accionable en edición y CI. | Hacer checks rápidos pero inútiles. |
| **Interrupciones de soporte** | Fricción no resuelta por autoservicio y documentación. | Convertir menos tickets en objetivo aislado. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Experiencia de desarrollo medible

**Propósito:** reducir una fricción real desde investigación hasta adopción sostenible. El resultado esperado es **journey map baseline prototipo herramienta documentación experimento métricas SPACE/DORA con límites**.

Entrega un expediente revisable con estas piezas:

1. **Contexto y alcance:** usuario, sistema, restricción, supuestos, fuera de alcance y
   criterio de no éxito.
2. **Decisión:** al menos dos alternativas reales, trade-offs, coste de reversión y un
   ADR o memo que indique cuándo revisar la elección.
3. **Artefacto principal:** una implementación, modelo, flujo o política coherente con
   las clases núcleo; no una captura aislada ni una presentación sin mecanismo.
4. **Fallo controlado:** introduce una condición adversa relacionada con el escenario
   anterior y conserva el resultado observado, sin inventar una ejecución.
5. **Verificación:** prueba, rúbrica, revisión o medición que pueda fallar y que conecte
   directamente con el resultado profesional.
6. **Operación y salida:** telemetría, recuperación, mantenimiento, deprecación o retiro
   según corresponda; incluye límites y deuda residual.

**Criterio de aceptación:** otra persona puede reconstruir el razonamiento, reproducir
la comprobación y distinguir claramente qué quedó demostrado de lo que sólo se propone.
El proyecto no se aprueba por cantidad de archivos ni por utilizar una marca concreta.

## 📈 Dominio esperado por alcance

| Alcance | Qué resuelve | Qué evidencia su autonomía |
| --- | --- | --- |
| **Inicial** | ejecuta una tarea acotada con criterios y acompañamiento | reproduce el caso, pregunta por supuestos y entrega evidencia legible |
| **Intermedio** | decide dentro de un componente o flujo conocido | compara alternativas, prueba fallos previsibles y coordina dependencias |
| **Senior** | conduce problemas ambiguos que cruzan sistemas o equipos | hace explícito el riesgo, diseña recuperación y mejora el mecanismo de trabajo |
| **Staff / Lead** | cambia capacidades compartidas y decisiones de largo plazo | multiplica criterio, define guardrails, mide adopción y conserva opciones futuras |

Progresar no significa alejarse de la práctica. Significa aumentar ambigüedad, horizonte,
blast radius y responsabilidad por consecuencias. La persona senior todavía debe poder
explicar el mecanismo; la persona Staff además crea condiciones para que otros lo
operen sin depender de ella.

## 🗓️ Plan de práctica 30 · 60 · 90 días

- **Días 1–30 — comprender y reproducir.** Estudia las primeras clases de cada parte,
  reproduce un caso pequeño y escribe un mapa de responsabilidades. El entregable es
  una baseline con preguntas abiertas, no una transformación prematura.
- **Días 31–60 — intervenir y fallar con control.** Construye el artefacto central,
  introduce el escenario de fallo y mide el comportamiento. Revisa el trabajo con una
  persona de una ruta vecina para descubrir supuestos de frontera.
- **Días 61–90 — operar y transferir.** Ejecuta recuperación, corrige la causa, publica
  runbook o guía de uso y presenta la decisión con trade-offs. Termina con una
  retrospectiva que separe resultado, evidencia, límites y siguiente inversión.

Este plan es una secuencia de práctica, no una promesa de empleabilidad en noventa días.
La experiencia previa, el dominio y el acceso a sistemas reales cambian el tiempo
necesario.

## 🎤 Preguntas para revisión o entrevista

1. ¿En qué contexto elegirías **Automatizar o enseñar** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Una plantilla acelera el inicio pero produce servicios imposibles de depurar**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Experiencia de desarrollo medible** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/) — **Google Cloud**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Development Container Specification](https://containers.dev/implementors/spec/) — **Dev Container Specification maintainers**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — **IEEE Computer Society**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- estudio de una tarea con baseline cualitativo y cuantitativo;
- herramienta o golden path probado por usuarios;
- medición antes/después con límites y efectos secundarios;
- plan de adopción, soporte y deprecación.

## 📈 Progresión

Developer/Tooling Engineer → DevEx Engineer → Senior/Staff DevEx o Platform Product Lead.

## ⚠️ Mitos frecuentes

- “DevEx es comprar herramientas.” La integración y el flujo determinan el valor.
- “Menos pasos siempre es mejor.” Algunos controles hacen visible un riesgo necesario.
- “Adopción obligatoria demuestra éxito.” Puede ocultar rechazo y workarounds.

## 🚀 Siguientes pasos

1. Observa una tarea completa antes de proponer solución.
2. Mide espera, errores y carga cognitiva con privacidad.
3. Prueba un cambio pequeño y conserva una salida reversible.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
