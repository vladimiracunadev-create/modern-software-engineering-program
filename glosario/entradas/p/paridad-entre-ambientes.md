# Paridad entre ambientes

[↑ Glosario](../../README.md) · [← Paridad demográfica](./paridad-demografica.md) · [Paridad entre entornos →](./paridad-entre-entornos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Igualdad de código, imagen y estructura entre desarrollo, pruebas y producción, con diferencias solo en configuración y credenciales.

Definición de trabajo de [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md).

## Por qué importa

La clase donde se define, [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), existe con este propósito: la clase existe para que trates un secreto como un dato con ciclo de vida y no como una línea de configuración: dónde nace, quién puede leerlo, cuánto vale lo que protege, cómo se detecta una filtración y cómo se cambia sin que el servicio caiga.

## Cómo funciona

Según [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md):

La separación de ambientes tiene dos partes que se confunden. La **separación de credenciales** hace que un secreto de desarrollo no abra producción: credenciales distintas por ambiente y, mejor, por servicio dentro del ambiente, para que una filtración abra lo mínimo. La **separación de datos** hace que los ambientes de prueba no contengan datos reales: una copia de producción en staging expone todos los registros aunque la credencial de staging no abra producción, y una persona con acceso a staging se convierte en una persona con acceso a datos de producción (ver `SE-463`). La configuración (qué endpoint, qué límite) puede diferir entre ambientes; el código y la imagen no deberían. La paridad entre ambientes reduce sorpresas, y la separación de credenciales y datos reduce daños: ambas son compatibles.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md):

El equipo inventaría 23 secretos con su dueño y radio y descubre dos sin dueño. Mueve las credenciales a un gestor que las entrega a cada servicio con una identidad propia, emite credenciales de base de datos con vencimiento de una hora para los procesos y deja una sola clave de larga duración (la de firma de enlaces). Separa ambientes: una credencial por servicio y ambiente, y datos sintéticos en staging.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md)) son:

- **Un secreto sigue vivo tras borrarlo del archivo** — causa: el historial lo conserva. Corrección: rotarlo; buscar en el historial.
- **La rotación tira el servicio** — causa: un solo valor válido durante el cambio. Corrección: doble validez y cierre observable.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-462 — Secretos, configuración y separación de ambientes](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El escáner es de juguete y se escribió conociendo los formatos que planta; la rotación se simuló en tiempo virtual con veinte instancias; la fuga uniforme entre ambientes es un supuesto; no se usó ninguna herramienta de detección ni gestor de secretos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Imagen](../i/imagen.md), [Producción](./produccion.md), [Doble validez](../d/doble-validez.md), [Entropía de una cadena](../e/entropia-de-una-cadena.md), [Radio de una filtración](../r/radio-de-una-filtracion.md).
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

[↑ Glosario](../../README.md) · [← Paridad demográfica](./paridad-demografica.md) · [Paridad entre entornos →](./paridad-entre-entornos.md)
