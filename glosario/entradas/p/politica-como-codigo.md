# Política como código

[↑ Glosario](../../README.md) · [← Polisemia](./polisemia.md) · [Política de acceso →](./politica-de-acceso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **política como código** es una regla de configuración escrita de forma que una herramienta pueda comprobarla de manera automática ([SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)). [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) la define con más precisión: una regla escrita en un lenguaje ejecutable que se evalúa sobre datos de entrada (la configuración de infraestructura, un archivo de flujo de trabajo, una lista de dependencias) y produce una decisión auditable.

## Por qué importa

Las normas escritas en un documento dependen de que alguien las recuerde y las revise a mano. Una política como código se aplica siempre, igual y sin depender de la memoria de nadie. La decisión que cambia es dónde vive una regla de seguridad o de operación: en una puerta automática por la que pasa todo, no en una guía que se lee una vez.

## Cómo funciona

[SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) describe un verificador de políticas que lee un descriptor de servicio (qué imagen, con qué usuario, qué límites) y comprueba reglas escritas como código: el servicio debe tener dueño, límites, una imagen con versión fija y un usuario sin privilegios. Dos propiedades hacen valiosa la puerta:

- **Independencia del origen**: un servicio de la plantilla (camino dorado) y uno hecho a mano pasan por la misma puerta. La plataforma no depende de que todos usen el camino fácil.
- **Decisión auditable**: la regla es texto versionado y la decisión se puede reproducir con los mismos datos de entrada.

Herramientas como Open Policy Agent ofrecen un lenguaje para escribir esas reglas. [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) las inserta en la canalización de CI/CD como compuerta: una violación bloquea el cambio antes de llegar a producción.

El límite está en la propia clase: estas políticas comprueban **forma, no sentido**. Un límite de CPU de mil núcleos cumple la regla «tiene límite» y es absurdo. Por eso se acompañan de rangos razonables y de revisión.

## Ejemplo

Una regla exige que todo descriptor declare un usuario distinto de root. El verificador revisa los descriptores en cada cambio. Un servicio nuevo sin usuario declarado falla la compuerta antes de desplegarse y el equipo recibe el motivo. El resultado es igual para el servicio generado por plantilla y para el escrito a mano. Mecanismo descrito en [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

## Errores y confusiones comunes

- **Los equipos no usan el camino**: es más difícil que lo manual o no cubre su caso; se corrige midiendo pasos y excepciones y mejorándolo. La política complementa el camino, no lo reemplaza.
- **El equipo de plataforma está saturado de solicitudes**: baja adopción y servicios hechos a mano.
- **Escribir reglas que solo miran la forma** y creer que garantizan sentido.
- **Políticas sin excepciones registradas**: obligan a puentear la puerta.

## Límites y cuándo no aplica

Solo comprueba lo que se le pidió y lo que puede evaluar sobre sus datos de entrada: no ve intención, contexto ni comportamiento en ejecución. Una política mal escrita bloquea trabajo legítimo o deja pasar lo inseguro con apariencia de control. Para reglas que dependen de juicio humano (aprobaciones, riesgo de negocio), el código solo puede exigir que la aprobación exista, no evaluarla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Regla](../r/regla.md), [Sobre](../s/sobre.md), [Camino dorado](../c/camino-dorado.md), [Carga cognitiva](../c/carga-cognitiva.md), [Compuerta](../c/compuerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Políticas como código».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) — políticas como código; autoridad: documentación del proyecto.
- [Open Policy Agent](https://www.openpolicyagent.org/docs) — políticas como código; autoridad: documentación del proyecto.
- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — qué es una plataforma interna y qué ofrece; autoridad: CNCF TAG App Delivery.
- [Team Topologies](https://teamtopologies.com/) — equipos de plataforma y carga cognitiva; autoridad: sitio de los autores del libro.
- [DORA](https://dora.dev/) — investigación sobre desempeño de entrega de software; autoridad: programa de investigación DORA.

---

[↑ Glosario](../../README.md) · [← Polisemia](./polisemia.md) · [Política de acceso →](./politica-de-acceso.md)
