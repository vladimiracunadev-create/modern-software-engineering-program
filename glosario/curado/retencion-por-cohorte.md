# Retención por cohorte

## Definición

La **retención por cohorte** es la fracción de las personas que empezaron en un periodo (la cohorte) y repiten la tarea útil k periodos después (SE-136). Una **cohorte** es el grupo que empezó en un mismo periodo; la retención de la semana k es la fracción de ese grupo que realiza la tarea útil en esa semana.

## Por qué importa

Responde si quienes llegaron vuelven, sin mezclar edades. Las cifras agregadas (usuarios activos totales) combinan a quien lleva dos días con quien lleva dos meses, y un crecimiento de captación puede ocultar una fuga. Cambia cómo se lee la salud de un producto: se mira la curva de cada cohorte y si las nuevas se comportan mejor o peor que las antiguas.

## Cómo funciona

Se definen la **tarea útil** (el evento que cuenta como retorno: una entrega aceptada, no solo abrir la aplicación; SE-136 la desarrolla) y el periodo (semana, mes). Para cada cohorte se calcula, por cada k, el porcentaje de sus integrantes que realizó la tarea en la semana k. Se dibuja una tabla o curva por cohorte.

SE-136 insiste en **comparar cohortes de la misma edad**: la retención de la semana 1 de la cohorte de ayer no es comparable con la de la semana 12 de hace seis meses. Dos errores frecuentes con causa conocida. El primero: la retención «mejora» sola en las cohortes nuevas porque se contó a quienes no han cumplido la ventana; la corrección es medir solo **cohortes completas** y rotular las parciales. El segundo: dos paneles dan DAU/MAU de 28 % y 8 % porque usan distinto evento de «activo»; la corrección es publicar el evento y la ventana en cada cifra.

La retención por cohorte se conecta con la actividad (que la mide en bruto) y con el resultado (la tarea útil es una aproximación al valor): una retención alta sobre actividad vacía es una señal engañosa.

## Ejemplo

La cohorte de estudiantes que se registraron en la semana 1 tiene 200 personas. En la semana 4, 90 realizan al menos una entrega: la retención de semana 4 es 45 %. La cohorte de la semana 5, con 300 personas, tiene en su semana 4 un 54 %. La comparación es válida porque ambas están a la misma edad; si se comparara la semana 4 de la primera con la semana 1 de la quinta, no. (Cifras ilustrativas.)

## Errores y confusiones comunes

- **La retención «mejora» sola en las cohortes nuevas**: se contó a quienes no cumplieron la ventana.
- **Dos paneles con DAU/MAU distinto**: distinto evento de activo.
- **Usar abrir la aplicación como retorno**: es actividad, no tarea útil.
- **Mirar solo el promedio de todas las cohortes**: reaparece la mezcla de edades.

## Límites y cuándo no aplica

Con cohortes pequeñas, el porcentaje tiene mucha incertidumbre (intervalos anchos). En productos de uso naturalmente esporádico (una vez al año), las ventanas semanales no tienen sentido. La retención no dice por qué se fue la gente, solo que se fue; para eso hacen falta entrevistas. Los datos de SE-136 son sintéticos y muestran el método.
