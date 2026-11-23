# Resolver la ruta

[↑ Glosario](../../README.md) · [← Resolver](./resolver.md) · [Respaldo →](./respaldo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Convertir un nombre de archivo en la ruta final que usará el sistema, aplicando decodificación, unión con la raíz y normalización.

Definición de trabajo de [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md).

## Por qué importa

La clase donde se define, [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), existe con este propósito: el taller existe para que practiques el ciclo completo con el que se descubre que un control aparente no controla: formular qué debería impedir, intentar romperlo con entradas que lo ataquen a él y no a su caso más conocido, reparar la causa y no el síntoma, y dejar una prueba que habría fallado antes de la reparación.

## Cómo funciona

Según [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md):

Un filtro que elimina `../` una vez convierte `....//secreto` en `../secreto`: al quitar la subcadena interna queda la que forma la secuencia. Quitarla en un bucle cierra ese caso y deja abiertos otros: la decodificación porcentual que ocurre después (`%2e%2e%2f`) vuelve a formar la secuencia, la barra invertida es un separador en Windows y no en POSIX, y las rutas absolutas ignoran la carpeta base. El patrón es el de `SE-460` (validar antes de transformar). La reparación es **resolver la ruta final con la misma lógica que usará el sistema y comprobar que sigue dentro de la raíz**: decodificar, unir con la carpeta base, normalizar y comparar el prefijo con la raíz, rechazando si no coincide.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md):

El equipo de la plataforma organiza el taller como una sesión de tres horas con dos roles: quien ataca escribe una hipótesis por control sin ver la implementación y quien defiende la reparación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md)) son:

- **Un archivo fuera de la carpeta se descarga** — causa: filtro de texto en lugar de comprobar el destino. Corrección: decodificar, resolver y comprobar el prefijo de la raíz.
- **El límite de intentos no frena a nadie** — causa: se cuenta por una cabecera que escribe el cliente. Corrección: contar por la conexión, por cuenta y por comportamiento.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La reparación es **resolver la ruta final con la misma lógica que usará el sistema y comprobar que sigue dentro de la raíz**: decodificar, unir con la carpeta base, normalizar y comparar el prefijo con la raíz, rechazando si no coincide. ([SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Normalización](../n/normalizacion.md), [Raíz](./raiz.md), [Ruta](./ruta.md), [Control aparente](../c/control-aparente.md), [Hipótesis de ruptura](../h/hipotesis-de-ruptura.md), [Prueba de regresión](../p/prueba-de-regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CWE-22](https://cwe.mitre.org/data/definitions/22.html) — recorrido de rutas; autoridad: MITRE.
- [OWASP: Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal) — descripción del ataque; autoridad: OWASP.
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) — tokens contra solicitudes forzadas; autoridad: OWASP.
- [MDN: X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) — uso seguro de la cabecera; autoridad: MDN.
- [Python: os.path](https://docs.python.org/3/library/os.path.html) — normalización de rutas y módulos por sistema; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Resolver](./resolver.md) · [Respaldo →](./respaldo.md)
