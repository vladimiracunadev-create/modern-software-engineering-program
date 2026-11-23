# Requisitos universales y negativos

[↑ Glosario](../../README.md) · [← Requisitos de datos](./requisitos-de-datos.md) · [Rerere →](./rerere.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Enunciados sobre todas las ejecuciones futuras («nunca», «siempre») que ninguna prueba finita puede demostrar.

Definición de trabajo de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).

## Por qué importa

En [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), el tema «Requisitos universales y negativos» importa porque «Nunca» y «siempre» no se verifican con pruebas finitas.

## Cómo funciona

Según [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), en la sección «Requisitos universales y negativos»:

«El sistema nunca perderá un borrador» es un enunciado universal sobre infinitas ejecuciones futuras; ninguna cantidad finita de pruebas puede demostrarlo. Lo que sí puede decirse es una cota: con n pruebas sin fallos, con 95 % de confianza, la tasa de fallo es menor que aproximadamente 3/n. Para decir «menos de 1 por cada 10 000» hacen falta unas 30 000 pruebas sin ningún fallo. Los requisitos universales son legítimos como intención, pero como criterio de aceptación deben convertirse en una tasa, una cota y una forma de aprender del fallo.

## Ejemplo

Caso medido en la sección «Requisitos universales y negativos» de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md):

«El sistema nunca perderá un borrador» es un enunciado universal sobre infinitas ejecuciones futuras; ninguna cantidad finita de pruebas puede demostrarlo. Lo que sí puede decirse es una cota: con n pruebas sin fallos, con 95 % de confianza, la tasa de fallo es menor que aproximadamente 3/n. Para decir «menos de 1 por cada 10 000» hacen falta unas 30 000 pruebas sin ningún fallo. Los requisitos universales son legítimos como intención, pero como criterio de aceptación deben convertirse en una tasa, una cota y una forma de aprender del fallo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)) son:

- **Se repara una frase con una cifra y nadie sabe de dónde salió** — causa: el número no tiene origen. Corrección: registrar la necesidad o la medición de la que proviene y marcarlo como hipótesis si falta.
- **La prueba pasa y las personas siguen quejándose** — causa: la reparación mide un proxy de lo que importa. Corrección: validar con personas el umbral y revisar si el proxy refleja la necesidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): el cálculo y la regla con salidas idénticas y la medición de latencia con tiempos propios de cada sistema. Las frases, las reparaciones y las etiquetas son del autor, la regla se ajustó viendo los diez primeros enunciados, el servidor es trivial y no se probó con personas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Patrones de reparación](../p/patrones-de-reparacion.md), [Procedimientos de verificación](../p/procedimientos-de-verificacion.md), [Reformulación](./reformulacion.md), [Verificabilidad](../v/verificabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — características de un buen requisito, entre ellas ser verificable; autoridad: ISO, IEC e IEEE.
- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de redacción; autoridad: IEEE International Requirements Engineering Conference.
- [Hanley y Lippman-Hand: If nothing goes wrong, is everything all right? (1983)](https://doi.org/10.1001/jama.1983.03330370053031) — regla de tres para cero fallos; autoridad: JAMA.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — objetivos con percentil, ventana y medición; autoridad: Google.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — verificación y validación de requisitos; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Requisitos de datos](./requisitos-de-datos.md) · [Rerere →](./rerere.md)
