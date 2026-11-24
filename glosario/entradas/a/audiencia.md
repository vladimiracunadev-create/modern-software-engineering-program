# Audiencia

[↑ Glosario](../../README.md) · [← AUC](./auc.md) · [Autenticación →](./autenticacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

En el programa, **audiencia** es un grupo de personas descrito por lo que sabe, lo que quiere conseguir y el tiempo del que dispone al leer; no es un cargo ni una etiqueta de rol. Es el sentido de [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), de documentación. En seguridad, el mismo término tiene otro sentido, el del campo *audience* de una credencial: el destinatario para el que un token es válido ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)). Esta entrada desarrolla el primero y señala el segundo para no confundirlos.

## Por qué importa

Una audiencia mal definida produce documentación que nadie termina. Define el vocabulario, el nivel de detalle y lo que se puede dar por sabido: un mismo hecho se escribe distinto para cada grupo. En el sentido de seguridad, comprobar la audiencia decide si una API acepta un token emitido para otro servicio.

## Cómo funciona

Según [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), «docente» es un cargo; «docente que debe mover un plazo antes de que termine el día, sin haber leído nunca el manual» es una audiencia. La diferencia fija decisiones concretas: si se puede usar «prórroga» sin definirla, si el primer párrafo da la respuesta o el contexto, si hay capturas o comandos. La audiencia se descubre preguntando a personas reales; cuando no es posible, se escribe como hipótesis y se marca como tal.

En el sentido de seguridad, el mecanismo es una comprobación. [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) indica que verificar un token exige varias cosas: algoritmo esperado, firma contra la clave del emisor, emisor y audiencia propios de esta API, y hora entre `nbf` y `exp`. Si la audiencia no se comprueba, un token legítimo emitido para otra API funciona aquí.

## Ejemplo

El portal documental de la plataforma de entregas ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md)) mantiene un inventario de tareas por audiencia en `audiencias.md`: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga), secretaría (exportar el acta) y mantenimiento (depurar el cálculo). La regla vive una sola vez en `politica/penalizacion.md`; las cuatro vistas la enlazan con una frase de contexto. Cuando el tope cambia al 30 %, es un solo commit en la fuente y una lista señala las cuatro vistas por revisar.

## Errores y confusiones comunes

- **Una página explica todo y nadie la termina.** Mezcla audiencias y tareas; corrección: separar por audiencia o tarea y enlazar lo común ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md)).
- **Definir la audiencia por cargo.** El cargo no dice qué sabe ni cuánto tiempo tiene.
- **Copiar la regla en cada vista.** Genera versiones divergentes; mejor una fuente y vistas que la enlazan.
- **Un token para otro receptor funciona.** No se comprueba la audiencia ([SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)); corrección: exigir la audiencia propia y el emisor.

## Límites y cuándo no aplica

La audiencia documental, cuando no se pudo preguntar a personas reales, es una hipótesis y debe marcarse así; nada garantiza que describa a quien realmente lee. Y no toda documentación necesita varias audiencias: un README mínimo de una herramienta personal puede tener una sola. En seguridad, la audiencia es una comprobación necesaria pero no suficiente: no sustituye verificar firma, emisor y vigencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Token](../t/token.md), [Autenticación](./autenticacion.md), [Autorización](./autorizacion.md), [Autorización a nivel de objeto](./autorizacion-a-nivel-de-objeto.md), [Denegación por defecto](../d/denegacion-por-defecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Spotify](../../../casos/exito/spotify.md), [Instagram](../../../casos/exito/instagram.md), [Quibi](../../../casos/fallo/quibi.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «aud».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google, Technical Writing One](https://developers.google.com/tech-writing/one) — curso con una unidad sobre audiencia; autoridad: Google for Developers.
- [Digital.gov, guías de lenguaje claro](https://www.plainlanguage.gov/) — escribir y probar el contenido para su audiencia; autoridad: Digital.gov.
- [RFC 8725: buenas prácticas para JWT](https://www.rfc-editor.org/rfc/rfc8725) — validación del algoritmo, emisor y audiencia; autoridad: IETF.
- [Diátaxis](https://diataxis.fr/) — cuatro necesidades de quien usa documentación y las formas que les corresponden; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — define una guía por su orientación a un objetivo y no a un componente; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← AUC](./auc.md) · [Autenticación →](./autenticacion.md)
