# Híbrido

[↑ Glosario](../../README.md) · [← Heurística de prueba](./heuristica-de-prueba.md) · [Hidratación →](./hidratacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

«Híbrido» tiene en el programa dos sentidos que conviene no mezclar. El principal, de [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) (criptografía poscuántica y migración), es la **combinación de un algoritmo clásico y uno poscuántico en una misma clave de sesión**. El segundo, de [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) (workflows frente a agentes), es una **arquitectura donde un enrutador manda cada solicitud al workflow o al agente que le corresponde**. (En [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) aparece además «híbrido en contenedor», una web dentro de una aplicación; ese es otro asunto, tratado en el enfoque de construcción.)

## Por qué importa

En criptografía, el híbrido protege si cualquiera de los dos resiste: si el algoritmo poscuántico resulta tener un defecto, el clásico sigue protegiendo, y si un computador cuántico rompe el clásico, el poscuántico sigue protegiendo. En agentes, permite pagar el agente solo donde aporta, y usar un workflow determinista para el resto.

## Cómo funciona

**Criptográfico ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md)).** El saludo de TLS intercambia, entre otras cosas, una clave pública del cliente y un texto cifrado o clave pública del servidor. El tamaño importa:

- X25519: unos 64 bytes; cabe en un segmento de red.
- ML-KEM-768 solo: 1 184 + 1 088 = 2 272 bytes; dos segmentos de 1 460 bytes.
- Híbrido (X25519 más ML-KEM-768): 2 336 bytes; también dos.

Dos segmentos en lugar de uno aumentan la probabilidad de fragmentación y de pérdida y, en redes con dispositivos intermedios que esperan el primer mensaje en un paquete, causan errores reales de conexión. El RFC 10024 define tres mecanismos híbridos para TLS 1.3 (X25519MLKEM768, SecP256r1MLKEM768 y SecP384r1MLKEM1024).

**De arquitectura ([SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md)).** Un enrutador clasifica cada solicitud y la manda al flujo fijo (workflow) cuando el camino es conocido, o al agente cuando exige decidir.

## Ejemplo

El equipo de *Avisos* en [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) hace un inventario y encuentra 31 usos de criptografía de clave pública (TLS entre cliente y servicio y entre servicios, firmas de artefactos, tokens de sesión, certificados de dispositivos, cifrado de copias con clave pública…), y los prioriza para migrar. Ilustración de [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md): solicitudes frecuentes y predecibles van al workflow; las raras y abiertas, al agente.

## Errores y confusiones comunes

- **Pasar a poscuántico solo y perder la protección clásica,** sin necesidad.
- **Ignorar el tamaño del saludo:** la fragmentación puede romper conexiones por dispositivos intermedios.
- **Confundir «híbrido» cripto con «híbrido» de aplicación o de nube,** que no tienen relación.
- **Usar un agente para todo** en lugar de enrutar ([SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md)).

## Límites y cuándo no aplica

El híbrido criptográfico no resuelve el inventario ni la migración de los demás usos (firmas, certificados). Los tamaños son los de [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) para esos algoritmos; otros parámetros difieren. El enrutador de agentes añade su propio punto de fallo: clasificar mal una solicitud.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Algoritmo](../a/algoritmo.md), [Arquitectura](../a/arquitectura.md), [Combinación](../c/combinacion.md), [Agencia excesiva](../a/agencia-excesiva.md), [Agilidad criptográfica](../a/agilidad-criptografica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Heurística de prueba](./heuristica-de-prueba.md) · [Hidratación →](./hidratacion.md)
