# Radio de explosión

[↑ Glosario](../../README.md) · [← Radio de efecto](./radio-de-efecto.md) · [Radio de impacto →](./radio-de-impacto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Conjunto de lo que un experimento puede dañar si sale mal, descrito por fracción de tráfico, alcance, duración, intensidad y profundidad.

Definición de trabajo de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md): Conjunto de recorridos o funciones que dejan de funcionar cuando falla un elemento.
- En [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md): Alcance máximo del daño que puede causar un experimento.
- En [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md): Conjunto de recursos que un error o una credencial comprometida puede afectar.

## Por qué importa

La clase donde se define, [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), existe con este propósito: la clase existe para que dimensiones el **radio de explosión** de un experimento (a cuánta gente, durante cuánto tiempo y con qué intensidad se le hace daño) y para que escribas las **condiciones de aborto** que lo detienen antes de que el daño supere lo acordado.

## Cómo funciona

Según [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md):

El **radio de explosión** es el conjunto de lo que el experimento puede dañar si sale mal. Los principios lo plantean como una responsabilidad: se admite un impacto negativo de corto plazo, pero se debe contener. No es un solo número. Se controla en cinco dimensiones que se combinan: la **fracción del tráfico** afectada; el **alcance** (qué clientes, instancias, zonas o regiones); la **duración**; la **intensidad** de la falla (10 % de errores o 100 %) y la **profundidad** (si afecta solo a la llamada probada o a lo que depende de ella). Chaos Mesh, por ejemplo, define el alcance con selectores por espacio de nombres, etiquetas, anotaciones o nodos, y la propia documentación presenta eso como el control del radio.

Según [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md):

Reproduce el fallo clásico de la clase: **replicar la base de datos y creer que el sistema ya no tiene un punto único de fallo**. Calcula el radio de explosión de la topología con la base replicada y la web en un solo nodo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md):

Supón, como caso hipotético y no como medición, que el equipo escribe la especificación del experimento «almacenamiento con 20 % de errores»: radio de 2 % del tráfico durante 10 minutos, aborto si el grupo experimental falla más de 50 % en 10 s o si el servicio global baja de 99,5 % en 30 s, reversión «quitar la regla del proxy» probada la víspera con un tiempo de 4 s, responsable la guardia de la API, ventana de martes a jueves de 10:00 a 16:00 y nunca en una semana de cierre de plazo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)) son:

- **El experimento no detecta nada y se declara confirmado** — causa: radio sin potencia suficiente. Corrección: calcular la fracción mínima y declarar el efecto mínimo detectable.
- **El experimento aborta de inmediato** — causa: condición global consumida por la falla esperada. Corrección: medir el grupo experimental y separar el umbral de aborto del de la hipótesis.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Calcula el radio de explosión de la topología con la base replicada y la web en un solo nodo. ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md))
- Separar por entorno y por carga reduce el **radio de explosión**: el máximo daño posible de una credencial robada o de un comando mal escrito. ([SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Conjunto](../c/conjunto.md), [Daño](../d/dano.md), [Función](../f/funcion.md), [Condición de aborto](../c/condicion-de-aborto.md), [Estado estable](../e/estado-estable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-403 — Entornos, cuentas y separación de responsabilidades](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — minimizar el radio de explosión; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Chaos Mesh: Define the Scope of Chaos Experiments](https://chaos-mesh.org/docs/define-chaos-experiment-scope/) — selectores y radio de explosión; autoridad: documentación del proyecto Chaos Mesh.
- [Netflix: «ChAP: Chaos Automation Platform»](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — tamaño de experimento, control y experimento, interruptor del experimento; autoridad: blog de ingeniería de Netflix.
- [AWS FIS: stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) — condiciones de parada basadas en alarmas; autoridad: documentación de Amazon Web Services.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Radio de efecto](./radio-de-efecto.md) · [Radio de impacto →](./radio-de-impacto.md)
