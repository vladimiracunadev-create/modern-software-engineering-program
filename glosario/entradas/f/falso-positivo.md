# Falso positivo

[↑ Glosario](../../README.md) · [← Falso pase](./falso-pase.md) · [Falso positivo de la puerta →](./falso-positivo-de-la-puerta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Un **falso positivo** es un aviso que una herramienta emite sobre código (o sistema) que no tiene el defecto que dice detectar ([SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md)). En [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) el sentido es el de pruebas: una prueba que falla sin que haya un defecto. En ambos casos, la señal dice «hay un problema» cuando no lo hay.

## Por qué importa

Una herramienta con muchos falsos positivos deja de ser creíble: la gente ignora sus avisos o la desactiva, y con ellos se pierde el aviso verdadero. [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) lo dice así: una batería que falla con defectos y también con el producto limpio no sirve. La decisión que cambia es cómo se evalúa una herramienta o una prueba: no solo si detecta defectos, sino si guarda silencio cuando no los hay.

## Cómo funciona

Una batería de pruebas se valida con dos ejecuciones opuestas. Con **defectos sembrados**, debe fallar (si no, no detecta). Con el producto **limpio**, debe dar cero fallos de forma estable, repetida y en entornos distintos. Si falla sin defecto, es un falso positivo.

[SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) da el procedimiento: en el taller se repitió la ejecución completa tres veces con salida idéntica; si una prueba depende del orden, del reloj o de la velocidad de la máquina, se convierte en una prueba inestable y se corrige antes de confiar en ella. La clase enumera las causas habituales: el reloj, el orden de ejecución, datos compartidos entre pruebas y la velocidad de la máquina. El tratamiento es investigar antes de continuar, aislar, corregir y repetir la ejecución limpia varias veces.

En el análisis estático ([SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), sistemas críticos), el falso positivo es el aviso que la herramienta emite sobre código correcto. Cada uno cuesta tiempo de revisión y, si se acumulan, entrena a quien revisa a descartar avisos sin leerlos. El mecanismo de fondo es el compromiso entre sensibilidad y especificidad: una herramienta más sensible encuentra más defectos y emite más avisos falsos.

## Ejemplo

Una prueba de plazos falla de vez en cuando porque usa el reloj real: cerca de medianoche el resultado cambia. Con el producto limpio, la batería da rojo algunas veces; es un falso positivo. Se aísla fijando un reloj controlado y se repite la ejecución limpia varias veces hasta que sale estable. Es el tratamiento de [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

## Errores y confusiones comunes

- **Desactivar la prueba o ignorar el aviso sin investigar**: se pierde la señal verdadera.
- **Confundirlo con un defecto menor**: un falso positivo no es un defecto.
- **Medir solo detección**: sin ejecutar con el producto limpio no se ve.
- **Culpar a la herramienta sin comprobar**: algunos avisos «falsos» son defectos reales poco evidentes.

## Límites y cuándo no aplica

Un número cero de falsos positivos no es alcanzable en general: reducirlos suele costar detecciones. Lo que se exige es que sean pocos, conocidos y tratables. La definición cambia con el contexto: en pruebas es un fallo sin defecto, en análisis estático un aviso sobre código correcto, y en un sistema crítico el costo de un falso negativo puede justificar tolerar más falsos positivos.

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
