# Hipótesis de ruptura

[↑ Glosario](../../README.md) · [← Hipótesis de estado estable](./hipotesis-de-estado-estable.md) · [Hipótesis discriminante →](./hipotesis-discriminante.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Enunciado de qué entrada eludiría un control y por qué, formulado antes de probarla.

Definición de trabajo de [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md).

## Por qué importa

La clase donde se define, [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), existe con este propósito: el taller existe para que practiques el ciclo completo con el que se descubre que un control aparente no controla: formular qué debería impedir, intentar romperlo con entradas que lo ataquen a él y no a su caso más conocido, reparar la causa y no el síntoma, y dejar una prueba que habría fallado antes de la reparación.

## Cómo funciona

[SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md):

El equipo de la plataforma organiza el taller como una sesión de tres horas con dos roles: quien ataca escribe una hipótesis por control sin ver la implementación y quien defiende la reparación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md)) son:

- **Un archivo fuera de la carpeta se descarga** — causa: filtro de texto en lugar de comprobar el destino. Corrección: decodificar, resolver y comprobar el prefijo de la raíz.
- **El límite de intentos no frena a nadie** — causa: se cuenta por una cabecera que escribe el cliente. Corrección: contar por la conexión, por cuenta y por comportamiento.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron cuatro experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los cuatro controles son funciones de juguete en memoria, las 5 000 cargas salen de un alfabeto del autor, las rutas se resuelven con módulos de Python y no con un sistema de archivos, y no se atacó ningún servicio ni sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Control](../c/control.md), [Control aparente](../c/control-aparente.md), [Prueba de regresión](../p/prueba-de-regresion.md), [Resolver la ruta](../r/resolver-la-ruta.md), [Token ligado a la sesión](../t/token-ligado-a-la-sesion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

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

[↑ Glosario](../../README.md) · [← Hipótesis de estado estable](./hipotesis-de-estado-estable.md) · [Hipótesis discriminante →](./hipotesis-discriminante.md)
