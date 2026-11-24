# Aceptación desde el consumidor

[↑ Glosario](../../README.md) · [← Acelerador](./acelerador.md) · [Acierto en tres de tres →](./acierto-en-tres-de-tres.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

La **aceptación desde el consumidor** es el criterio de cierre de un producto reutilizable que [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) plantea así: una persona nueva, que no conoce el código, sigue el quickstart, ejecuta un caso, interpreta un error, instala un plugin y migra de una versión a otra. El producto se acepta cuando esa persona lo consigue con la documentación y los artefactos publicados, no cuando quien lo construyó puede demostrarlo en su máquina. En el programa el término aparece en el proyecto SDK y CLI; no es una certificación formal, es un procedimiento de aceptación propio del proyecto.

## Por qué importa

Quien construye una biblioteca arrastra conocimiento que el consumidor no tiene: qué variable de entorno hay que fijar, qué orden de instalación funciona, qué mensaje de error significa qué. Una demostración hecha por el autor oculta justo esas brechas. Aceptar desde el consumidor cambia una decisión concreta: la fecha de «terminado» deja de depender de que las pruebas internas pasen y depende de que un tercero llegue a un resultado correcto con lo que se entrega. También obliga a registrar tiempo y bloqueos, de modo que la facilidad de adopción deja de ser una impresión y pasa a ser un dato.

## Cómo funciona

El procedimiento tiene cinco recorridos, cada uno con una salida observable:

1. **Quickstart:** instalar en un entorno limpio y obtener un primer resultado correcto.
2. **Ejecutar un caso:** usar la interfaz pública con una entrada propia, no la del ejemplo.
3. **Interpretar un error:** provocar una entrada inválida y comprobar que el mensaje permite actuar.
4. **Instalar un plugin:** usar el punto de extensión con un complemento compatible y con uno incompatible.
5. **Migrar:** pasar de la versión anterior a la nueva siguiendo la guía de migración.

Se anotan el tiempo hasta el primer éxito y cada punto donde la persona se detuvo. La causa de que el método funcione es la separación de roles: quien acepta no es quien implementó, así que cada supuesto implícito se vuelve un bloqueo visible. El cierre incluye además los **problemas conocidos** y la **ruta de rollback**; una demostración solo del camino feliz no los contiene.

## Ejemplo

En el producto reutilizable de [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), un release agrupa contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La aceptación consiste en que alguien ajeno parta del paquete instalado (no del repositorio clonado) y recorra los cinco pasos. Si en el paso 3 el mensaje dice solo «error de configuración», el bloqueo se registra y la corrección es mejorar el mensaje, no explicarlo en voz alta. Una forma mínima de dejarlo escrito (ilustración, no un formato del programa):

```text
paso: instalar plugin incompatible
esperado: rechazo con versión requerida y versión encontrada
observado: traza interna sin mencionar versiones
bloqueo: sí (12 min)  -> corregir mensaje antes de aceptar
```

## Errores y confusiones comunes

- **Aceptar con la demo del autor.** El autor conoce los atajos; la prueba pierde su valor. Debe ejecutarla alguien que no escribió el producto.
- **Confundirla con una prueba de contrato.** La prueba de contrato ([SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) la pide desde el consumidor) verifica promesas automáticamente; la aceptación verifica además documentación, mensajes y migración con una persona.
- **Medir solo el éxito.** Sin tiempo ni bloqueos registrados no hay dato para mejorar.
- **Omitir problemas conocidos y rollback.** Un cierre sin ellos oculta el riesgo de adoptar la versión.

## Límites y cuándo no aplica

Una persona es una muestra pequeña: encuentra bloqueos, pero no estima cuántos usuarios fallarían. El procedimiento acredita un release candidato dentro de su matriz de versiones y entornos, no disponibilidad, seguridad ni soporte en producción ([SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) lo declara). No aplica a código interno de un solo uso, donde el costo de reclutar a alguien supera lo que se aprende, y no sustituye una prueba de usabilidad con varios perfiles cuando el producto tiene muchos consumidores.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Complemento](../c/complemento.md), [Contrato multicapa](../c/contrato-multicapa.md), [Matriz de compatibilidad](../m/matriz-de-compatibilidad.md), [Release candidate](../r/release-candidate.md), [Supply chain mínima](../s/supply-chain-minima.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Acelerador](./acelerador.md) · [Acierto en tres de tres →](./acierto-en-tres-de-tres.md)
