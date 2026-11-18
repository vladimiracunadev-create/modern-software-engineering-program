# 🛡️ Safety-Critical Software Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Sistemas%20cr%C3%ADticos-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P04%20%C2%B7%20P12%20%C2%B7%20P13%20%C2%B7%20P22%20%C2%B7%20P30%20%C2%B7%20P31%20%C2%B7%20P32%20%C2%B7%20P40%20%C2%B7%20P47-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Traduce peligros del dominio en requisitos, arquitectura, verificación y evidencia
> capaces de sostener una afirmación de seguridad limitada y auditable.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** safety, hazards y assurance
> · **Evidencia central:** cadena peligro → requisito → control → prueba → evidencia

## 🧭 Qué es y por qué importa

En medicina, transporte, industria o aeroespacio, un fallo puede causar daño físico.
Este rol no “certifica” por intuición: define contexto, analiza hazards, diseña
controles independientes y conserva evidencia bajo el estándar aplicable.

## 🗓️ Un día en el puesto

- revisar un hazard y sus supuestos operacionales;
- convertir mitigaciones en requisitos trazables;
- analizar modos de fallo y cobertura diagnóstica;
- revisar independencia, cambios y evidencia de pruebas;
- coordinar con dominio, hardware, calidad y autoridad evaluadora.

## ✅ Responsabilidades y límites

- Responde por rigor, trazabilidad y límites de las afirmaciones de safety.
- Separa seguridad funcional de ciberseguridad y conecta ambas cuando interactúan.
- No declara conformidad sin jurisdicción, estándar y evidencia aplicables.
- No sustituye especialistas médicos, industriales o regulatorios.

## 🧠 Qué necesitas saber

Requisitos, invariantes, máquinas de estado, métodos formales, hazard analysis,
redundancia, independencia, testing basado en riesgo, configuración, cambios,
factores humanos, incidentes y ciclos de vida largos.

## 📚 Tu ruta en el programa

1. Partes 00, 04 y 10–17 para ética, modelos y trazabilidad.
2. [Parte 23 — Software especializado y dominios](../classes/part-23-software-especializado-y-dominios/README.md).
3. Partes 22 y 24–28 para tiempo real, arquitectura y fallos.
4. Partes 30–33 para verificación, resiliencia, seguridad y configuración.
5. Partes 35–37 para incidentes, retiro y liderazgo.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Hazard"] --> B
    B["🧠 Requisito"] --> C
    C["🛠️ Control"] --> D
    D["🔎 Verificación"] --> E["📈 Assurance"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🛡️ Safety-Critical Software Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Traduce peligros del dominio en requisitos, arquitectura, verificación y evidencia capaces de sostener una afirmación de seguridad limitada y auditable. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Sistemas críticos**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🔌 Embedded & IoT Engineer](embedded-iot-engineer.md); [🧾 Requirements Engineer / Business Systems Analyst](requirements-engineer.md); [⚖️ Compliance Engineer](compliance-engineer.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **senior → principal**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 04 · Pensamiento computacional y resolución de problemas](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) | desarrollada | [SE-052 · Invariantes, precondiciones y poscondiciones](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md)<br>[SE-053 · Recursión, inducción y razonamiento estructural](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md)<br>[SE-054 · Algoritmos, corrección y terminación](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)<br>[SE-057 · Modelado de estado, transiciones y eventos](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) | Profundiza **invariantes, complejidad y resolución sistemática** desde la responsabilidad del rol. | Especificación contrastable. |
