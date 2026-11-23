# Monitor

[↑ Glosario](../../README.md) · [← Mojibake](./mojibake.md) · [Monolito →](./monolito.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Comprobación automática con umbral que alerta.

Definición de trabajo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md).

## Por qué importa

En [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), el tema «Matriz falla por monitor» importa porque muestra cobertura y huecos.

## Cómo funciona

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

El ensayo simula 14 días de tráfico con lotes de 400 decisiones por hora. Un modelo de boosting se entrena una vez con 20 000 filas de referencia. Cada hora llegan 400 entradas y, 48 horas después, sus etiquetas. A las 168 horas (el día siete) se inyecta una falla que no se anuncia.

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

El equipo de *Avisos-ML* ejecuta el ensayo un martes con la persona de guardia sin aviso. La falla de unidad se inyecta a las 10:00. A las 10:02 llega el aviso de la validación de entrada a la persona de guardia, que abre el runbook, ve la rama «falla de calidad de entrada» y confirma que la tasa de lectura llega en porcentaje. A las 10:20 despliega una corrección de la conversión en el servicio y verifica en el tablero que la tasa de marcados vuelve a su banda. El incidente se cierra a las 10:45.

## Ejemplo

Ejemplo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* ejecuta el ensayo un martes con la persona de guardia sin aviso. La falla de unidad se inyecta a las 10:00. A las 10:02 llega el aviso de la validación de entrada a la persona de guardia, que abre el runbook, ve la rama «falla de calidad de entrada» y confirma que la tasa de lectura llega en porcentaje. A las 10:20 despliega una corrección de la conversión en el servicio y verifica en el tablero que la tasa de marcados vuelve a su banda. El incidente se cierra a las 10:45.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuarta: el AUC con etiquetas ve tres fallas, a las 51, 53 y 57 horas, y no ve la deriva de covariables, porque no daña; es el único monitor que ve la deriva de concepto y es el más lento. ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md))
- Inyecta en un entorno de prueba una falla de unidad y una de nulos, y registra qué monitor alerta y cuándo. ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación automática](../c/comprobacion-automatica.md), [Exposición](../e/exposicion.md), [Inyección de fallas](../i/inyeccion-de-fallas.md), [Mitigación](./mitigacion.md), [Postmortem sin culpa](../p/postmortem-sin-culpa.md), [Recuperación](../r/recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Mojibake](./mojibake.md) · [Monolito →](./monolito.md)
