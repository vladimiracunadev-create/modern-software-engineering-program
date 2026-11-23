# Híbrido

[↑ Glosario](../../README.md) · [← Heurística de prueba](./heuristica-de-prueba.md) · [Hidratación →](./hidratacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Combinación de un algoritmo clásico y uno poscuántico en una misma clave de sesión.

Definición de trabajo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md): Arquitectura donde un enrutador manda cada solicitud al workflow o al agente que le corresponde.

## Por qué importa

En [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), el tema «Híbrido» importa porque protege si cualquiera de los dos resiste.

En [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), el tema «Híbrido» importa porque permite pagar el agente solo donde aporta.

## Cómo funciona

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

Un saludo de TLS intercambia, entre otras cosas, una clave pública del cliente y un texto cifrado o clave pública del servidor. Con X25519, el intercambio ocupa unos 64 bytes y cabe en un segmento de red. Con ML-KEM-768 solo, 1 184 + 1 088 = 2 272 bytes: dos segmentos de 1 460 bytes. Con el híbrido (X25519 más ML-KEM-768), 2 336 bytes: también dos. Dos segmentos en lugar de uno significa una probabilidad mayor de fragmentación y de pérdida, y en redes con dispositivos intermedios que esperan que el primer mensaje del saludo quepa en un paquete, errores reales de conexión. El RFC 10024 define tres mecanismos híbridos para TLS 1.3 (X25519MLKEM768, SecP256r1MLKEM768 y SecP384r1MLKEM1024) y es lo que los clientes y servidores modernos implementan.

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

El equipo de *Avisos* hace el inventario y encuentra 31 usos de criptografía de clave pública: TLS entre cliente y servicio, TLS entre servicios, firmas de artefactos, tokens de sesión, certificados de dispositivos de aulas, cifrado de copias de seguridad con una clave pública y la firma de los informes que se entregan a las universidades. Clasifica por vida útil: las copias de seguridad y los historiales (25 años) son lo más urgente por la amenaza de almacenar ahora; los tokens de sesión (minutos) son lo menos urgente. El primer cambio es de agilidad: el formato de las copias identifica el algoritmo en una cabecera.

## Ejemplo

Ejemplo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* hace el inventario y encuentra 31 usos de criptografía de clave pública: TLS entre cliente y servicio, TLS entre servicios, firmas de artefactos, tokens de sesión, certificados de dispositivos de aulas, cifrado de copias de seguridad con una clave pública y la firma de los informes que se entregan a las universidades. Clasifica por vida útil: las copias de seguridad y los historiales (25 años) son lo más urgente por la amenaza de almacenar ahora; los tokens de sesión (minutos) son lo menos urgente. El primer cambio es de agilidad: el formato de las copias identifica el algoritmo en una cabecera.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un esquema híbrido combina un algoritmo clásico y uno poscuántico: ambos producen un secreto y la clave de sesión se deriva de los dos. ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))
- Para tres usos, calcula la desigualdad de Mosca con tus valores, decide si hace falta un híbrido, escribe qué tamaño nuevo aparece (clave, texto cifrado, firma, certificado) y qué límite conocido podría romper. ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))

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
