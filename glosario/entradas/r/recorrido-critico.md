# Recorrido crítico

[↑ Glosario](../../README.md) · [← Reconstrucción independiente](./reconstruccion-independiente.md) · [Recorrido por saltos →](./recorrido-por-saltos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Secuencia de pasos de un usuario cuyo fallo causa un daño inaceptable para el negocio.

Definición de trabajo de [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md).

## Por qué importa

La clase donde se define, [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), existe con este propósito: la clase existe para que decidas qué recorridos completos del sistema merece la pena automatizar de extremo a extremo, que escribas criterios de aceptación ejecutables y que sepas cuánto cuesta en inestabilidad cada paso que añades.

## Cómo funciona

[SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor. Esta clase deja el cuarto artefacto: cinco recorridos críticos con criterios de aceptación y presupuesto de inestabilidad. `SE-425` explora una forma distinta de elegir casos: dejar que un generador los produzca a partir de una propiedad o de un modelo. Cambia después la probabilidad espuria de 0,5 % a 2 % y observa cuántos recorridos siguen en el presupuesto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md)) son:

- **La suite casi nunca está en verde sin cambios** — causa: demasiados pasos con fallo espurio pequeño. Corrección: calcular \((1-q)^k\) y acortar o dividir los recorridos.
- **Las instantáneas se aprueban sin leerlas** — causa: casi todas las diferencias son ruido. Corrección: aserciones semánticas y una instantánea solo para salidas pequeñas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con simulaciones y un registro sintético en Windows y Ubuntu (WSL2) con salidas idénticas. No se usó navegador ni herramienta de automatización; la inestabilidad por paso, la distribución Zipf de las rutas, los impactos y los 16 cambios de HTML son del autor. La comprobación de estilo y de accesibilidad visual queda fuera de lo medido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Daño](../d/dano.md), [Secuencia](../s/secuencia.md), [Aserción semántica](../a/asercion-semantica.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Fallo espurio](../f/fallo-espurio.md), [Instantánea](../i/instantanea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «BroadStackTest»](https://martinfowler.com/bliki/BroadStackTest.html) — pruebas de banda ancha; autoridad: autor del texto.
- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) — costo de las pruebas de extremo a extremo; autoridad: equipo de pruebas de Google.
- [Martin Fowler, «TestPyramid»](https://martinfowler.com/bliki/TestPyramid.html) — reparto por nivel; autoridad: autor del texto.
- [Playwright: buenas prácticas](https://playwright.dev/docs/best-practices) — pruebas centradas en el usuario; autoridad: documentación oficial.
- [Cucumber: referencia de Gherkin](https://cucumber.io/docs/gherkin/reference/) — criterios de aceptación; autoridad: documentación oficial.

---

[↑ Glosario](../../README.md) · [← Reconstrucción independiente](./reconstruccion-independiente.md) · [Recorrido por saltos →](./recorrido-por-saltos.md)