| 2 | [Parte 12 · Ingeniería de requisitos](../classes/part-12-ingenieria-de-requisitos/README.md) | desarrollada | [SE-147 · Atributos de calidad y restricciones](../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)<br>[SE-151 · Trazabilidad desde necesidad hasta evidencia](../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)<br>[SE-152 · Requisitos regulatorios, de datos y seguridad](../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)<br>[SE-154 · Ambigüedad, contradicción e incompletitud](../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) | Profundiza **requisitos, restricciones y trazabilidad** desde la responsabilidad del rol. | Baseline de requisitos revisable. |
| 3 | [Parte 13 · Especificaciones, contratos y modelos](../classes/part-13-especificaciones-contratos-y-modelos/README.md) | desarrollada | [SE-157 · Especificación informal, semiformal y formal](../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)<br>[SE-159 · Contratos, invariantes y diseño por contrato](../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)<br>[SE-161 · Máquinas de estado y model checking introductorio](../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md)<br>[SE-166 · Especificaciones ejecutables y pruebas contractuales](../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) | Profundiza **contratos, modelos e invariantes verificables** desde la responsabilidad del rol. | Especificación trazable. |
| 4 | [Parte 22 · Embedded, IoT y tiempo real](../classes/part-22-embedded-iot-y-tiempo-real/README.md) | desarrollada | [SE-268 · Sistemas de tiempo real y deadlines](../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md)<br>[SE-269 · Interrupciones, concurrencia y estado compartido](../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)<br>[SE-274 · Safety, seguridad y vida útil prolongada](../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md)<br>[SE-275 · Taller: modelar fallos físicos y digitales](../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) | Profundiza **firmware, tiempo real, OTA y dispositivo** desde la responsabilidad del rol. | Sistema simulado recuperable. |
| 5 | [Parte 30 · Estrategia y técnicas de prueba](../classes/part-30-estrategia-y-tecnicas-de-prueba/README.md) | desarrollada | [SE-361 · Calidad por riesgo y propósito de las pruebas](../classes/part-30-estrategia-y-tecnicas-de-prueba/se-361-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)<br>[SE-365 · Pruebas basadas en propiedades y modelos](../classes/part-30-estrategia-y-tecnicas-de-prueba/se-365-pruebas-basadas-en-propiedades-y-modelos/README.md)<br>[SE-366 · Mutación, fuzzing y generación de casos](../classes/part-30-estrategia-y-tecnicas-de-prueba/se-366-mutacion-fuzzing-y-generacion-de-casos/README.md)<br>[SE-371 · Taller: demostrar que una prueba detecta defectos](../classes/part-30-estrategia-y-tecnicas-de-prueba/se-371-taller-demostrar-que-una-prueba-detecta-defectos/README.md) | Profundiza **estrategia de pruebas guiada por riesgo** desde la responsabilidad del rol. | Suite que demuestra detección de defectos. |
| 6 | [Parte 31 · Calidad, rendimiento y resiliencia](../classes/part-31-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-374 · Revisión, análisis estático y quality gates](../classes/part-31-calidad-rendimiento-y-resiliencia/se-374-revision-analisis-estatico-y-quality-gates/README.md)<br>[SE-378 · Timeouts, retries, backoff y jitter](../classes/part-31-calidad-rendimiento-y-resiliencia/se-378-timeouts-retries-backoff-y-jitter/README.md)<br>[SE-379 · Circuit breakers, bulkheads y degradación](../classes/part-31-calidad-rendimiento-y-resiliencia/se-379-circuit-breakers-bulkheads-y-degradacion/README.md)<br>[SE-380 · Disponibilidad, durabilidad y recuperación](../classes/part-31-calidad-rendimiento-y-resiliencia/se-380-disponibilidad-durabilidad-y-recuperacion/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 7 | [Parte 32 · Seguridad, privacidad y cumplimiento](../classes/part-32-seguridad-privacidad-y-cumplimiento/README.md) | desarrollada | [SE-385 · Principios de seguridad y modelos de amenaza](../classes/part-32-seguridad-privacidad-y-cumplimiento/se-385-principios-de-seguridad-y-modelos-de-amenaza/README.md)<br>[SE-392 · Secure SDLC, abuso y pruebas negativas](../classes/part-32-seguridad-privacidad-y-cumplimiento/se-392-secure-sdlc-abuso-y-pruebas-negativas/README.md)<br>[SE-393 · Vulnerabilidades, divulgación y respuesta](../classes/part-32-seguridad-privacidad-y-cumplimiento/se-393-vulnerabilidades-divulgacion-y-respuesta/README.md)<br>[SE-394 · Cumplimiento, evidencia y límites legales](../classes/part-32-seguridad-privacidad-y-cumplimiento/se-394-cumplimiento-evidencia-y-limites-legales/README.md) | Profundiza **seguridad, privacidad y cumplimiento** desde la responsabilidad del rol. | Controles con pruebas y evidencia. |
| 8 | [Parte 40 · Metodologías de desarrollo: de TDD a ODD](../classes/part-40-metodologias-de-desarrollo-de-tdd-a-odd/README.md) | desarrollada | [SE-481 · Mapa de metodologías: qué decide cada una y cómo elegir](../classes/part-40-metodologias-de-desarrollo-de-tdd-a-odd/se-481-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md)<br>[SE-482 · TDD: ciclo rojo-verde-refactor y diseño emergente](../classes/part-40-metodologias-de-desarrollo-de-tdd-a-odd/se-482-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md)<br>[SE-485 · ATDD y Specification by Example: aceptación ejecutable](../classes/part-40-metodologias-de-desarrollo-de-tdd-a-odd/se-485-atdd-y-specification-by-example-aceptacion-ejecutable/README.md)<br>[SE-487 · Diseño por contrato y pruebas de contrato como oráculo](../classes/part-40-metodologias-de-desarrollo-de-tdd-a-odd/se-487-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) | Profundiza **metodologías de desarrollo con evidencia de equipo** desde la responsabilidad del rol. | Política metodológica con evidencia. |
| 9 | [Parte 47 · Sistemas críticos, tiempo real y normas de seguridad](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md) | desarrollada | [SE-565 · Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-565-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md)<br>[SE-566 · IEC 61508 y niveles de integridad de seguridad](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-566-iec-61508-y-niveles-de-integridad-de-seguridad/README.md)<br>[SE-570 · Casos de seguridad y trazabilidad](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-570-casos-de-seguridad-y-trazabilidad/README.md)<br>[SE-571 · RTOS y planificación de tiempo real](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-571-rtos-y-planificacion-de-tiempo-real/README.md)<br>[SE-573 · Verificación formal y model checking: TLA+, SPARK y Alloy](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-573-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md)<br>[SE-574 · Verificación y cobertura: MC/DC, HIL y SIL](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-574-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) | Profundiza **sistemas críticos, tiempo real y normas de seguridad** desde la responsabilidad del rol. | Paquete de aseguramiento de un controlador. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes 00–48 (`SE-001`–`SE-588`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-160 · Modelos estructurales, conductuales y de información](../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) | Parte 13 |
| [SE-187 · Riesgos, supuestos, issues y decisiones](../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) | Parte 15 |
| [SE-279 · Machine learning como componente de producto](../classes/part-23-software-especializado-y-dominios/se-279-machine-learning-como-componente-de-producto/README.md) | Parte 23 |
| [SE-283 · Salud, datos sensibles y sistemas regulados](../classes/part-23-software-especializado-y-dominios/se-283-salud-datos-sensibles-y-sistemas-regulados/README.md) | Parte 23 |
| [SE-287 · Taller: comparar riesgos entre dominios](../classes/part-23-software-especializado-y-dominios/se-287-taller-comparar-riesgos-entre-dominios/README.md) | Parte 23 |
| [SE-429 · Postmortems sin culpa y aprendizaje](../classes/part-35-observabilidad-sre-e-incidentes/se-429-postmortems-sin-culpa-y-aprendizaje/README.md) | Parte 35 |
| [SE-430 · Continuidad, disaster recovery y ejercicios](../classes/part-35-observabilidad-sre-e-incidentes/se-430-continuidad-disaster-recovery-y-ejercicios/README.md) | Parte 35 |
| [SE-567 · Automoción: ISO 26262 y niveles ASIL](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-567-automocion-iso-26262-y-niveles-asil/README.md) | Parte 47 |
| [SE-568 · Aviación: DO-178C, DO-254 y ARP4754](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-568-aviacion-do-178c-do-254-y-arp4754/README.md) | Parte 47 |
| [SE-569 · Dispositivos médicos: IEC 62304](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-569-dispositivos-medicos-iec-62304/README.md) | Parte 47 |
| [SE-572 · Codificación segura: MISRA y CERT](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-572-codificacion-segura-misra-y-cert/README.md) | Parte 47 |
| [SE-582 · Contenedores, microVM y sandboxes](../classes/part-48-runtimes-y-plataformas-modernas/se-582-contenedores-microvm-y-sandboxes/README.md) | Parte 48 |
| [SE-583 · Hardware seguro: TEE y atestación](../classes/part-48-runtimes-y-plataformas-modernas/se-583-hardware-seguro-tee-y-atestacion/README.md) | Parte 48 |

**Cómo recorrerla.** Empieza por [SE-052](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) para fijar el
primer mecanismo, usa [SE-371](../classes/part-30-estrategia-y-tecnicas-de-prueba/se-371-taller-demostrar-que-una-prueba-detecta-defectos/README.md) para integrar el
centro de la especialidad y llega a [SE-574](../classes/part-47-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-574-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. Las Partes 00–48 (`SE-001`–`SE-588`) están
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

## ✅ Ampliación completada: Partes 40–48

> [!NOTE]
> Las Partes 40–48 (`SE-481`–`SE-588`) ya están desarrolladas ([ADR-004](../docs/adr/ADR-004-expand-to-540-class-scope.md) y [ADR-006](../docs/adr/ADR-006-extend-program-parts-45-48-and-roles.md)); sus clases figuran en el núcleo y en las clases de apoyo de esta guía.


## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Disponibilidad o estado seguro** | Definir qué degradación evita daño y cuál lo incrementa. | Análisis de hazards más prueba de transición. |
| **Prueba o demostración formal** | Usar rigor proporcional a criticidad y modelo disponible. | Trazabilidad de propiedades supuestos y contraejemplos. |
| **Cambio o recertificación** | Aislar impacto y conservar evidencia de configuración. | Baseline revisada y análisis de regresión. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Disponibilidad o estado seguro**, **Prueba o demostración formal**
y **Cambio o recertificación** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Sensor inconsistente activa una decisión peligrosa

**Síntoma.** Dos entradas plausibles violan un supuesto no documentado. La respuesta madura evita convertir la primera
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
2. **Investigar:** Rastrear hazard requisito invariante modelo y evidencia de prueba. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Pasar a estado seguro aislar entrada y revisar el argumento de assurance. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Cobertura de hazards** | Peligros con controles y pruebas trazables. | Contar requisitos sin severidad. |
| **Defectos de escape críticos** | Fallos que invalidan una garantía de seguridad. | Mezclar incidentes menores y catastróficos. |
| **Tiempo hasta estado seguro** | Capacidad de detectar y mitigar condición peligrosa. | Optimizar disponibilidad sobre seguridad. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Caso de assurance trazable

**Propósito:** demostrar cómo un hazard se convierte en requisito control prueba y evidencia. El resultado esperado es **modelo de estados invariantes matriz de trazabilidad pruebas negativas y revisión independiente**.

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

1. ¿En qué contexto elegirías **Disponibilidad o estado seguro** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Sensor inconsistente activa una decisión peligrosa**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Caso de assurance trazable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — **ISO**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) — **ACM**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — **IEEE Computer Society**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- análisis de hazards con contexto y límites;
- matriz trazable de requisitos, controles y pruebas;
- modelo de estado con propiedad y contraejemplo;
- caso de assurance que distingue evidencia de afirmación.

## 📈 Progresión

Software/Verification Engineer → Safety Engineer → Senior → Safety Architect/Lead.

## ⚠️ Mitos frecuentes

- “Más pruebas garantizan seguridad.” Sin modelo de riesgo no se conoce su suficiencia.
- “Cumplir un estándar elimina responsabilidad.” El contexto real sigue mandando.
- “Formal significa infalible.” Un modelo puede omitir el supuesto decisivo.

## 🚀 Siguientes pasos

1. Selecciona un caso hipotético y declara su contexto sin afirmar certificación.
2. Traza un hazard hasta una prueba y un límite residual.
3. Revisa qué cambio invalidaría la evidencia.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
