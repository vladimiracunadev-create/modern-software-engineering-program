# Doble validez

[↑ Glosario](../../README.md) · [← Doble escritura](./doble-escritura.md) · [Doce factores →](./doce-factores.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Periodo en que el verificador acepta tanto el secreto viejo como el nuevo para permitir una migración sin interrupción.

Definición de trabajo de [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md).

## Por qué importa

La clase donde se define, [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), existe con este propósito: la clase existe para que trates un secreto como un dato con ciclo de vida y no como una línea de configuración: dónde nace, quién puede leerlo, cuánto vale lo que protege, cómo se detecta una filtración y cómo se cambia sin que el servicio caiga.

## Cómo funciona

Según [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md):

Rotar es cambiar el valor válido de un secreto. Si el emisor y el verificador cambian en instantes distintos, hay una ventana en la que no coinciden y las solicitudes fallan. La solución es la **doble validez**: el verificador acepta la clave vieja y la nueva durante la transición; los emisores migran a la nueva; cuando ninguno usa la vieja, se retira. El criterio de cierre debe ser **observable** (un contador de usos de la clave vieja en cero durante un periodo), no un temporizador fijo, porque siempre hay una instancia que no recargó. Esa instancia es el caso de borde: un cierre por tiempo la rompe en silencio; un cierre condicionado deja la clave vieja viva más tiempo y lo hace visible.

Según [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md):

El equipo inventaría 23 secretos con su dueño y radio y descubre dos sin dueño. Mueve las credenciales a un gestor que las entrega a cada servicio con una identidad propia, emite credenciales de base de datos con vencimiento de una hora para los procesos y deja una sola clave de larga duración (la de firma de enlaces). Separa ambientes: una credencial por servicio y ambiente, y datos sintéticos en staging. Añade un escáner de secretos en la revisión de cambios y en una tarea nocturna sobre el historial, con una regla: un hallazgo cuenta como incidente y la clave se rota, no se oculta.

## Ejemplo

Ejemplo de [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md) (sección «Ejemplo profesional»):

El equipo inventaría 23 secretos con su dueño y radio y descubre dos sin dueño. Mueve las credenciales a un gestor que las entrega a cada servicio con una identidad propia, emite credenciales de base de datos con vencimiento de una hora para los procesos y deja una sola clave de larga duración (la de firma de enlaces). Separa ambientes: una credencial por servicio y ambiente, y datos sintéticos en staging. Añade un escáner de secretos en la revisión de cambios y en una tarea nocturna sobre el historial, con una regla: un hallazgo cuenta como incidente y la clave se rota, no se oculta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La rotación tira el servicio** — causa: un solo valor válido durante el cambio. Corrección: doble validez y cierre observable. ([SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La solución es la **doble validez**: el verificador acepta la clave vieja y la nueva durante la transición; los emisores migran a la nueva; cuando ninguno usa la vieja, se retira. ([SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interrupción](../i/interrupcion.md), [Migración](../m/migracion.md), [Secreto](../s/secreto.md), [Verificador](../v/verificador.md), [Entropía de una cadena](../e/entropia-de-una-cadena.md), [Paridad entre ambientes](../p/paridad-entre-ambientes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — gestión, rotación y auditoría de secretos; autoridad: OWASP.
- [The Twelve-Factor App: configuración](https://12factor.net/config) — separar configuración y código; autoridad: metodología publicada por sus autores.
- [CWE-798](https://cwe.mitre.org/data/definitions/798.html) — credenciales incrustadas; autoridad: MITRE.
- [GitHub: secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) — detección por patrones de proveedores; autoridad: documentación de GitHub.
- [Meli et al., NDSS 2019](https://www.ndss-symposium.org/ndss-paper/how-bad-can-it-git-characterizing-secret-leakage-in-public-github-repositories/) — filtración de secretos en repositorios públicos; autoridad: Network and Distributed System Security Symposium.

---

[↑ Glosario](../../README.md) · [← Doble escritura](./doble-escritura.md) · [Doce factores →](./doce-factores.md)
