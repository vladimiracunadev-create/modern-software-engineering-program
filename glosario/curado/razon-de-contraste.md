# Razón de contraste

## Definición

La **razón de contraste** es el cociente (L1 + 0,05) / (L2 + 0,05) entre las luminancias relativas del color más claro (L1) y del más oscuro (L2) (SE-173, SE-175, SE-229, SE-442). Mide cuánto se distinguen dos colores, típicamente texto y fondo, y va de 1:1 (idénticos) a 21:1 (negro sobre blanco).

## Por qué importa

Convierte «que se lea bien» en un número que se puede exigir y vigilar. Elegir colores a ojo falla a menudo: lo que parece legible para quien diseña no lo es con baja visión, con sol en la pantalla o en una impresión en gris. Cambia la decisión de diseño: se calcula y se comprueba, y el umbral pasa a ser parte del presupuesto de accesibilidad.

## Cómo funciona

La **luminancia relativa** L de un color se calcula a partir de sus componentes rojo, verde y azul linealizados y ponderados según la sensibilidad del ojo: el verde pesa mucho más que el azul. Con L1 la del color más claro y L2 la del más oscuro, la razón es (L1 + 0,05) / (L2 + 0,05); el 0,05 modela la luz ambiente y evita la división por cero con negro.

SE-173 recoge los **mínimos**: **4,5:1** para texto normal y **3:1** para texto grande y componentes de interfaz (bordes de campos, iconos). Son los criterios de las pautas de accesibilidad web. SE-173 añade una regla complementaria: el **color no puede ser la única señal** de un estado; un error indicado solo en rojo no se distingue para personas con daltonismo ni en una impresión en gris, de modo que se acompaña con texto o un icono.

SE-442 incluye la razón de contraste entre los **presupuestos** de una página: un límite medible con dueño, un umbral con una razón, una medición automática y una acción al superarlo. A diferencia del peso o del tiempo de carga, el contraste es determinista y se comprueba en integración continua sobre la hoja de estilos. El presupuesto captura una parte de la experiencia (la legibilidad del color) y deja fuera otras (tamaño de letra, espaciado, foco), que requieren otras medidas.

## Ejemplo

Texto gris medio sobre fondo blanco: si la luminancia del gris es L2 = 0,2 y la del blanco L1 = 1, la razón es (1 + 0,05) / (0,2 + 0,05) = 4,2: no alcanza el 4,5:1 para texto normal, aunque «se vea bien» en un monitor nuevo. Oscurecer el gris hasta L2 = 0,18 da 4,57 y cumple. (Cálculo propio con la fórmula de SE-173; las luminancias son de ejemplo.)

## Errores y confusiones comunes

- **Elegir colores sin calcular.**
- **Usar solo el color para señalar un estado.**
- **Aplicar el umbral de texto normal a texto grande o al revés.**
- **Medir contraste sobre imágenes o degradados** con un único valor.

## Límites y cuándo no aplica

La razón es una aproximación de la percepción: no capta toda la legibilidad (tipografía, tamaño, espaciado) ni condiciones como el modo oscuro. Cumplir el mínimo no certifica accesibilidad: es una condición necesaria. En logotipos y elementos decorativos las pautas no exigen un contraste mínimo.
