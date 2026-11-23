# 🔗 API Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Interfaces-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P13%20%C2%B7%20P17%20%C2%B7%20P20%20%C2%B7%20P26%20%C2%B7%20P31%20%C2%B7%20P35%20%C2%B7%20P38%20%C2%B7%20P43%20%C2%B7%20P45-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Diseña contratos consumibles, compatibles y operables entre equipos, sistemas y
> organizaciones, cualquiera que sea su protocolo.
>
> **Entrada habitual:** semi-senior · **Foco:** contratos, experiencia y gobernanza
> · **Evidencia central:** API versionada con consumidores y fallos contractuales probados

## 🧭 Qué es y por qué importa

Una API es una promesa de comportamiento, no una lista de endpoints. API engineering
integra semántica, modelo de dominio, seguridad, compatibilidad, documentación y
operación para que productores y consumidores evolucionen sin coordinación perfecta.

## 🗓️ Un día en el puesto

- modelar un caso de uso y elegir REST, RPC, eventos o tiempo real;
- revisar OpenAPI/AsyncAPI y ejemplos de error;
- negociar compatibilidad y deprecación con consumidores;
- analizar abuso, cuotas, latencia e idempotencia;
- observar adopción y fallos por versión.

## ✅ Responsabilidades y límites

- Responde por contrato, ergonomía, seguridad y ciclo de vida de la interfaz.
- No convierte una preferencia de protocolo en arquitectura universal.
- No versiona para evitar comprender compatibilidad.
- No publica una API sin ownership, soporte y política de retirada.

## 🧠 Qué necesitas saber

HTTP y protocolos, REST/RPC/GraphQL/gRPC, WebSockets/SSE, eventos y webhooks;
modelado, esquemas, errores, paginación, idempotencia, authn/authz, rate limiting,
contract testing, SDK, observabilidad y developer experience.

## 📚 Tu ruta en el programa

1. Partes [03](../classes/part-03-redes-internet-y-protocolos/README.md), [05](../classes/part-05-fundamentos-de-programacion/README.md)–[09](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) para red, programación y APIs internas.
2. Partes [10](../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)–[13](../classes/part-13-especificaciones-contratos-y-modelos/README.md) y [17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) para usuarios, contratos y documentación.
3. [Parte 20 — Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md).
4. Partes [27](../classes/part-27-arquitectura-de-software-y-dominio/README.md), [29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) y [31](../classes/part-31-integracion-eventos-y-mensajeria/README.md)–[32](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) para límites, datos, eventos y distribución.
5. Partes [35](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)–[36](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) y [38](../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)–[41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) para pruebas, seguridad, gateways y operación.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

