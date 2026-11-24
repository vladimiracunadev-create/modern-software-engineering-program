# Sonda

[↑ Glosario](../../README.md) · [← Solutions Architect](./solutions-architect.md) · [Sonda de actividad →](./sonda-de-actividad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

En el programa, una **sonda** es un valor de entrada elegido por su capacidad de revelar defectos conocidos. Es la definición de trabajo de [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md), en estrategia de pruebas. El término tiene otros dos sentidos, que conviene no mezclar: en [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) es un programa que aplica una operación con el comportamiento antiguo y el nuevo sobre datos representativos y cuenta cuántos resultados difieren; en [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) es una llamada ocasional al nivel superior para saber si ya se recuperó (como en un cortacircuitos semiabierto). Esta entrada desarrolla el de [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) y relaciona los otros.

## Por qué importa

Los valores «típicos» casi nunca fallan. Los defectos viven en los bordes y en los rarezas: la cadena vacía, el espacio, la longitud límite. Elegir sondas con criterio cambia la eficiencia de una batería de pruebas: una lista dirigida encuentra defectos específicos casi siempre, y cadenas aleatorias casi nunca ([SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)).

## Cómo funciona

Una sonda se elige por lo que suele romper. [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) da la lista:

- vacío y solo espacios;
- longitudes de borde (79, 80, 81 si el límite es 80);
- caracteres con tilde o combinantes;
- caracteres de control;
- texto bidireccional;
- emoji;
- cadenas que empiezan por un nombre reservado.

Una lista de sondas es una **lista de verificación de entradas**: no sustituye a la exploración, la prepara. La causa de su eficacia es que codifica experiencia sobre *clases* de fallo (los límites, las codificaciones), de modo que cada tipo de dato tiene su propia lista.

En el sentido de [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), la sonda es una herramienta de migración: aplica el comportamiento antiguo y el nuevo sobre datos representativos y cuenta cuántos resultados difieren, para encontrar cambios silenciosos. Y en [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md) es la llamada de prueba que decide si el sistema se recuperó.

## Ejemplo

Un validador de nombres de usuario acepta hasta 80 caracteres. La lista de sondas: `""`, `" "`, una cadena de 79, 80 y 81 caracteres, `"é"` en forma compuesta y descompuesta, `"‮"` (control bidireccional), un emoji, y `"con"` (nombre reservado en Windows). Un validador con el defecto `<= 80` escrito como `< 80` falla con la sonda de 80. Ninguna cadena aleatoria de 1 a 600 caracteres lo encontraría con probabilidad razonable. El código es ilustración del criterio de [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md).

## Errores y confusiones comunes

- **Un validador acepta entradas que no debería.** Solo se probaron valores típicos ([SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)); corrección: lista de sondas por tipo de dato.
- **La suite pasa y los datos cambian.** Un cambio silencioso no fue ejercitado por las pruebas ([SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md)); escribir sondas con datos reales y ampliar el maestro dorado.
- **Tomar la lista como completa.** Es un punto de partida; la exploración añade lo no previsto.
- **Confundir los tres sentidos.** Ver la definición.

## Límites y cuándo no aplica

Las sondas encuentran lo que ya se sabe que suele romper; un defecto de una clase nueva no aparece en la lista. Dependen del tipo de dato: sondas de texto no sirven para fechas ni archivos. La sonda de migración ([SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md)) solo cubre los datos representativos que se le den. Y una sonda no es una especificación: dice que un valor revela algo, no cuál es el comportamiento correcto; eso lo decide el oráculo.

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
