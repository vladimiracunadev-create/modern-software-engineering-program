# 💸 FinOps Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Econom%C3%ADa-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P11%20%C2%B7%20P23%20%C2%B7%20P28%20%C2%B7%20P30%20%C2%B7%20P33%20%C2%B7%20P36%20%C2%B7%20P44%20%C2%B7%20P49%20%C2%B7%20P50-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Hace visible y accionable el coste tecnológico para que producto, ingeniería y
> finanzas decidan con contexto de valor, capacidad y riesgo.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** coste unitario y accountability
> · **Evidencia central:** modelo de coste trazable que cambia una decisión técnica

## 🧭 Qué es y por qué importa

FinOps no es recortar facturas de forma aislada. Relaciona consumo cloud, ownership,
unidad de negocio y arquitectura para optimizar valor. Una reducción que destruye
resiliencia o desplaza trabajo humano puede aumentar el coste total.

## 🗓️ Un día en el puesto

- asignar consumo a producto, equipo y ambiente;
- investigar una anomalía o recurso ocioso;
- modelar coste por transacción, cliente o capacidad;
- evaluar compromiso, elasticidad y build-vs-buy;
- negociar una acción con ingeniería, finanzas y producto.

## ✅ Responsabilidades y límites

- Responde por datos, modelos, guardrails y facilitación de decisiones.
- Expone incertidumbre, amortización y coste de oportunidad.
- No optimiza sólo la factura del proveedor.
- No usa rankings de coste para castigar equipos sin contexto.

## 🧠 Qué necesitas saber

TCO, CAPEX/OPEX, facturación cloud, tags y allocation, costes fijos/variables,
unit economics, forecast, capacidad, compromiso, anomalías, arquitectura,
observabilidad, sostenibilidad y comunicación financiera.

## 📚 Tu ruta en el programa

