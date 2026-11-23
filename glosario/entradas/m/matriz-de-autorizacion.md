# Matriz de autorización

[↑ Glosario](../../README.md) · [← Matriz](./matriz.md) · [Matriz de compatibilidad →](./matriz-de-compatibilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Enumeración de combinaciones de rol, acción, relación con el recurso y estado, cada una con su resultado esperado.

Definición de trabajo de [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md).

## Por qué importa

La clase donde se define, [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), existe con este propósito: la clase existe para que puedas afirmar, con una prueba y no con una impresión, que una persona autenticada solo puede hacer lo que le corresponde sobre los recursos que le corresponden.

## Cómo funciona

[SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md):

El equipo extrae la política a un módulo con una función `decide(sujeto, acción, recurso, contexto)` y hace que todos los endpoints la invoquen antes de tocar datos; un linter de la revisión de cambios rechaza endpoints con un parámetro de identificador que no llamen a la función. Genera la matriz desde la política (seis roles, siete acciones, cinco relaciones, cuatro estados), la ejecuta en cada cambio y mantiene una lista de mutantes conocidos que la suite debe matar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)) son:

- **Un estudiante lee la entrega de otro** — causa: se comprueba el rol y no el dueño. Corrección: autorización por objeto en cada endpoint con identificador.
- **Las pruebas pasan y el defecto existe** — causa: solo hay casos permitidos. Corrección: matriz con relación, estado y entradas del cliente.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se probó ningún sistema ajeno ni se usó ninguna herramienta de pruebas de seguridad; la política, los trece defectos, las dimensiones de la matriz, la fracción de identificadores filtrados y la tasa de cambios de rol son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Enumeración](../e/enumeracion.md), [Estado](../e/estado.md), [Recurso](../r/recurso.md), [Autorización](../a/autorizacion.md), [Autorización a nivel de objeto](../a/autorizacion-a-nivel-de-objeto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP API Security Top 10 2023: API1](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/) — autorización a nivel de objeto; autoridad: OWASP.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — denegar por defecto, mínimo privilegio y pruebas; autoridad: OWASP.
- [NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) — control de acceso basado en atributos; autoridad: NIST.
- [Sandhu et al., 1996](https://doi.org/10.1109/2.485845) — modelos de control de acceso por roles; autoridad: IEEE Computer.
- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — principios de diseño de la protección; autoridad: Proceedings of the IEEE.

---

[↑ Glosario](../../README.md) · [← Matriz](./matriz.md) · [Matriz de compatibilidad →](./matriz-de-compatibilidad.md)
