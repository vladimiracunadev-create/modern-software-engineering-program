# ♿ Accessibility Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Inclusi%C3%B3n-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20lead-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P10%20%C2%B7%20P12%20%C2%B7%20P14%20%C2%B7%20P19%20%C2%B7%20P21%20%C2%B7%20P35%20%C2%B7%20P36%20%C2%B7%20P40-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Integra accesibilidad en diseño, código, contenido, pruebas y operación para que
> personas con distintas capacidades puedan completar tareas reales.
>
> **Entrada habitual:** semi-senior · **Foco:** inclusión y calidad de interacción
> · **Evidencia central:** flujo probado con herramientas automáticas y uso manual

## 🧭 Qué es y por qué importa

Accessibility engineering convierte principios y WCAG en decisiones concretas de
semántica, navegación, contenido y componentes. No es una auditoría al final: evita
barreras desde requisitos y diseño y comprueba la experiencia con más de una técnica.

## 🗓️ Un día en el puesto

- revisar un flujo con teclado y lector de pantalla;
- diagnosticar nombre, rol, foco, contraste o anuncio incorrecto;
- asesorar diseño y componentes compartidos;
- combinar pruebas automáticas, manuales y con usuarios;
- priorizar barreras por impacto y prevenir regresiones.

## ✅ Responsabilidades y límites

- Responde por criterios, habilitación y evidencia de accesibilidad.
- Involucra personas con discapacidad sin convertirlas en único mecanismo de QA.
- No declara conformidad por pasar una herramienta automática.
- No reduce accesibilidad a color, ARIA o cumplimiento legal.

## 🧠 Qué necesitas saber

HTML semántico, accesibilidad de plataformas, teclado, foco, lectores de pantalla,
contraste, zoom, movimiento, contenido, formularios, multimedia, WCAG, inclusive
design, testing manual/automático y gestión de defectos.

## 📚 Tu ruta en el programa

1. Partes 00, 10–13 para ética, usuarios y requisitos.
2. [Parte 14 — Experiencia, accesibilidad e i18n](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md).
3. Partes 19 y 21 para web y clientes.
4. Partes 35–36 y 38 para estrategia de prueba, calidad y cumplimiento.
5. Partes 40 y 44 para gates y cambio organizacional.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Tarea"] --> B
    B["🧠 Barrera"] --> C
    C["🛠️ Patrón accesible"] --> D
    D["🔎 Prueba"] --> E["📈 Prevención"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **♿ Accessibility Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Integra accesibilidad en diseño, código, contenido, pruebas y operación para que personas con distintas capacidades puedan completar tareas reales. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Inclusión**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🎨 Frontend Engineer](frontend-engineer.md); [🧪 QA / Test Automation Engineer](qa-test-engineer.md); [✍️ Technical Writer / Documentation Engineer](technical-writer.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **semi-senior → lead**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 10 · Descubrimiento y estrategia de producto](../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) | desarrollada | [SE-122 · Usuarios, actores, trabajos y contextos](../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md)<br>[SE-123 · Investigación, entrevistas y evidencia cualitativa](../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md)<br>[SE-127 · Prototipos, experimentos y reducción de incertidumbre](../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)<br>[SE-129 · Ética del descubrimiento y protección de participantes](../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) | Profundiza **discovery, usuarios, hipótesis y valor** desde la responsabilidad del rol. | Dossier de problema y decisión. |