![Diagrama de flujo con 5 pasos. Recorrido: «🎯 Consumidor»; luego «🧠 Contrato»; luego «🛠️ Compatibilidad»; luego «🔎 Gobierno»; luego «📈 Retiro».](../site/assets/figures/mermaid-b3ef87955a.svg)

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🔗 API Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Diseña contratos consumibles, compatibles y operables entre equipos, sistemas y organizaciones, cualquiera que sea su protocolo. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Interfaces**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [⚙️ Backend Engineer](backend-engineer.md); [✍️ Technical Writer / Documentation Engineer](technical-writer.md); [🧩 Solutions Architect](solutions-architect.md);
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
| 1 | [Parte 13 · Especificaciones, contratos y modelos](../classes/part-13-especificaciones-contratos-y-modelos/README.md) | desarrollada | [SE-159 · Contratos, invariantes y diseño por contrato](../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)<br>[SE-162 · Esquemas de datos y validación](../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md)<br>[SE-163 · OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)<br>[SE-164 · Compatibilidad, versionado y evolución de contratos](../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)<br>[SE-165 · Spec-first, spec-anchored y spec-as-source](../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md)<br>[SE-166 · Especificaciones ejecutables y pruebas contractuales](../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) | Profundiza **contratos, modelos e invariantes verificables** desde la responsabilidad del rol. | Especificación trazable. |
| 2 | [Parte 17 · Documentación y conocimiento técnico](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) | desarrollada | [SE-206 · Tutoriales, how-to, referencia y explicación](../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md)<br>[SE-208 · ADRs, RFCs y registro de decisiones](../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md)<br>[SE-210 · API docs, ejemplos y contratos publicados](../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md)<br>[SE-214 · Documentación para humanos, máquinas y LLM](../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) | Profundiza **documentación, decisiones y conocimiento operativo** desde la responsabilidad del rol. | Paquete documental probado por terceros. |
| 3 | [Parte 20 · Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) | desarrollada | [SE-242 · REST y semántica de recursos](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)<br>[SE-243 · RPC, GraphQL y selección de interfaz](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md)<br>[SE-244 · Validación, errores y contratos consistentes](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)<br>[SE-245 · Autenticación, autorización y contexto](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)<br>[SE-246 · Idempotencia, reintentos y deduplicación](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)<br>[SE-249 · Caching, rate limiting y protección](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) | Profundiza **servicios, APIs y procesamiento asíncrono** desde la responsabilidad del rol. | Servicio contractual operable. |
| 4 | [Parte 26 · Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) | desarrollada | [SE-315 · GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)<br>[SE-319 · Enterprise Integration Patterns como lenguaje común](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md)<br>[SE-320 · Resiliencia: timeout, retry con jitter y circuit breaker](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)<br>[SE-321 · Resiliencia: bulkhead, sidecar, ambassador y degradación](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) | Profundiza **patrones de diseño, empresariales y de resiliencia** desde la responsabilidad del rol. | Catálogo de patrones con su costo. |
| 5 | [Parte 31 · Integración, eventos y mensajería](../classes/part-31-integracion-eventos-y-mensajeria/README.md) | desarrollada | [SE-373 · Integración síncrona y asíncrona](../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md)<br>[SE-374 · Mensajes, eventos, comandos y documentos](../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md)<br>[SE-379 · Webhooks, polling y suscripciones](../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md)<br>[SE-380 · Compatibilidad de esquemas y registros](../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)<br>[SE-382 · Observabilidad y seguridad de integraciones](../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) | Profundiza **eventos, mensajería y compatibilidad** desde la responsabilidad del rol. | Flujo tolerante a duplicados. |
| 6 | [Parte 35 · Estrategia y técnicas de prueba](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md) | desarrollada | [SE-423 · Integración, componentes y contratos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)<br>[SE-424 · End-to-end, aceptación y recorridos críticos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md)<br>[SE-426 · Mutación, fuzzing y generación de casos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)<br>[SE-431 · Taller: demostrar que una prueba detecta defectos](../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) | Profundiza **estrategia de pruebas guiada por riesgo** desde la responsabilidad del rol. | Suite que demuestra detección de defectos. |
| 7 | [Parte 38 · Seguridad, privacidad y cumplimiento](../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md) | desarrollada | [SE-458 · Identidad, autenticación y sesiones](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md)<br>[SE-459 · Autorización, recursos y mínimo privilegio](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)<br>[SE-460 · Validación, codificación y clases de inyección](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md)<br>[SE-464 · Secure SDLC, abuso y pruebas negativas](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) | Profundiza **seguridad, privacidad y cumplimiento** desde la responsabilidad del rol. | Controles con pruebas y evidencia. |
| 8 | [Parte 43 · Mantenimiento y modernización legacy](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) | desarrollada | [SE-520 · Dependencias obsoletas y riesgo acumulado](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)<br>[SE-521 · Strangler, branch by abstraction y anticorruption](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)<br>[SE-524 · Compatibilidad, coexistencia y doble escritura](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md)<br>[SE-525 · Retiro, archivado y disposición de sistemas](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) | Profundiza **mantenimiento, modernización y retiro** desde la responsabilidad del rol. | Migración incremental reversible. |
| 9 | [Parte 45 · Metodologías de desarrollo: de TDD a ODD](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) | desarrollada | [SE-544 · BDD: ejemplos, conversación y lenguaje compartido](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md)<br>[SE-545 · ATDD y Specification by Example: aceptación ejecutable](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md)<br>[SE-547 · Diseño por contrato y pruebas de contrato como oráculo](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md)<br>[SE-548 · SDD: spec-first, spec-anchored y spec-as-source](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) | Profundiza **metodologías de desarrollo con evidencia de equipo** desde la responsabilidad del rol. | Política metodológica con evidencia. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-110 · SemVer, compatibilidad y contratos públicos](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md) | [Parte 09](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) |
| [SE-312 · Proyecto: evolución compatible de un componente](../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) | [Parte 25](../classes/part-25-diseno-patrones-y-refactorizacion/README.md) |
| [SE-354 · Migraciones compatibles y evolución de esquema](../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) | [Parte 29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) |
| [SE-409 · Qué hace distinto a un producto SaaS](../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) | [Parte 34](../classes/part-34-saas-y-plataformas-de-producto/README.md) |
| [SE-414 · Planes, derechos de uso y banderas de funcionalidad](../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) | [Parte 34](../classes/part-34-saas-y-plataformas-de-producto/README.md) |
| [SE-420 · Taller y proyecto integrador: producto SaaS mínimo con evidencia](../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) | [Parte 34](../classes/part-34-saas-y-plataformas-de-producto/README.md) |