1. Partes 00 y 10, seguidas por [Parte 11 — Economía, métricas y decisiones de producto](../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md).
2. Partes 15 y 27–33 para estimación, arquitectura y cloud.
3. Partes 36, 40–41 para capacidad, plataforma y operación.
4. Partes 43–44 y 46 para vida útil, liderazgo y coste de IA.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Valor"] --> B
    B["🧠 Consumo"] --> C
    C["🛠️ Asignación"] --> D
    D["🔎 Decisión"] --> E["📈 Seguimiento"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **💸 FinOps Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Hace visible y accionable el coste tecnológico para que producto, ingeniería y finanzas decidan con contexto de valor, capacidad y riesgo. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Economía**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [☁️ Cloud Engineer](cloud-engineer.md); [🧭 Technical Product Engineer](technical-product-engineer.md); [🧭 CTO / Dirección de Tecnología](cto.md);
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

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 11 · Economía, métricas y decisiones de producto](../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) | desarrollada | [SE-134 · Costos de construcción, operación y oportunidad](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md)<br>[SE-135 · Resultados, outputs, actividad y vanity metrics](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)<br>[SE-140 · FinOps de producto y costo por resultado](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)<br>[SE-141 · Portafolio, opciones y secuenciación de inversión](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md)<br>[SE-142 · Decisiones reversibles e irreversibles](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md)<br>[SE-144 · Proyecto: caso de viabilidad técnico-económica](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) | Profundiza **economía, métricas y experimentación** desde la responsabilidad del rol. | Caso económico con sensibilidad. |
| 2 | [Parte 23 · Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | desarrollada | [SE-278 · WebAssembly en servidor y borde: component model](../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md)<br>[SE-280 · GPU y aceleradores: modelo de ejecución](../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)<br>[SE-281 · Rendimiento y costo en aceleradores](../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)<br>[SE-282 · Contenedores, microVM y sandboxes](../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) | Profundiza **runtimes, aislamiento, aceleradores y confianza** desde la responsabilidad del rol. | Plataforma de ejecución aislada con evidencia. |
| 3 | [Parte 28 · Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | desarrollada | [SE-340 · Microservicios y sus costes reales](../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)<br>[SE-342 · Multi-tenancy y aislamiento](../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md)<br>[SE-344 · Arquitectura celular y radio de impacto](../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md)<br>[SE-346 · Evolución y migración entre estilos](../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) | Profundiza **estilos arquitectónicos y sus fuerzas de calidad** desde la responsabilidad del rol. | Decisión arquitectónica defendida con ADR. |
| 4 | [Parte 30 · Ingeniería de datos y plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) | desarrollada | [SE-362 · Ingesta batch y streaming](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md)<br>[SE-368 · Warehouse, lake, lakehouse y formatos columnares](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md)<br>[SE-369 · Gobierno, privacidad y retención de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md)<br>[SE-370 · Costos y operación de plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) | Profundiza **plataformas de datos, calidad, contratos y gobierno** desde la responsabilidad del rol. | Plataforma de datos mínima gobernada. |
| 5 | [Parte 33 · Cloud, plataforma e infraestructura](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) | desarrollada | [SE-397 · IaaS, PaaS, SaaS y responsabilidad compartida](../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)<br>[SE-400 · Serverless y ejecución gestionada](../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md)<br>[SE-403 · Entornos, cuentas y separación de responsabilidades](../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)<br>[SE-404 · Escalado, capacidad y costos](../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md)<br>[SE-405 · Multi-cloud, híbrido y portabilidad real](../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) | Profundiza **cloud, infraestructura y plataformas** desde la responsabilidad del rol. | Entorno reproducible y eliminable. |
| 6 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-435 · Carga, estrés, picos y endurance](../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)<br>[SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-437 · Perfiles, benchmarks y errores de medición](../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)<br>[SE-440 · Disponibilidad, durabilidad y recuperación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 7 | [Parte 44 · Gestión, liderazgo y práctica profesional](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) | desarrollada | [SE-534 · Gestión de riesgos y decisiones ejecutivas](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md)<br>[SE-535 · Compras, proveedores y evaluación técnica](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md)<br>[SE-536 · Propiedad intelectual, contratos y ética](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md)<br>[SE-537 · Economía del software y costo total](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) | Profundiza **liderazgo, organización y decisiones** desde la responsabilidad del rol. | Propuesta defendida ante conflicto. |
| 8 | [Parte 49 · Patrones agénticos y sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md) | desarrollada | [SE-589 · Workflows frente a agentes: cuándo no usar un agente](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md)<br>[SE-597 · Evals y LLMOps de sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md)<br>[SE-598 · Costo, latencia y seguridad en sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md)<br>[SE-600 · Proyecto: sistema con LLM evaluado y operable](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) | Profundiza **patrones agénticos, evaluación y operación de sistemas con LLM** desde la responsabilidad del rol. | Sistema con LLM evaluado y operable. |
| 9 | [Parte 50 · Machine learning en producción y MLOps](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) | desarrollada | [SE-603 · Experimentos y entrenamiento reproducible](../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md)<br>[SE-605 · Ajuste fino, adaptación y costo](../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md)<br>[SE-606 · Servir modelos: latencia, lotes y GPU](../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)<br>[SE-608 · Monitoreo, deriva y reentrenamiento](../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) | Profundiza **machine learning en producción, MLOps y gobierno de IA** desde la responsabilidad del rol. | Sistema de ML operable con evidencia. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes 00–33, 35–41 y 43–50 (`SE-001`–`SE-408`, `SE-421`–`SE-504` y `SE-517`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-022 · Rendimiento, consumo energético y límites físicos](../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) | Parte 01 |
| [SE-133 · Modelos de negocio y sostenibilidad](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) | Parte 11 |
| [SE-143 · Taller: diseñar un árbol de métricas](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) | Parte 11 |
| [SE-495 · Métricas, dimensiones y cardinalidad](../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) | Parte 41 |
| [SE-561 · Evals de exactitud, utilidad, costo y latencia](../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) | Parte 46 |

**Cómo recorrerla.** Empieza por [SE-134](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) para fijar el
primer mecanismo, usa [SE-400](../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) para integrar el
centro de la especialidad y llega a [SE-608](../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. Las Partes 00–33, 35–41 y 43–50 (`SE-001`–`SE-408`, `SE-421`–`SE-504` y `SE-517`–`SE-612`) están
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

## 🔭 Ampliación planificada: Partes 34 y 42 (sin clases publicadas)

> [!NOTE]
> Las Partes 34 y 42 (`SE-409`–`SE-420` y `SE-505`–`SE-516`) están **planificadas**; sus números están reservados desde el 23 de
> noviembre de 2026 ([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)). Todavía no
> tienen clases ni README, por lo que no se enlazan aquí y ninguna de sus clases debe
> considerarse disponible.

| Parte planificada | Rango previsto | Qué cambiará para este rol |
| --- | --- | --- |
| **Parte 34 · SaaS y plataformas de producto** | `SE-409`–`SE-420` | Medirá el costo de servir por tenant y lo conectará con planes, precios y márgenes mediante economía unitaria. |

Hasta que esas partes se publiquen, el rol se apoya en el núcleo y en las clases
desarrolladas de arriba. La planificación indica hacia dónde crecerá la ruta; no es
evidencia de que el contenido exista ni de que su alcance final coincida con esta
descripción.

## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Ahorro o resiliencia** | Reducir desperdicio sin erosionar SLO ni opciones de recuperación. | Coste unitario más riesgo. |
| **Reservar o mantener elasticidad** | Comparar demanda incertidumbre compromiso y salida. | Escenarios de sensibilidad. |
| **Showback o chargeback** | Elegir incentivo que mejora decisiones sin castigar equipos. | Calidad de etiquetas y comportamiento observado. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Ahorro o resiliencia**, **Reservar o mantener elasticidad**
y **Showback o chargeback** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Factura sube mientras el tráfico permanece estable

**Síntoma.** Un cambio de arquitectura altera transferencia retención o unidad de cómputo. La respuesta madura evita convertir la primera
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
2. **Investigar:** Descomponer precio uso volumen compromiso y resultado. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Contener anomalía preservar servicio y presentar opciones con sensibilidad. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Costo por unidad útil** | Gasto asociado a transacción cliente o capacidad. | Usar coste total sin denominador. |
| **Cobertura de asignación** | Consumo atribuible a propietario y producto. | Forzar etiquetas sin corregir shared cost. |
| **Forecast y desviación** | Capacidad de anticipar demanda y explicar cambio. | Premiar exactitud falsa. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Caso económico operable

**Propósito:** vincular telemetría técnica con coste valor riesgo y decisión reversible. El resultado esperado es **modelo unitario dashboard forecast anomalías alternativas ADR y plan de seguimiento**.

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

1. ¿En qué contexto elegirías **Ahorro o resiliencia** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Factura sube mientras el tráfico permanece estable**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Caso económico operable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [Software Carbon Intensity Specification](https://greensoftware.foundation/standards/sci/) — **Green Software Foundation**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/) — **Google Cloud**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — **ISO**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- modelo de allocation y coste unitario;
- forecast con escenarios y sensibilidad;
- caso build-vs-buy con TCO y riesgo;
- acción de optimización con impacto en coste, SLO y carbono.

## 📈 Progresión

Cloud/Finance/Data Analyst → FinOps Engineer → Senior FinOps Practitioner/Lead.

## ⚠️ Mitos frecuentes

- “FinOps es apagar recursos.” También decide arquitectura y demanda.
- “Reservar siempre ahorra.” Añade riesgo si la carga cambia.
- “Coste menor es mejor.” El objetivo es valor sostenible, no mínimo absoluto.

## 🚀 Siguientes pasos

1. Define una unidad de valor antes del dashboard.
2. Explica una factura desde recurso hasta producto.
3. Propón una acción y mide efectos en SLO y trabajo humano.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