| 2 | [Parte 12 · Ingeniería de requisitos](../classes/part-12-ingenieria-de-requisitos/README.md) | desarrollada | [SE-147 · Atributos de calidad y restricciones](../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)<br>[SE-149 · Criterios de aceptación y ejemplos](../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)<br>[SE-151 · Trazabilidad desde necesidad hasta evidencia](../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)<br>[SE-154 · Ambigüedad, contradicción e incompletitud](../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) | Profundiza **requisitos, restricciones y trazabilidad** desde la responsabilidad del rol. | Baseline de requisitos revisable. |
| 3 | [Parte 14 · Experiencia, accesibilidad e internacionalización](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md) | desarrollada | [SE-172 · Estados vacíos, carga, error y recuperación](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md)<br>[SE-173 · Accesibilidad perceptible, operable y comprensible](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)<br>[SE-174 · Semántica, teclado, foco y tecnologías de asistencia](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md)<br>[SE-175 · Diseño visual, tipografía, color y contraste](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md)<br>[SE-176 · Responsive, adaptativo y preferencias del usuario](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md)<br>[SE-179 · Taller: auditar y reparar un flujo excluyente](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) | Profundiza **experiencia, accesibilidad e internacionalización** desde la responsabilidad del rol. | Flujo inclusivo evaluado. |
| 4 | [Parte 19 · Web, frontend y aplicaciones progresivas](../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md) | desarrollada | [SE-229 · Plataforma web, HTML semántico y CSS](../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md)<br>[SE-233 · Formularios, validación y experiencia de error](../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md)<br>[SE-234 · Navegación, routing y URLs durables](../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md)<br>[SE-239 · Taller: construir un flujo web resiliente](../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md)<br>[SE-240 · Proyecto: aplicación web accesible y offline](../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) | Profundiza **plataforma web, estado y experiencia cliente** desde la responsabilidad del rol. | Aplicación accesible y observable. |
| 5 | [Parte 21 · Software móvil, escritorio y multiplataforma](../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) | desarrollada | [SE-257 · Permisos, sensores y capacidades del dispositivo](../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md)<br>[SE-258 · Interacción táctil, teclado, mouse y accesibilidad](../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md)<br>[SE-263 · Taller: adaptar un producto a dos plataformas](../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md)<br>[SE-264 · Proyecto: cliente multiplataforma con sincronización](../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) | Profundiza **clientes, sincronización y distribución** desde la responsabilidad del rol. | Cliente offline con actualización segura. |
| 6 | [Parte 35 · Estrategia y técnicas de prueba](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md) | desarrollada | [SE-424 · End-to-end, aceptación y recorridos críticos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md)<br>[SE-429 · Pruebas exploratorias y sesiones](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)<br>[SE-430 · Flakiness, diagnóstico y mantenimiento](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)<br>[SE-431 · Taller: demostrar que una prueba detecta defectos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) | Profundiza **estrategia de pruebas guiada por riesgo** desde la responsabilidad del rol. | Suite que demuestra detección de defectos. |
| 7 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-433 · Modelos de calidad y atributos medibles](../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)<br>[SE-441 · Compatibilidad, portabilidad e interoperabilidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)<br>[SE-442 · Calidad de experiencia y presupuestos](../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md)<br>[SE-444 · Proyecto: informe reproducible de calidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 8 | [Parte 40 · CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) | desarrollada | [SE-481 · Integración continua y feedback temprano](../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md)<br>[SE-482 · Pipelines, jobs, matrices y cachés](../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md)<br>[SE-483 · Tests, seguridad y políticas como gates](../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md)<br>[SE-488 · Entornos preview y datos seguros](../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) | Profundiza **CI/CD, IaC, plataforma y DevEx** desde la responsabilidad del rol. | Camino autoservicio con rollback. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes 00–33, 35–41 y 43–50 (`SE-001`–`SE-408`, `SE-421`–`SE-504` y `SE-517`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-106 · Ergonomía, accesibilidad y productividad del entorno](../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md) | Parte 08 |
| [SE-169 · Diseño centrado en personas y tareas](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) | Parte 14 |
| [SE-170 · Arquitectura de información y navegación](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) | Parte 14 |
| [SE-171 · Interacción, affordances y retroalimentación](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) | Parte 14 |
| [SE-178 · Investigación de usabilidad y medición](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md) | Parte 14 |
| [SE-221 · TUI, terminales y accesibilidad](../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) | Parte 18 |
| [SE-544 · BDD: ejemplos, conversación y lenguaje compartido](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) | Parte 45 |
| [SE-545 · ATDD y Specification by Example: aceptación ejecutable](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) | Parte 45 |

**Cómo recorrerla.** Empieza por [SE-122](../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) para fijar el
primer mecanismo, usa [SE-239](../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) para integrar el
centro de la especialidad y llega a [SE-488](../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) cuando ya
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
| — | — | Las partes que este rol esperaba ya están desarrolladas y figuran en el núcleo o en las clases de apoyo. |

Hasta que esas partes se publiquen, el rol se apoya en el núcleo y en las clases
desarrolladas de arriba. La planificación indica hacia dónde crecerá la ruta; no es
evidencia de que el contenido exista ni de que su alcance final coincida con esta
descripción.

## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Semántica nativa o ARIA** | Usar el mecanismo más interoperable y simple. | Matriz navegador tecnología asistiva. |
| **Automático o manual** | Combinar detección rápida con evaluación de tarea y comprensión. | Evidencia de teclado lector zoom y contraste. |
| **Conformidad o usabilidad** | Cumplir criterios sin perder el objetivo real de la persona. | Prueba de tarea con barreras priorizadas. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Semántica nativa o ARIA**, **Automático o manual**
y **Conformidad o usabilidad** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Un modal visible deja el foco detrás y atrapa a un lector

**Síntoma.** La implementación cambia apariencia sin gestionar nombre foco y retorno. La respuesta madura evita convertir la primera
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
2. **Investigar:** Recorrer DOM árbol accesible teclado anuncios y cierre. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Restaurar semántica probar variantes y convertir la solución en patrón. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Éxito de tarea asistida** | Personas que completan el flujo con distintas técnicas. | Contar issues cerrados. |
| **Regresiones por componente** | Barreras reintroducidas en patrones compartidos. | Medir páginas y no sistema de diseño. |
| **Tiempo de remediación** | Velocidad desde barrera confirmada hasta solución verificada. | Cerrar tickets sin revalidación. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Flujo inclusivo verificable

**Propósito:** reparar una tarea completa y prevenir la misma barrera en el sistema de diseño. El resultado esperado es **auditoría priorizada componente accesible pruebas manuales automatizadas y guía de adopción**.

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

1. ¿En qué contexto elegirías **Semántica nativa o ARIA** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Un modal visible deja el foco detrás y atrapa a un lector**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Flujo inclusivo verificable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — **W3C**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — **ISO**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) — **ACM**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- mapa de tareas, barreras, impacto y criterio de aceptación;
- flujo operable con teclado y lector de pantalla;
- pruebas automáticas y manuales con sus límites;
- patrón accesible documentado y prueba de regresión.

## 📈 Progresión

Frontend/QA/UX → Accessibility Engineer → Senior/Lead Accessibility o Inclusive Design.

## ⚠️ Mitos frecuentes

- “Un scanner cubre accesibilidad.” No evalúa comprensión ni recorrido completo.
- “ARIA arregla HTML.” La semántica nativa suele ser más robusta.
- “Es un grupo pequeño.” Las barreras cambian con contexto y situación.

## 🚀 Siguientes pasos

1. Selecciona una tarea completa, no componentes aislados.
2. Pruébala con teclado, zoom y lector de pantalla.
3. Convierte el defecto en patrón y regresión automatizada cuando proceda.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
