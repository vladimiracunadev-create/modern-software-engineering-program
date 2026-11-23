# Heurística de prueba

[↑ Glosario](../../README.md) · [← Heurística](./heuristica.md) · [Híbrido →](./hibrido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Regla práctica que orienta qué entradas o acciones probar.

Definición de trabajo de [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md).

## Por qué importa

La clase donde se define, [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md), existe con este propósito: la clase existe para que explores un sistema con criterio (misiones acotadas, sondas de entrada, heurísticas) donde ninguna prueba escrita llega, y para que sepas qué partes de la accesibilidad y de la seguridad decide una regla automática y cuáles exigen a una persona.

## Cómo funciona

[SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md):

Antes de cada cierre de curso, el equipo de la plataforma planifica tres sesiones de 60 minutos con misiones distintas (archivos y adjuntos; sesión, zona horaria y plazo; texto y caracteres especiales) a cargo de personas que no escribieron el código. Cada sesión usa una hoja con la misión, la lista de heurísticas (límites de la especificación, repetir, deshacer, cambiar de contexto) y una sección de registro con hallazgos, preguntas y lo que no se pudo probar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)) son:

- **«Exploramos» y nadie sabe qué se hizo** — causa: sin misión ni registro. Corrección: misión acotada y notas de sesión.
- **La herramienta de accesibilidad pasa y una persona no puede usar la página** — causa: solo se probó lo que una regla decide. Corrección: revisión manual con tecnologías de apoyo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con agentes simulados, páginas sintéticas y validadores escritos por el autor en Windows y Ubuntu (WSL2) con salidas idénticas. No se midió a ninguna persona exploradora, no se evaluó una página real con tecnologías de apoyo y no se hizo una prueba de seguridad; el explorador heurístico y la lista de sondas conocían los límites de la especificación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Práctica](../p/practica.md), [Regla](../r/regla.md), [Exploración](../e/exploracion.md), [Misión](../m/mision.md), [Relación de contraste](../r/relacion-de-contraste.md), [Sonda](../s/sonda.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-429 — Pruebas exploratorias y sesiones](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

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

[↑ Glosario](../../README.md) · [← Heurística](./heuristica.md) · [Híbrido →](./hibrido.md)
