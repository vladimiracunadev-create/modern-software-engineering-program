# Control aparente

[↑ Glosario](../../README.md) · [← Control](./control.md) · [Controlador →](./controlador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Control que existe, tiene pruebas favorables y decide con un dato que controla quien ataca.

Definición de trabajo de [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md).

## Por qué importa

La clase donde se define, [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), existe con este propósito: el taller existe para que practiques el ciclo completo con el que se descubre que un control aparente no controla: formular qué debería impedir, intentar romperlo con entradas que lo ataquen a él y no a su caso más conocido, reparar la causa y no el síntoma, y dejar una prueba que habría fallado antes de la reparación.

## Cómo funciona

Según [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md):

**Cómo leer la figura.** Cada tarjeta es una prueba y a la derecha el resultado con el control aparente y con el reparado: coral si el aparente deja pasar lo que no debe y verde azulado si los dos coinciden. Mira que solo dos de las seis pruebas separan los controles: las que usan un dato que controla el atacante. **Dónde deja de valer:** detrás de un proxy la dirección de la conexión es la del proxy: la reparación real exige configurar qué proxies son de confianza y leer el elemento correcto de la cadena. El verificador reparado es de juguete; en producción se usa una biblioteca revisada configurada con una lista cerrada de algoritmos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md):

El equipo de la plataforma organiza el taller como una sesión de tres horas con dos roles: quien ataca escribe una hipótesis por control sin ver la implementación y quien defiende la reparación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md)) son:

- **Un archivo fuera de la carpeta se descarga** — causa: filtro de texto en lugar de comprobar el destino. Corrección: decodificar, resolver y comprobar el prefijo de la raíz.
- **El límite de intentos no frena a nadie** — causa: se cuenta por una cabecera que escribe el cliente. Corrección: contar por la conexión, por cuenta y por comportamiento.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada tarjeta es una prueba y a la derecha el resultado con el control aparente y con el reparado: coral si el aparente deja pasar lo que no debe y verde azulado si los dos coinciden. ([SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Control](./control.md), [Hipótesis de ruptura](../h/hipotesis-de-ruptura.md), [Prueba de regresión](../p/prueba-de-regresion.md), [Resolver la ruta](../r/resolver-la-ruta.md), [Token ligado a la sesión](../t/token-ligado-a-la-sesion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-467 — Taller: explotar y reparar un control aparente](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md).

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

[↑ Glosario](../../README.md) · [← Control](./control.md) · [Controlador →](./controlador.md)