**Cómo recorrerla.** Empieza por [SE-159](../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) para fijar el
primer mecanismo, usa [SE-373](../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) para integrar el
centro de la especialidad y llega a [SE-548](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. Las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`) están
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

## ✅ Ampliación completada: todas las partes del alcance

> [!NOTE]
> Todas las partes del alcance ya están desarrolladas ([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)); sus clases figuran en el núcleo y en las clases de apoyo de esta guía.


## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **REST RPC o eventos** | Elegir semántica por interacción acoplamiento y tooling. | Prototipo contractual y escenario de fallo. |
| **Versión nueva o evolución compatible** | Preferir cambios aditivos con deprecación observable. | Consumer contract y análisis de uso. |
| **Gateway o lógica distribuida** | Centralizar capacidades transversales sin ocultar dominio. | Políticas versionadas y trazas extremo a extremo. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **REST RPC o eventos**, **Versión nueva o evolución compatible**
y **Gateway o lógica distribuida** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Un cambio opcional rompe un consumidor generado

**Síntoma.** La forma del esquema cambió aunque el endpoint conserve URL. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

![Diagrama de flujo con 6 pasos. Recorrido: «⚠️ Síntoma»; luego «🔎 Hipótesis»; luego «🧯 Contención»; luego «🧠 Diagnóstico»; luego «🛠️ Recuperación»; luego «📚 Prevención».](../site/assets/figures/mermaid-637bdc6ac9.svg)

**Cómo leer el diagrama:** empieza en «⚠️ Síntoma» y sigue las flechas hasta el final del recorrido. Las filas se leen como una serpentina: de izquierda a derecha y, en la fila siguiente, de derecha a izquierda.

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Comparar especificaciones SDK serialización y pruebas de consumidores. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Restaurar compatibilidad publicar deprecación y añadir contract test. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Éxito por operación** | Resultado contractual no sólo código HTTP. | Agrupar errores de cliente y servidor. |
| **Adopción de versión** | Consumidores migrados antes de retiro. | Medir llamadas sin identificar dependencia. |
| **Incidentes de compatibilidad** | Rupturas causadas por cambio de contrato. | Culpar consumidores sin test previo. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: API gobernada de extremo a extremo

**Propósito:** diseñar publicar observar evolucionar y retirar un contrato consumible. El resultado esperado es **OpenAPI o AsyncAPI SDK ejemplos pruebas contractuales métricas de adopción y política de deprecación**.

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

1. ¿En qué contexto elegirías **REST RPC o eventos** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Un cambio opcional rompe un consumidor generado**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **API gobernada de extremo a extremo** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — **OpenAPI Initiative**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest) — **AsyncAPI Initiative**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — **IETF**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- contrato con casos positivos, negativos y ejemplos ejecutables;
- prueba proveedor-consumidor y detección de breaking change;
- política de versionado y deprecación aplicada;
- dashboard por operación, consumidor y versión.

## 📈 Progresión

Backend Engineer → API Engineer → Senior/Staff API → API Platform o Architect.

## ⚠️ Mitos frecuentes

- “REST es JSON sobre HTTP.” La semántica y el contrato importan más que el formato.
- “GraphQL elimina versionado.” Los cambios incompatibles siguen existiendo.
- “La documentación se genera sola.” Un esquema no explica intención ni decisiones.

## 🚀 Siguientes pasos

1. Diseña primero ejemplos y errores de un caso de uso.
2. Añade un consumidor real y rompe el contrato de forma controlada.
3. Practica deprecación, observación y retirada.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
