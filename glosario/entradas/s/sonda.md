# Sonda

[↑ Glosario](../../README.md) · [← Solutions Architect](./solutions-architect.md) · [Sonda de actividad →](./sonda-de-actividad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Valor de entrada elegido por su capacidad de revelar defectos conocidos.

Definición de trabajo de [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md): Programa que aplica una operación con el comportamiento antiguo y el nuevo sobre datos representativos y cuenta cuántos resultados difieren.
- En [SE-599 — Taller: elegir y degradar un patrón agéntico](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md): Llamada ocasional al nivel superior para saber si ya se recuperó.

## Por qué importa

En [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md), el tema «Sondas de entrada» importa porque un validador falla ante pocos valores especiales.

## Cómo funciona

Según [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md):

Una sonda es un valor elegido por lo que suele romper: vacío, solo espacios, longitudes de borde (79, 80, 81), caracteres con tilde o combinantes, controles, texto bidireccional, emoji, cadenas que empiezan por un nombre reservado. Una lista de sondas es una lista de verificación de entradas; no sustituye a la exploración, la prepara. Contra un validador con un defecto específico, la lista dirigida lo encuentra casi siempre y cadenas aleatorias casi nunca.

Según [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md):

Antes de cada cierre de curso, el equipo de la plataforma planifica tres sesiones de 60 minutos con misiones distintas (archivos y adjuntos; sesión, zona horaria y plazo; texto y caracteres especiales) a cargo de personas que no escribieron el código. Cada sesión usa una hoja con la misión, la lista de heurísticas (límites de la especificación, repetir, deshacer, cambiar de contexto) y una sección de registro con hallazgos, preguntas y lo que no se pudo probar. La batería automática de accesibilidad corre en cada propuesta de cambio y bloquea solo las seis clases que decide una regla; una revisión manual con lector de pantalla cubre una vez por trimestre los recorridos de ingreso y de entrega.

## Ejemplo

Ejemplo de [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) (sección «Ejemplo profesional»):

Antes de cada cierre de curso, el equipo de la plataforma planifica tres sesiones de 60 minutos con misiones distintas (archivos y adjuntos; sesión, zona horaria y plazo; texto y caracteres especiales) a cargo de personas que no escribieron el código. Cada sesión usa una hoja con la misión, la lista de heurísticas (límites de la especificación, repetir, deshacer, cambiar de contexto) y una sección de registro con hallazgos, preguntas y lo que no se pudo probar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un validador acepta entradas que no debería** — causa: solo se probaron valores típicos. Corrección: lista de sondas por tipo de dato. ([SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md))
- **La suite pasa y los datos cambian** — causa: cambio silencioso no ejercitado por las pruebas. Corrección: escribir sondas con datos reales y ampliar el maestro dorado. ([SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una sonda es un valor elegido por lo que suele romper: vacío, solo espacios, longitudes de borde (79, 80, 81), caracteres con tilde o combinantes, controles, texto bidireccional, emoji, cadenas que empiezan por un nombre reservado. ([SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Operación](../o/operacion.md), [Resultado](../r/resultado.md), [Sobre](./sobre.md), [Cambio ruidoso](../c/cambio-ruidoso.md), [Cambio silencioso](../c/cambio-silencioso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-599 — Taller: elegir y degradar un patrón agéntico](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bach, «Exploratory Testing»](https://www.satisfice.com/exploratory-testing) — exploración como disciplina; autoridad: autor del texto.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — criterios de accesibilidad; autoridad: Recomendación del W3C.
- [Understanding SC 1.4.3: contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — umbrales de contraste; autoridad: W3C WAI.
- [W3C WAI: evaluar la accesibilidad web](https://www.w3.org/WAI/test-evaluate/) — herramientas y revisión manual; autoridad: W3C WAI.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — pruebas de seguridad web; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Solutions Architect](./solutions-architect.md) · [Sonda de actividad →](./sonda-de-actividad.md)
