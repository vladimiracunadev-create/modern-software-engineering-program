# Secuencia

[↑ Glosario](../../README.md) · [← Secretos y configuración](./secretos-y-configuracion.md) · [Secuencia de escape →](./secuencia-de-escape.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

La palabra **secuencia** tiene en el programa tres sentidos, y esta entrada los separa. El **principal** viene de [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md): un **número monótono dentro de lo firmado** que impide aceptar una versión anterior (un número de secuencia en un manifiesto de publicación). Los otros dos son de uso general: en [SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md), una **colección ordenada accesible por posición** (lista, tupla, cadena), y en [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), el **orden de ejecución de las tareas que respeta las dependencias**. La interfaz de secuencia como contrato de una colección tiene su propia entrada (*interfaz de secuencia*); aquí el foco es el sentido de seguridad de la cadena de suministro.

## Por qué importa

Una firma digital prueba que unos bytes fueron firmados con una clave, pero no que sean **recientes**. Un atacante que controle el canal de distribución puede reenviar un manifiesto antiguo, perfectamente firmado, que describe una versión con una vulnerabilidad ya conocida: es un ataque de *rollback* (retroceso). La decisión que cambia es qué se firma: no solo el contenido, sino también un contador que impide retroceder. [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) lo documenta como síntoma: se acepta una versión antigua vulnerable porque no hay secuencia ni caducidad en lo firmado.

## Cómo funciona

En el ejemplo de [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), la API de entregas publica un manifiesto (`release.json`) con nombre, versión, **número de secuencia** y las huellas del artefacto, del SBOM y de la procedencia, firmado con Ed25519 (el algoritmo de firma de curva elíptica especificado en el RFC 8032, con claves de 32 bytes y firmas de 64). El cliente:

1. Calcula la huella del archivo descargado.
2. Comprueba la firma del manifiesto con la **clave pública que ya incorpora**.
3. Comprueba el nombre.
4. **Rechaza una secuencia inferior a la mayor que recuerda.**
5. Falla cerrado ante cualquier discrepancia.

El número es *monótono* (solo sube) y está **dentro** de lo firmado: si estuviera fuera, un atacante lo cambiaría sin invalidar la firma. Esto responde a la limitación de la firma: la verificación correcta prueba que quien posee la clave privada firmó esos bytes, no que sean recientes ni benignos. [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) ofrece dos defensas complementarias: la **secuencia** y una **fecha de caducidad** en los metadatos, que obliga a renovarlos con regularidad.

## Ejemplo

El cliente guarda en disco la mayor secuencia vista y la compara antes de instalar:

```python
def aceptar(manifiesto, ultima_vista):
    if manifiesto["secuencia"] < ultima_vista:
        raise ValueError("retroceso: secuencia menor a la recordada")
    return manifiesto["secuencia"]
```

Un atacante reenvía el manifiesto de la secuencia 41, vulnerable, cuando el cliente ya vio la 44: se rechaza aunque la firma sea válida. Esta comprobación asume que el cliente conserva su estado; un cliente recién instalado no tiene secuencia recordada y no se protege del primer retroceso. Los otros sentidos son más simples: `secuencia[2]` accede por posición en una colección ordenada, y la secuencia de tareas de un plan es un orden compatible con sus dependencias (un orden topológico).

## Errores y confusiones comunes

- **Confundir los tres sentidos.** Una secuencia de seguridad es un contador, no una lista.
- **Poner la secuencia fuera de lo firmado.** Se puede alterar sin invalidar la firma.
- **Creer que la firma basta.** No prueba novedad.
- **No persistir la mayor secuencia vista.** El cliente olvida y acepta un retroceso.

## Límites y cuándo no aplica

La secuencia no protege del primer contacto: un cliente que nunca vio una versión no sabe cuál es la reciente. Tampoco sustituye la caducidad, que además fuerza la renovación aunque el atacante solo congele el canal. Y no responde a la pregunta de quién firmó ni de si el contenido es benigno; solo impide aceptar una versión anterior a la ya vista.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Colección](../c/coleccion.md), [Dependencia](../d/dependencia.md), [Tarea](../t/tarea.md), [Versión](../v/version.md), [Arrepentimiento](../a/arrepentimiento.md), [Comprensión](../c/comprension.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (592 clases más lo mencionan; las que más):

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Update Framework: especificación](https://theupdateframework.io/specification/) — actualizaciones seguras, secuencia y caducidad; autoridad: proyecto TUF, CNCF.
- [RFC 8032: EdDSA](https://www.rfc-editor.org/rfc/rfc8032) — algoritmo de firma Ed25519; autoridad: IETF.
- [Samuel et al., «Survivable key compromise in software update systems»](https://doi.org/10.1145/1866307.1866315) — diseño frente al compromiso de claves; autoridad: ACM CCS 2010.
- [Sigstore: documentación](https://docs.sigstore.dev/) — firma con identidades efímeras y registro de transparencia; autoridad: proyecto Sigstore, OpenSSF.
- [OpenSSL: pkeyutl](https://docs.openssl.org/3.0/man1/openssl-pkeyutl/) — firma y verificación en los experimentos; autoridad: proyecto OpenSSL.

---

[↑ Glosario](../../README.md) · [← Secretos y configuración](./secretos-y-configuracion.md) · [Secuencia de escape →](./secuencia-de-escape.md)
