# Radio de explosión

[↑ Glosario](../../README.md) · [← Radio de efecto](./radio-de-efecto.md) · [Radio de impacto →](./radio-de-impacto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

El **radio de explosión** es el conjunto de lo que algo puede dañar si sale mal. El programa lo usa con tres matices:

- En [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) (ingeniería del caos): lo que un experimento puede dañar, descrito por fracción de tráfico, alcance, duración, intensidad y profundidad. [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) lo resume como el alcance máximo del daño de un experimento.
- En [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (arquitectura): el conjunto de recorridos o funciones que dejan de funcionar cuando falla un elemento.
- En [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) (cloud): el conjunto de recursos que un error o una credencial comprometida puede afectar.

## Por qué importa

Un fallo, un experimento o una credencial robada tienen un daño máximo. Si ese máximo es la plataforma entera, cada error es potencialmente catastrófico. La decisión que cambia es diseñar para acotar: separar, limitar y dosificar, de modo que lo peor posible sea tolerable.

## Cómo funciona

[SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md) plantea el radio como una responsabilidad: se admite un impacto negativo de corto plazo, pero se debe contener. No es un solo número: se controla en cinco dimensiones que se combinan:

1. **Fracción del tráfico** afectada.
2. **Alcance**: qué clientes, instancias, zonas o regiones.
3. **Duración**.
4. **Intensidad** de la falla (10 % de errores o 100 %).
5. **Profundidad**: si afecta solo a la llamada probada o a lo que depende de ella.

Herramientas como Chaos Mesh definen el alcance con selectores por espacio de nombres, etiquetas, anotaciones o nodos; la documentación lo presenta como el control del radio.

En arquitectura, [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) reproduce el fallo clásico: replicar la base de datos y creer que el sistema ya no tiene un punto único de fallo, cuando la web sigue en un solo nodo; calcular el radio de explosión de la topología revela qué sigue cayendo. En cloud, [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) muestra que separar por entorno y por carga reduce el máximo daño posible de una credencial robada o de un comando mal escrito.

## Ejemplo

Un experimento de caos inyecta latencia. Con el radio definido como 1 % del tráfico, una zona, 5 minutos, intensidad moderada y solo la llamada probada, el daño máximo es pequeño aunque la falla resulte peor de lo previsto. Con un radio sin acotar, la misma falla puede tumbar la plataforma. Principio de [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

## Errores y confusiones comunes

- **El experimento no detecta nada y se declara confirmado**: radio sin potencia suficiente; se calcula la fracción mínima y se declara el efecto mínimo detectable.
- **El experimento aborta de inmediato**: condición global consumida por la falla esperada; se mide el grupo experimental y se separa el umbral de aborto del de la hipótesis.
- **Reducirlo a un porcentaje**: son cinco dimensiones.
- **Creer que replicar un componente elimina el punto único de fallo**.

## Límites y cuándo no aplica

Un radio muy pequeño reduce el daño pero también la potencia para detectar el efecto: hay un compromiso entre seguridad y capacidad de aprender del experimento. El radio describe el máximo previsto: un fallo que se propaga por dependencias no consideradas puede exceder el cálculo. Y no sustituye una condición de aborto que detenga el daño en curso.

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
