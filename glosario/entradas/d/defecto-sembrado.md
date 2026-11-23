# Defecto sembrado

[↑ Glosario](../../README.md) · [← Defecto latente](./defecto-latente.md) · [Defensa en profundidad →](./defensa-en-profundidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Error introducido a propósito para comprobar que una prueba lo detecta.

Definición de trabajo de [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

## Por qué importa

En [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), el tema «Defecto sembrado» importa porque comprueba que la prueba puede fallar.

## Cómo funciona

Según [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md):

Que las seis comprobaciones detecten los seis defectos sembrados dice que la batería *puede* detectar esas seis cosas. No dice que no haya un séptimo defecto que ninguna vea, ni que el producto sea seguro, ni que cumpla la normativa, ni que soporte la carga de producción. Un expediente honesto separa tres niveles: lo que se ejecutó y funcionó, lo que se ejecutó y es parcial, y lo que no se ejecutó. Esa separación es lo que da credibilidad a las partes que sí se probaron.

Según [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md):

El equipo de *Tablero* prepara el dossier para el comprador. Escribe siete invariantes con su prueba y su defecto sembrado, construye la matriz y la ejecuta delante del técnico del comprador. Cuando el técnico pide sembrar «uno que no esperen», quitan la restricción de unicidad de la referencia del asiento: la matriz muestra que ninguna de las seis pruebas lo ve y la conciliación diaria tarda un día en señalarlo. El equipo lo registra como un hueco, añade la prueba de referencia única y la matriz queda con la celda nueva.

## Ejemplo

Ejemplo de [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* prepara el dossier para el comprador. Escribe siete invariantes con su prueba y su defecto sembrado, construye la matriz y la ejecuta delante del técnico del comprador. Cuando el técnico pide sembrar «uno que no esperen», quitan la restricción de unicidad de la referencia del asiento: la matriz muestra que ninguna de las seis pruebas lo ve y la conciliación diaria tarda un día en señalarlo. El equipo lo registra como un hueco, añade la prueba de referencia única y la matriz queda con la celda nueva.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Fallo.** La batería de un equipo pasa con los seis defectos sembrados y falla una vez cada diez ejecuciones sin defectos. ([SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Expediente](../e/expediente.md), [Falso negativo](../f/falso-negativo.md), [Falso positivo](../f/falso-positivo.md), [Invariante](../i/invariante.md), [Matriz defecto por prueba](../m/matriz-defecto-por-prueba.md), [Red de seguridad](../r/red-de-seguridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Defecto latente](./defecto-latente.md) · [Defensa en profundidad →](./defensa-en-profundidad.md)
