# Prueba discriminante

[↑ Glosario](../../README.md) · [← Prueba de trabajo](./prueba-de-trabajo.md) · [Prueba frágil →](./prueba-fragil.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una **prueba discriminante** es un experimento ([SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)) u observación ([SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md)) cuyo resultado separa hipótesis: da un resultado distinto según cuál sea cierta. No es cualquier prueba: una que pasa igual con las dos explicaciones no discrimina nada.

## Por qué importa

En diagnóstico, es común acumular datos compatibles con todas las hipótesis y sentir que se avanza. La prueba discriminante es la que realmente reduce el espacio: tras ella, al menos una hipótesis sale. Cambia cómo se decide el siguiente paso: no «qué puedo medir», sino «qué medición separa mis dos mejores explicaciones».

## Cómo funciona

[SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) presenta el método: después de la traza normal, se introduce un **único** fallo. La prueba debe producir un cambio **predicho**: un *override* de DNS, un puerto cerrado o una caché controlada. Si cambian varias señales, se vuelve a reducir antes de concluir. La estructura lógica es la de [SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md): «si H entonces O»; observar no-O refuta H (*modus tollens*), mientras observar O no prueba H (afirmar el consecuente es una falacia).

Los pasos prácticos:

1. Escribir dos o más hipótesis rivales.
2. Elegir un cambio mínimo (una sola variable).
3. **Predecir** el resultado bajo cada hipótesis, antes de ejecutar.
4. Ejecutar y comparar.

La causa de su valor es que fuerza a que la hipótesis pueda fallar; una explicación que no predice nada observable no se puede discriminar.

## Ejemplo

Síntoma: «la página no carga». Hipótesis A: falla la resolución DNS. Hipótesis B: falla la conexión al puerto. Prueba discriminante: conectar directamente a la IP (saltando DNS). Si carga, A se sostiene y B se descarta; si no carga, B sigue en pie. Ilustración:

```bash
curl --resolve ejemplo.com:443:203.0.113.10 https://ejemplo.com/    # fija la IP y salta DNS
```

## Errores y confusiones comunes

- **Informe con una lista de errores sin ordenar.** Causa: no se identificó la primera divergencia; corrección: comparar con el caso sano y señalar la primera fase que difiere ([SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)).
- **Eventos de componentes que no se pueden unir.** Causa: falta un identificador propagado; corrección: generarlo en el borde, propagarlo y registrarlo en cada capa ([SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)).
- **Cambiar varias cosas a la vez.** Si cambian varias señales, no se sabe cuál separó las hipótesis.

## Límites y cuándo no aplica

El taller de [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) no garantiza visibilidad dentro de redes de terceros, y no deben recolectarse tokens ni cuerpos personales. Una prueba discriminante supone que las hipótesis son exhaustivas: si la causa real no estaba entre ellas, la prueba puede «confirmar» la menos mala. Y en sistemas con fallos intermitentes, una sola ejecución no discrimina: hay que repetir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hipótesis](../h/hipotesis.md), [Observación](../o/observacion.md), [Resultado](../r/resultado.md), [Alcance](../a/alcance.md), [Cambio mínimo](../c/cambio-minimo.md), [Diagnóstico](../d/diagnostico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Prueba de trabajo](./prueba-de-trabajo.md) · [Prueba frágil →](./prueba-fragil.md)
