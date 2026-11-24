# Aserción

[↑ Glosario](../../README.md) · [← Artefacto inmutable](./artefacto-inmutable.md) · [Aserción semántica →](./asercion-semantica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Una **aserción** es la comprobación en ejecución de un supuesto del programa ([SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md)): una condición que el código declara cierta en un punto y que se verifica al llegar a él.

## Por qué importa

Convierte un supuesto silencioso en un fallo inmediato y localizado. En sistemas críticos, [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) recoge las reglas de Holzmann, diez reglas que caben en una página, escritas para que una herramienta las compruebe; una de ellas pide un mínimo de aserciones por función.

## Cómo funciona

La aserción documenta una precondición, una postcondición o un invariante y falla de forma ruidosa cuando se viola, en lugar de dejar que el dato corrupto se propague. Funciona junto con otras reglas del estándar: flujo de control simple (sin saltos arbitrarios ni recursión), bucles con una cota fija comprobable, funciones que caben en una página y comprobación del valor de retorno de lo que puede fallar. La causa de su utilidad es que acorta la distancia entre el defecto y su síntoma.

## Ejemplo

```python
def promedio(notas):
    assert len(notas) > 0, "promedio requiere al menos una nota"
    resultado = sum(notas) / len(notas)
    assert 0 <= resultado <= 7
    return resultado
```

## Errores y confusiones comunes

Usar aserciones para validar entradas externas (esas se validan con errores normales: las aserciones pueden desactivarse); poner efectos secundarios dentro de la condición.

## Límites y cuándo no aplica

[SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) aclara que las ideas (cotas, comprobación de retornos, aserciones, sin excepciones vacías) se trasladan a otros lenguajes, mientras que las reglas de C sobre punteros o preprocesador no. En Python, ejecutar con optimización elimina las sentencias `assert`, así que no deben ser la única defensa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Supuestos](../s/supuestos.md), [Cota de bucle](../c/cota-de-bucle.md), [Desviación](../d/desviacion.md), [Envoltorio de enteros](../e/envoltorio-de-enteros.md), [Estándar de codificación segura](../e/estandar-de-codificacion-segura.md), [Falso positivo](../f/falso-positivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-452 — Codificación segura: MISRA y CERT](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (30 clases más lo mencionan; las que más):

[SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Artefacto inmutable](./artefacto-inmutable.md) · [Aserción semántica →](./asercion-semantica.md)
