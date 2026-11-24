# Valor esperado

## Definición

**Valor esperado** tiene dos sentidos en el programa, no relacionados entre sí. En `SE-534` (gestión de riesgos) es la suma de los resultados posibles ponderados por su probabilidad. En `SE-479` (cadena de suministro) es el dato (clave, constructor, repositorio, secuencia) que el verificador conoce *por fuera* del release que está comprobando.

## Por qué importa

En riesgos, ordenar por valor esperado evita mitigar lo que no pesa: `SE-534` señala que una matriz con celdas que agrupan valores muy distintos hace elegir mal. En verificación de releases, que el valor esperado provenga de fuera es lo que da sentido a la comprobación.

## Cómo funciona

**Sentido de riesgos.** Se multiplica probabilidad por impacto y se ordenan los riesgos por ese producto, con rangos para no fingir precisión. La matriz de colores agrupa cosas muy distintas en una celda; el valor esperado conserva la magnitud.

**Sentido de releases.** El verificador compara el release con valores obtenidos de un canal independiente (el contrato, un archivo de configuración versionado), nunca del mismo documento que verifica. Si los valores esperados se toman del release, un atacante que lo manipula manipula también lo que se espera.

## Ejemplo

`SE-479`: el equipo de seguridad guarda clave pública, nombre del producto, constructor y repositorio en configuración versionada obtenida del contrato, y registra la secuencia más alta aceptada para rechazar un release antiguo. `SE-534`: se generan carteras de treinta riesgos y se cuenta en cuántas el riesgo de mayor valor esperado no está entre los cinco que elige la matriz.

## Errores y confusiones comunes

- **El verificador acepta un release de otro constructor.** Valores esperados tomados del documento; usar configuración independiente y fijada de antemano.
- **Se mitigan riesgos que no pesan.** Matriz con celdas muy heterogéneas; ordenar por valor esperado con rangos.

## Límites y cuándo no aplica

Probabilidades e impactos estimados son inciertos: el producto da una falsa precisión si no se acompaña de rangos. Un valor esperado bajo no cubre eventos raros de impacto catastrófico, que se tratan aparte.
