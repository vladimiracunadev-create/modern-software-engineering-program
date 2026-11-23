# Bandera de funcionalidad

[↑ Glosario](../../README.md) · [← Bandeja de salida](./bandeja-de-salida.md) · [Barrera independiente →](./barrera-independiente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Una **bandera de funcionalidad** (*feature flag*) es una condición en el código que activa o desactiva un comportamiento sin desplegar código nuevo. [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) la define así, [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) como una condición de ejecución que activa o desactiva una función sin desplegar y [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) como un interruptor que decide qué código se ejecuta. [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) insiste en no mezclarla con otras dos cosas que los productos SaaS suelen confundir: el **plan** (un paquete comercial que se vende) y el **derecho** (lo que una cuenta concreta puede hacer hoy, con límites y vencimientos).

## Por qué importa

Permite separar la **exposición** del **despliegue** ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)): se despliega apagada, se enciende para unas personas y se apaga ante un problema sin volver a la versión anterior. Eso reduce el costo de revertir y habilita lanzamientos graduales.

## Cómo funciona

El código contiene la condición y el valor se lee de configuración, de modo que cambiarlo no requiere un nuevo despliegue. [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) toma de Fowler una tipología: banderas de **lanzamiento** (de corta vida), de **experimento**, **operativas** (para apagar una dependencia) y de **permisos**. Cada tipo tiene ciclo de vida distinto. [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) separa su rol del de los derechos de uso: la bandera es un interruptor técnico, el derecho es una regla de negocio por cuenta.

## Ejemplo

[SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md): una función nueva se despliega con la bandera apagada, se activa para un grupo de personas y, si aparece un problema, se apaga sin desplegar de nuevo. [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) muestra el error contrario: usar la misma tabla o el mismo `if` para plan, derecho y bandera.

Los tipos importan porque cada uno vive un tiempo distinto: una bandera de lanzamiento debe retirarse cuando el lanzamiento termina, mientras que una operativa (apagar una dependencia) o de permisos puede durar mientras exista la razón. Según [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), la disciplina que contiene el costo es asignar a cada bandera un dueño y un plazo.

## Errores y confusiones comunes

- **Mezclar plan, derecho y bandera** en una misma condición ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md)).
- **Banderas olvidadas.** Se convierten en código que nadie se atreve a borrar ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)).
- **Ignorar las combinaciones.** Cada bandera duplica las configuraciones posibles del sistema y las combinaciones dejan de probarse ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)).

## Límites y cuándo no aplica

[SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) nombra el costo: duplicación de configuraciones, combinaciones sin probar y banderas olvidadas; la disciplina consiste en darle a cada bandera un dueño y un plazo de retiro. Una bandera cambia la ruta de ejecución en producción, de modo que apagarla no equivale a deshacer cambios de datos ya realizados con ella encendida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Función](../f/funcion.md), [Cambio de plan](../c/cambio-de-plan.md), [Cubrimiento de pares](../c/cubrimiento-de-pares.md), [Cuota](../c/cuota.md), [Derecho](../d/derecho.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-475 — Feature flags y entrega progresiva](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Banderas de funcionalidad».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DORA: entrega continua](https://dora.dev/capabilities/continuous-delivery/) — capacidad de liberar con seguridad en cualquier momento; autoridad: DORA, Google Cloud.
- [Fowler: BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: Martin Fowler.
- [Fowler: CanaryRelease](https://martinfowler.com/bliki/CanaryRelease.html) — exposición a un subconjunto; autoridad: Martin Fowler.
- [Google SRE Workbook: canarying releases](https://sre.google/workbook/canarying-releases/) — decisión estadística del canario; autoridad: Google.
- [Fowler: feature toggles](https://martinfowler.com/articles/feature-toggles.html) — tipos de banderas y su costo; autoridad: Pete Hodgson en martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Bandeja de salida](./bandeja-de-salida.md) · [Barrera independiente →](./barrera-independiente.md)
