# Excepción

[↑ Glosario](../../README.md) · [← Excedente del cliente](./excedente-del-cliente.md) · [Excepción registrada →](./excepcion-registrada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

**Excepción** tiene dos sentidos que el programa mantiene separados:

- **En el código** ([SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md)): un objeto que señala una interrupción anormal del flujo.
- **En gobernanza** ([SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md)): un cambio o incumplimiento que no sigue la política, aceptado con **dueño, razón y fecha de vencimiento**. [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) la usa para un cambio de un derecho a un cliente, con vencimiento y autorización.

## Por qué importa

En código, decide cómo se comunica un fallo: por una interrupción del flujo o por un resultado esperado. En gobernanza, decide si una política es real: sin excepciones registradas, la política se incumple en silencio; con excepciones sin dueño ni fecha, se convierten en la regla. [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) lo resume: una política que nadie comprueba es una intención.

## Cómo funciona

- **Código** ([SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md)): cuando ausencia o rechazo es parte esperada del dominio, un resultado etiquetado evita usar excepciones como control ordinario (por ejemplo, `{'ok': False, 'error': ...}` o `Result<T,E>` en Rust). Un resultado como `DNS_TIMEOUT` puede ser un dato normal del diagnóstico y no una excepción. Al traducir una excepción hay que conservar la causa con `raise ... from e`.
- **Política** ([SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md)): las excepciones se registran con dueño y fecha, se revisan periódicamente y se comprueban mecánicamente donde se pueda (por ejemplo, el comprobador de forma o el contrato en integración continua).
- **Derechos** ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md)): una excepción de un cliente (más cupo, una función habilitada) tiene vencimiento y autorización; sin ellos, el modelo de derechos se llena de casos sueltos.

## Ejemplo

```python
try:
    resolver(nombre)
except socket.gaierror as e:
    raise ErrorDeDiagnostico("fallo de resolución") from e   # conserva la causa
```

En gobernanza ([SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md)): «incumplimiento aceptado: cifrado en reposo del bucket X, dueño: plataforma, razón: migración en curso, vence: 2026-06-30».

## Errores y confusiones comunes

- **El mensaje final no menciona el fallo original.** Causa: se tradujo la excepción sin `from`; corrección: `raise ... from e` ([SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md)).
- **Excepciones de política sin vencimiento.** Se vuelven permanentes y la política deja de ser cierta.
- **Usar excepciones para el flujo ordinario.** Cuando el rechazo es esperado, un resultado etiquetado es más claro.

## Límites y cuándo no aplica

No todo error de dominio es una excepción de código ([SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md)). Un modelo de derechos con muchas excepciones indica que el modelo propio de la base de clientes sería más claro ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md)). Y una excepción de política aprobada no reduce el riesgo: solo lo hace explícito y con dueño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autorización](../a/autorizacion.md), [Control](../c/control.md), [Derecho](../d/derecho.md), [Evento](./evento.md), [Chaining](../c/chaining.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (158 clases más lo mencionan; las que más):

[SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Shopify](../../../casos/exito/shopify.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Excepciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — documenta ownership, tipos de error, traits y concurrencia usados como contraste semántico.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de verificación; autoridad: OWASP.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Excedente del cliente](./excedente-del-cliente.md) · [Excepción registrada →](./excepcion-registrada.md)
