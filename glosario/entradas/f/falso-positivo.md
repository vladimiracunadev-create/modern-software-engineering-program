# Falso positivo

[↑ Glosario](../../README.md) · [← Falso pase](./falso-pase.md) · [Falso positivo de la puerta →](./falso-positivo-de-la-puerta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Aviso que la herramienta emite sobre código que no tiene el defecto.

Definición de trabajo de [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md): Prueba que falla sin que haya un defecto.

## Por qué importa

En [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), el tema «Falsos positivos» importa porque una regla mal ajustada pierde credibilidad.

## Cómo funciona

Según [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md):

Una batería que falla con defectos y también con el producto limpio (falsos positivos) no sirve: se ignora o se desactiva. La ejecución sin defectos debe dar cero fallos de forma estable, repetida y en entornos distintos. En el taller se repitió la ejecución completa tres veces con salida idéntica; si una prueba depende del orden, del reloj o de la velocidad de la máquina, se convierte en una prueba inestable y se corrige antes de confiar en ella.

Según [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md):

Es un falso positivo: se investiga antes de continuar. Casi siempre depende del reloj, del orden de ejecución, de datos compartidos entre pruebas o de la velocidad de la máquina. Se aísla, se corrige y se repite la ejecución limpia varias veces.

## Ejemplo

Ejemplo de [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) (sección «Preguntas frecuentes»):

Es un falso positivo: se investiga antes de continuar. Casi siempre depende del reloj, del orden de ejecución, de datos compartidos entre pruebas o de la velocidad de la máquina. Se aísla, se corrige y se repite la ejecución limpia varias veces.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una batería que falla con defectos y también con el producto limpio (falsos positivos) no sirve: se ignora o se desactiva. ([SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Sobre](../s/sobre.md), [Aserción](../a/asercion.md), [Cota de bucle](../c/cota-de-bucle.md), [Defecto sembrado](../d/defecto-sembrado.md), [Desviación](../d/desviacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (54 clases más lo mencionan; las que más):

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Falsos positivos».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Falso pase](./falso-pase.md) · [Falso positivo de la puerta →](./falso-positivo-de-la-puerta.md)
