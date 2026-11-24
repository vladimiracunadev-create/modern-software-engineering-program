# Secuencia

## Definición

La palabra **secuencia** tiene en el programa tres sentidos, y esta entrada los separa. El **principal** viene de `SE-473`: un **número monótono dentro de lo firmado** que impide aceptar una versión anterior (un número de secuencia en un manifiesto de publicación). Los otros dos son de uso general: en `SE-066`, una **colección ordenada accesible por posición** (lista, tupla, cadena), y en `SE-141`, el **orden de ejecución de las tareas que respeta las dependencias**. La interfaz de secuencia como contrato de una colección tiene su propia entrada (*interfaz de secuencia*); aquí el foco es el sentido de seguridad de la cadena de suministro.

## Por qué importa

Una firma digital prueba que unos bytes fueron firmados con una clave, pero no que sean **recientes**. Un atacante que controle el canal de distribución puede reenviar un manifiesto antiguo, perfectamente firmado, que describe una versión con una vulnerabilidad ya conocida: es un ataque de *rollback* (retroceso). La decisión que cambia es qué se firma: no solo el contenido, sino también un contador que impide retroceder. `SE-473` lo documenta como síntoma: se acepta una versión antigua vulnerable porque no hay secuencia ni caducidad en lo firmado.

## Cómo funciona

En el ejemplo de `SE-473`, la API de entregas publica un manifiesto (`release.json`) con nombre, versión, **número de secuencia** y las huellas del artefacto, del SBOM y de la procedencia, firmado con Ed25519 (el algoritmo de firma de curva elíptica especificado en el RFC 8032, con claves de 32 bytes y firmas de 64). El cliente:

1. Calcula la huella del archivo descargado.
2. Comprueba la firma del manifiesto con la **clave pública que ya incorpora**.
3. Comprueba el nombre.
4. **Rechaza una secuencia inferior a la mayor que recuerda.**
5. Falla cerrado ante cualquier discrepancia.

El número es *monótono* (solo sube) y está **dentro** de lo firmado: si estuviera fuera, un atacante lo cambiaría sin invalidar la firma. Esto responde a la limitación de la firma: la verificación correcta prueba que quien posee la clave privada firmó esos bytes, no que sean recientes ni benignos. `SE-473` ofrece dos defensas complementarias: la **secuencia** y una **fecha de caducidad** en los metadatos, que obliga a renovarlos con regularidad.

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
