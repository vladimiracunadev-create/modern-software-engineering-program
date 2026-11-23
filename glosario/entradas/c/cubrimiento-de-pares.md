# Cubrimiento de pares

[↑ Glosario](../../README.md) · [← Cubo de fichas](./cubo-de-fichas.md) · [Cuello de botella →](./cuello-de-botella.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Conjunto de configuraciones en el que todo par de parámetros aparece en todas sus combinaciones.

Definición de trabajo de [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md).

## Por qué importa

La clase donde se define, [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), existe con este propósito: la clase existe para que separes dos decisiones que el despliegue tradicional ata:

## Cómo funciona

[SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md):

El equipo de la API de entregas define una política: cada bandera tiene tipo, propietario, fecha de caducidad y valor por defecto ante fallo; las de lanzamiento caducan a los 30 días. La evaluación es local, determinista, con la bandera como sal y el identificador de usuario como contexto, y el sistema de reglas está detrás de una interfaz neutral para poder cambiar de proveedor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md)) son:

- **La misma persona ve cosas distintas** — causa: azar por petición. Corrección: huella determinista del identificador.
- **Dos experimentos se confunden** — causa: misma huella sin sal. Corrección: usar la bandera como sal.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron cuatro experimentos con usuarios sintéticos y SHA-256 real, idénticos en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](./combinacion.md), [Conjunto](./conjunto.md), [Parámetro](../p/parametro.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Deuda de banderas](../d/deuda-de-banderas.md), [Huella de segmentación](../h/huella-de-segmentacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Feature Toggles»](https://martinfowler.com/articles/feature-toggles.html) — tipos y costos de las banderas; autoridad: autor del texto.
- [OpenFeature: especificación](https://openfeature.dev/specification/) — interfaz neutral de evaluación; autoridad: proyecto OpenFeature, CNCF.
- [Trunk Based Development: banderas](https://trunkbaseddevelopment.com/feature-flags/) — integración continua con código oculto; autoridad: sitio de referencia de la práctica.
- [NIST SP 800-142](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias; autoridad: NIST.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — funciones hash; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Cubo de fichas](./cubo-de-fichas.md) · [Cuello de botella →](./cuello-de-botella.md)
