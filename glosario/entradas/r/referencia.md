# Referencia

[↑ Glosario](../../README.md) · [← Refactorización](./refactorizacion.md) · [Referencia de API →](./referencia-de-api.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

**Referencia** tiene tres sentidos en el programa. El principal ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), documentación) es una descripción completa y neutral de los elementos de un producto, estructurada como el producto. [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (Git) la usa para un nombre (rama, etiqueta, HEAD) que apunta a un commit o a otra referencia. [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) (monitoreo de modelos) la usa para la distribución con la que se compara, normalmente la de entrenamiento o la de un periodo sano. Esta entrada desarrolla los dos primeros, que son los más usados, y señala el tercero.

## Por qué importa

En documentación, distingue lo que se **consulta** de lo que se lee: la referencia describe la máquina con completitud y sin opinión. En Git, la distinción entre «existe» y «es alcanzable» es la base de toda la recuperación ([SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)): un objeto está a salvo mientras alguna referencia lo alcance.

## Cómo funciona

**Referencia documental ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md)).** Describe la máquina: los parámetros, sus tipos, sus valores por defecto, los errores que puede devolver. Se consulta de forma puntual y por eso importa más que sea completa, uniforme y exacta que agradable. Su estructura imita la del producto, no la de las tareas. Es el único tipo de documentación cuya exactitud puede comprobarse casi por completo con herramientas, porque sus afirmaciones tienen una contraparte en el código: nombres, firmas, límites; por eso se genera de la configuración o del código. Una referencia con opiniones («recomendamos un tope del 50 %») mezcla tipos: la opinión va a una guía o a una explicación.

**Referencia de Git ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md)).** Una rama, una etiqueta y HEAD son archivos pequeños con un identificador (o con el nombre de otra referencia). Mover una rama no borra objetos: solo cambia a qué commit se llega desde ese nombre. Un objeto queda a salvo mientras sea alcanzable desde alguna referencia o desde el registro de movimientos (reflog); si deja de serlo, es candidato a la poda.

**Referencia de comparación ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md)).** En monitoreo, la distribución de referencia (entrenamiento o un periodo sano) es contra la que se mide la deriva de los datos actuales.

## Ejemplo

La plataforma de entregas separa la penalización en cuatro páginas ([SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md)): tutorial, guía, explicación y una referencia, «Parámetros de penalización», que se genera de la configuración y lista cada parámetro con su tipo, valor por defecto y límites. En Git ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md)), tras `git reset --hard HEAD~1`, el commit descartado deja de ser alcanzable desde la rama, pero sigue existiendo en el reflog durante un tiempo, y con `git reflog` se localiza y se recupera con una nueva rama. (El segundo caso es un ejemplo estándar de Git.)

## Errores y confusiones comunes

- **Opinión en la referencia**: se mezcla descripción con recomendación.
- **Referencia escrita a mano que diverge del código.**
- **Creer que mover una rama borra commits**: solo cambia el puntero.
- **Confundir los tres sentidos**: la referencia documental, la de Git y la de comparación no tienen relación técnica.

## Límites y cuándo no aplica

La referencia documental no sirve para aprender (necesita tutorial) ni para decidir (necesita explicación). Las referencias de Git no impiden la pérdida: un objeto no alcanzable se poda con el tiempo, y el reflog es local, de modo que no protege a otras personas ni a clones. Y una distribución de referencia de ML se vuelve obsoleta si el mundo cambia.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Producto](../p/producto.md), [Árbol](../a/arbol.md), [Blob](../b/blob.md), [Explicación](../e/explicacion.md), [Guía práctica](../g/guia-practica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-206 — Tutoriales, how-to, referencia y explicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (190 clases más lo mencionan; las que más):

[SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md).

**Aparece en los casos de estudio:** [Instagram](../../../casos/exito/instagram.md), [TSB Bank](../../../casos/fallo/tsb.md), [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Referencias».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis: referencia](https://diataxis.fr/reference/) — descripción neutral y completa; autoridad: proyecto Diátaxis.
- [Python: `inspect`](https://docs.python.org/3/library/inspect.html) — firmas de funciones para comparar con una referencia.
- [Diátaxis](https://diataxis.fr/) — los cuatro tipos y la relación entre ellos; autoridad: proyecto Diátaxis.
- [Diátaxis: tutoriales](https://diataxis.fr/tutorials/) — qué es y qué no es un tutorial; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — guías orientadas a un objetivo; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Refactorización](./refactorizacion.md) · [Referencia de API →](./referencia-de-api.md)
