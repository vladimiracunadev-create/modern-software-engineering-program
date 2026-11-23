# Inyección indirecta de instrucciones

[↑ Glosario](../../README.md) · [← Inyección indirecta](./inyeccion-indirecta.md) · [Inyección por expansión →](./inyeccion-por-expansion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Ataque en que contenido externo recuperado por una aplicación contiene órdenes que alteran su comportamiento.

Definición de trabajo de [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md): Alteración del comportamiento de un modelo por instrucciones contenidas en datos externos que este procesa.

## Por qué importa

La clase donde se define, [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), existe con este propósito: la clase existe para que veas los tres riesgos que acompañan a todo flujo con asistente y que ninguna medida de exactitud captura: lo que sale de tu entorno (datos personales, secretos y código propietario que viajan en el contexto), lo que entra con una procedencia incierta (código cuya licencia y origen nadie conoce) y lo que entra con un defecto de seguridad que parece correcto.

## Cómo funciona

[SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica sus datos: los de estudiantes (nombre, correo, identificador, notas) no salen en ninguna forma; las credenciales no salen ni se pegan, y se rotan si se sospecha; el código propietario sale solo hacia el servicio con contrato de no retención aprobado por el área legal; el código abierto y los datos sintéticos salen libremente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md)) son:

- **Se pegan trazas con datos de estudiantes** — causa: la política depende de la memoria. Corrección: filtro previo y datos sintéticos por defecto.
- **El escáner no ve una credencial** — causa: ángulo ciego de una regla. Corrección: combinar patrones, entropía y contexto.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: un escáner real sobre mensajes sintéticos con cadenas generadas al azar, una comparación real de búsqueda de texto y árbol sintáctico, y un cálculo real de huellas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instrucción](./instruccion.md), [Modelo](../m/modelo.md), [Agente en cuarentena](../a/agente-en-cuarentena.md), [Cadena de huellas](../c/cadena-de-huellas.md), [Contenido no confiable](../c/contenido-no-confiable.md), [Dependencia alucinada](../d/dependencia-alucinada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-562 — Privacidad, propiedad intelectual y código inseguro](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta de instrucciones; autoridad: preprint académico.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — riesgos de aplicaciones con modelos de lenguaje; autoridad: OWASP.
- [Perry et al., «Do Users Write More Insecure Code with AI Assistants?»](https://arxiv.org/abs/2211.03622) — código inseguro con asistente; autoridad: ACM CCS 2023.
- [Pearce et al., «Asleep at the Keyboard?»](https://arxiv.org/abs/2108.09293) — seguridad del código sugerido; autoridad: IEEE S&P 2022.
- [Spracklen et al., «We Have a Package for You!»](https://arxiv.org/abs/2406.10279) — alucinaciones de paquetes y cadena de suministro; autoridad: preprint académico.

---

[↑ Glosario](../../README.md) · [← Inyección indirecta](./inyeccion-indirecta.md) · [Inyección por expansión →](./inyeccion-por-expansion.md)
