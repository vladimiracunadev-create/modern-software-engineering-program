# Autorización a nivel de objeto

[↑ Glosario](../../README.md) · [← Autorización](./autorizacion.md) · [Autorización, captura, liquidación →](./autorizacion-captura-liquidacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Comprobación, en cada acceso, de que el sujeto tiene la relación requerida con el recurso concreto que pide.

Definición de trabajo de [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md): Comprobación de que el sujeto tiene derecho sobre la instancia concreta que pide.

## Por qué importa

En [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), el tema «Autorización a nivel de objeto» importa porque es el defecto más frecuente de las API y no lo ve una prueba por roles.

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

- **Prerrequisito:** las clases previas [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Derecho](../d/derecho.md), [Instancia](../i/instancia.md), [Recurso](../r/recurso.md), [Relación](../r/relacion.md), [Audiencia](./audiencia.md), [Autenticación](./autenticacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

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

[↑ Glosario](../../README.md) · [← Autorización](./autorizacion.md) · [Autorización, captura, liquidación →](./autorizacion-captura-liquidacion.md)
