# Dependencia alucinada

[↑ Glosario](../../README.md) · [← Dependencia](./dependencia.md) · [Dependencia atrasada →](./dependencia-atrasada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Paquete referenciado por código generado que no existe o no es el esperado.

Definición de trabajo de [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

## Por qué importa

En [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), el tema «Dependencias alucinadas» importa porque abren la cadena de suministro

## Cómo funciona

[SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica sus datos: los de estudiantes (nombre, correo, identificador, notas) no salen en ninguna forma; las credenciales no salen ni se pegan, y se rotan si se sospecha; el código propietario sale solo hacia el servicio con contrato de no retención aprobado por el área legal; el código abierto y los datos sintéticos salen libremente.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se instala un paquete que no existe o no es el esperado** — causa: dependencia alucinada. Corrección: verificar existencia, historial, licencia y fijar versión. ([SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: un escáner real sobre mensajes sintéticos con cadenas generadas al azar, una comparación real de búsqueda de texto y árbol sintáctico, y un cálculo real de huellas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Paquete](../p/paquete.md), [Escáner previo al envío](../e/escaner-previo-al-envio.md), [Huella de código](../h/huella-de-codigo.md), [Inyección indirecta de instrucciones](../i/inyeccion-indirecta-de-instrucciones.md), [Minimización de datos](../m/minimizacion-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Dependencias alucinadas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — riesgos de aplicaciones con modelos de lenguaje; autoridad: OWASP.
- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta de instrucciones; autoridad: preprint académico.
- [Perry et al., «Do Users Write More Insecure Code with AI Assistants?»](https://arxiv.org/abs/2211.03622) — código inseguro con asistente; autoridad: ACM CCS 2023.
- [Pearce et al., «Asleep at the Keyboard?»](https://arxiv.org/abs/2108.09293) — seguridad del código sugerido; autoridad: IEEE S&P 2022.
- [Spracklen et al., «We Have a Package for You!»](https://arxiv.org/abs/2406.10279) — alucinaciones de paquetes y cadena de suministro; autoridad: preprint académico.

---

[↑ Glosario](../../README.md) · [← Dependencia](./dependencia.md) · [Dependencia atrasada →](./dependencia-atrasada.md)
