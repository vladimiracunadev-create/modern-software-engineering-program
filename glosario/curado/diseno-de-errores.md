# Diseño de errores

## Definición

El **diseño de errores** es la práctica de decidir, antes de que ocurran, qué comunica un fallo a quien consume una biblioteca, un SDK o una CLI. `SE-118` lo resume en cuatro componentes de un error útil: **qué falló**, **contexto seguro**, **acción** que puede tomar quien lo recibe y una **referencia estable**. El error se trata como parte de la API pública y de la experiencia de quien desarrolla con el producto, no como un detalle interno que aparece al final.

## Por qué importa

Un error es, muchas veces, la primera «documentación» que alguien lee de verdad. Si dice solo «no funciona» o vuelca una traza interna, el consumidor abre una incidencia sin datos o abandona el producto. `SE-118` documenta ese síntoma: los reportes de error son «no funciona» sin datos, porque el mensaje no dice qué faltó ni cómo arreglarlo. La decisión que cambia es quién paga el costo del diagnóstico: con un error diseñado lo paga el autor una vez, al escribirlo; sin él, lo paga cada consumidor, cada vez.

## Cómo funciona

Cada componente tiene una razón:

- **Qué falló:** el nombre del problema en términos del dominio, no del código interno («configuración ausente», no «KeyError»).
- **Contexto seguro:** los datos que ayudan a entenderlo (clave que faltó, valor esperado, versión) **sin filtrar secretos**: ni tokens ni rutas personales.
- **Acción:** qué hacer a continuación («defina `CLIENTE_ID` o pase `--cliente`»).
- **Referencia estable:** un código o identificador que no cambia aunque cambie el texto, para buscar documentación o filtrar registros. `SE-118` advierte que no se debe obligar a **buscar texto cambiante**: si el contrato es el texto del mensaje, cualquier mejora de redacción rompe a quien lo analizaba.

Además, tipos de excepción, códigos de salida y documentación deben **contar la misma clasificación**. Si la API lanza `ErrorDeConfiguracion`, la CLI sale con un código asociado y la documentación lista el mismo nombre, el consumidor puede tratar el fallo de manera uniforme. La corrección que propone la clase es una **excepción propia con causa, solución y atributos estructurados**.

## Ejemplo

Un SDK que lee credenciales de un archivo. Un error pobre:

```python
raise Exception("error")
```

Un error diseñado, siguiendo los cuatro componentes (ilustración):

```python
class ErrorDeConfiguracion(Exception):
    codigo = "SDK-CFG-001"
    def __init__(self, clave, archivo):
        self.clave, self.archivo = clave, archivo
        super().__init__(
            f"[{self.codigo}] Falta la clave '{clave}' en '{archivo}'. "
            f"Agréguela o defina la variable de entorno {clave.upper()}."
        )
```

La referencia `SDK-CFG-001` es estable, el atributo `clave` permite programarla, y el mensaje no contiene valores sensibles. En la CLI, la misma clasificación se traduce a un código de salida concreto.

## Errores y confusiones comunes

- **Mensaje sin acción.** Dice qué pasó pero no qué hacer.
- **Incluir el valor del secreto.** «Token inválido: abc...» termina en registros y capturas.
- **Depender del texto.** Los consumidores analizan el mensaje y una mejora de redacción los rompe.
- **Clasificaciones distintas por capa.** La API, la CLI y la documentación nombran el mismo fallo de maneras diferentes.

## Límites y cuándo no aplica

Una evaluación interna de la experiencia de desarrollo no sustituye investigación diversa ni soporte real (`SE-118`): un error que parece claro a su autor puede no serlo para otras personas. Los mensajes muy detallados pueden revelar demasiado sobre el sistema cuando el consumidor no es de confianza (un servicio público); allí se devuelve una referencia y el detalle queda en registros internos. No todo error merece diseño: en código interno de vida corta, una excepción estándar con mensaje claro basta.
