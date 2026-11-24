# Adaptador

## Definición

Un **adaptador** es la pieza que traduce entre una capacidad local y un modelo común: de un lado habla el idioma de una plataforma, tecnología o colaborador concreto, y del otro cumple el contrato que el resto del sistema espera. `SE-030` lo define así para scripts portables. El programa lo usa con matices:

- **Portabilidad** (`SE-030`, `SE-036`, `SE-263`): implementa las capacidades de una plataforma concreta tras un contrato común.
- **Arquitectura** (`SE-328`): implementación de un puerto con una tecnología concreta (puertos y adaptadores).
- **Patrón estructural** (`SE-304`): traduce la interfaz de un colaborador a la que espera el cliente.

## Por qué importa

Sin adaptadores, las diferencias entre entornos se filtran por todo el código: cada lugar que necesita «el tipo de archivo» o «la versión instalada» conoce las rarezas de cada plataforma. Con ellos, esa diferencia vive en un solo sitio y el resto razona contra un contrato estable. Decide también dónde se prueba: el contrato se verifica una vez y cada adaptador se contrasta contra él.

## Cómo funciona

El mecanismo tiene tres partes. Primero, un **contrato externo** que fija nombres y valores (en `SE-030`, por ejemplo un esquema JSON). Segundo, un adaptador por entorno que consulta una fuente estable, valida y **normaliza** hacia ese contrato. Tercero, un consumidor que solo ve el modelo común. La causa de que funcione es que la traducción no comparte sintaxis como si fuera un lenguaje neutral: Bash entrega líneas de texto y PowerShell entrega objetos, así que cada uno convierte lo suyo a la forma común y conserva la salida original solo como detalle diagnóstico. Cuando una capacidad no existe, el adaptador lo declara (`unavailable`) en lugar de inventar un valor.

## Ejemplo

En `SE-030`, ambos adaptadores producen `{exists, type}` para una ruta, y las pruebas comparan campos, no presentación. En una herramienta que inventaría versiones en tres sistemas, el tablero no confunde «desconocido» con «versión cero» porque el adaptador informa `unavailable` cuando una política bloquea el acceso. Ilustración mínima:

```python
class AdaptadorLinux:
    def info(self, ruta): return {"exists": os.path.exists(ruta), "type": "file"}
```

## Errores y confusiones comunes

- **Kit multiplataforma convertido en un script de cien comandos.** Causa: no hay modelo ni contrato; corrección: separar capacidades, adaptadores y decisiones (`SE-036`).
- **Un adjunto se guarda en una plataforma y no en otra.** Causa: reglas de nombres distintas; corrección: sanear el nombre en el adaptador y probar en ambas (`SE-263`).
- **Las pruebas pasan y el sistema real falla.** Causa: el doble se desvió del adaptador real; corrección: una suite de contrato ejecutada contra ambos (`SE-328`).

## Límites y cuándo no aplica

Un adaptador sin contrato explícito solo mueve el desorden de sitio. Si solo existe un entorno y no se espera otro, la capa añade indirección sin beneficio. Tampoco elimina las diferencias reales: lo que una plataforma no puede hacer se declara, no se simula. Y el patrón estructural de `SE-304` traduce una interfaz; no resuelve diferencias de semántica más profundas entre sistemas.
