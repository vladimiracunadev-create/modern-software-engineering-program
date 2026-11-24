# Regla de negocio

## Definición

Una **regla de negocio** es una decisión de la organización, independiente del sistema, sobre qué se acepta, se calcula o se rechaza (SE-146). Existiría aunque no hubiera software: «una entrega en gracia pierde el 10 % de la nota» es una regla de la institución, no del sistema.

## Por qué importa

Pertenece a la organización y cambia con la política, no con el código. Distinguirla del requisito funcional importa por **quién puede cambiarla**: la coordinación académica cambia la regla; el equipo cambia el modo de aplicarla. Si la regla vive solo en el código, cada cambio de política es un cambio de software y solo el equipo lo entiende.

## Cómo funciona

SE-146 separa dos cosas. La **regla** dice qué se aplica («una entrega en gracia pierde el 10 %»). El **requisito funcional** dice cómo el sistema la aplica («calculará la nota final aplicando BR-07»). Esa separación permite que quien decide la política la cambie sin tocar el código, y que el requisito cambie solo cuando cambia **cómo** se aplica la regla.

La práctica de la clase es darle a la regla **identificador, texto, responsable y fecha**, registrada aparte del requisito que la aplica. El identificador permite referirla desde requisitos, pruebas y código; el responsable dice a quién preguntar; la fecha, desde cuándo rige. Y vive en **un solo punto**: el síntoma de lo contrario es que dos módulos calculan una nota distinta para la misma entrega porque la regla vive duplicada y cada copia evolucionó por su lado. La corrección es extraerla a un único lugar con identificador y responsable.

Las reglas con varias condiciones se especifican con tablas de decisión, para enumerar las combinaciones y detectar huecos: otro síntoma que la clase señala es que el comité de política pregunta «¿qué pasa si…?» y nadie lo sabe, porque se redactaron solo los casos felices. La regla también se conecta con las obligaciones externas, que son reglas impuestas desde fuera y no se negocian.

## Ejemplo

BR-07: «Una entrega en gracia pierde el 10 % de la nota». Responsable: coordinación académica. Vigente desde: inicio del semestre. Requisito que la aplica: «Cuando una estudiante envíe una entrega después del plazo y dentro de la gracia, el sistema calculará la nota final aplicando BR-07 y mostrará el descuento». Si la coordinación cambia el 10 % al 15 %, cambia la regla; el requisito no cambia. (Ejemplo basado en SE-146.)

## Errores y confusiones comunes

- **Dos módulos calculan notas distintas**: regla duplicada.
- **Mezclar regla y requisito** en la misma frase.
- **Reglas sin responsable**: nadie decide cuando hay duda.
- **Confundirla con una restricción técnica**: la regla viene de la organización.

## Límites y cuándo no aplica

No toda condición del sistema es una regla de negocio; las restricciones técnicas (límites de memoria) son otra cosa. En organizaciones sin proceso de decisión claro, la regla puede no tener responsable real. Y una regla muy volátil puede justificar sacarla a configuración.
