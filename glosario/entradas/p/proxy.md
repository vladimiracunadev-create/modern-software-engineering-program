# Proxy

[↑ Glosario](../../README.md) · [← Proveniencia de datos](./proveniencia-de-datos.md) · [Proxy de inyección →](./proxy-de-inyeccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Un **proxy** es un sustituto con la misma interfaz que controla el acceso al objeto real ([SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)). Es uno de los patrones estructurales: el cliente cree hablar con el objeto verdadero, pero el proxy decide si, cuándo y cómo el acceso llega. En [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) aparece otra acepción, la de un **proxy de medición**: una medida sobre un sustituto accesible que muestra la forma de un efecto sin su magnitud. Esta entrada trata el patrón.

## Por qué importa

Permite añadir control (carga diferida, permisos, acceso remoto) sin cambiar a los clientes. Y obliga a distinguirlo de patrones vecinos con los que comparte estructura. [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) insiste en que la estructura es la misma para varios y lo que los separa es la intención; confundirla produce una prueba equivocada.

## Cómo funciona

Los cinco patrones de [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) comparten una estructura: un objeto que **contiene o envuelve** a otro. La intención diferencia:

- **Adapter:** cambia la interfaz a la que el cliente espera.
- **Facade:** ofrece una interfaz simple a un subsistema.
- **Proxy:** controla el acceso a un objeto con *su misma* interfaz (perezoso, remoto, con permisos).
- **Composite:** trata un grupo de objetos como uno solo.
- **Decorator:** añade comportamiento conservando la interfaz.

Proxy y Decorator pueden ser estructuralmente idénticos, y un mismo objeto puede ser ambos: el Decorator añade comportamiento (registro, reintento); el Proxy controla el acceso (perezoso, permisos, remoto). Cada intención tiene su propio modo de estropearse y su propia prueba: la del proxy perezoso es que el objeto real no se cree hasta el primer uso y que el resultado sea el mismo.

## Ejemplo

```python
class ImagenProxy:
    def __init__(self, ruta): self._ruta, self._real = ruta, None
    def mostrar(self):
        if self._real is None:          # carga diferida
            self._real = Imagen(self._ruta)
        return self._real.mostrar()
```

Un proxy de permisos haría lo análogo comprobando la identidad antes de delegar.

## Errores y confusiones comunes

- **Confundir proxy con Decorator.** La estructura es igual; lo que cambia es la intención ([SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)).
- **Proxy que cambia el resultado.** Si altera lo que devuelve, ya no es transparente para el cliente.
- **Confundirlo con un servidor proxy de red.** Comparte el nombre y la idea de intermediario, pero [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) trata el patrón de objetos.

## Límites y cuándo no aplica

El proxy es adecuado cuando la construcción es cara y el uso es raro; si casi todos los objetos se usan, solo suma una indirección ([SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)). Un proxy remoto oculta la red, pero no sus fallos: latencia y errores parciales siguen existiendo y el cliente debe contemplarlos. Y el proxy de medición de [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) es otra cosa: un indicador accesible que sustituye a uno inaccesible.

## Relación con otros conceptos

- **Prerrequisito:** [Interfaz](../i/interfaz.md).
- **Ver también:** [Efecto](../e/efecto.md), [Medida](../m/medida.md), [Objeto](../o/objeto.md), [Sobre](../s/sobre.md), [Bloque y rejilla](../b/bloque-y-rejilla.md), [Coalescencia](../c/coalescencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (26 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Cloudflare](../../../casos/exito/cloudflare.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Proveniencia de datos](./proveniencia-de-datos.md) · [Proxy de inyección →](./proxy-de-inyeccion.md)
