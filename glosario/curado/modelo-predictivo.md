# Modelo predictivo

## Definición

El **modelo predictivo** organiza el trabajo en fases (analizar, diseñar, construir, probar, entregar) con alcance, coste y plazo comprometidos al inicio, y retroalimentación concentrada hacia el final (SE-181). También se le llama en cascada o plan-driven. No es un sinónimo de «malo» ni de «obsoleto».

## Por qué importa

Es eficiente cuando lo desconocido es poco. Comprometer alcance, coste y plazo desde el inicio facilita la coordinación, los contratos y la planificación de dependencias. Cambia la decisión de cómo organizar un proyecto: no se elige un modelo por moda sino por la cantidad de incertidumbre del trabajo.

## Cómo funciona

En un modelo predictivo se analiza, diseña, construye, prueba y entrega en fases, con el alcance fijado al inicio. Su **fuerza es la coordinación**: todos saben qué se hará y las dependencias se resuelven en el papel (proveedores, fechas, contratos). Su **debilidad** está en el momento en que se descubre un malentendido: ocurre cuando alguien usa lo construido, y entonces todo lo hecho sobre ese malentendido se rehace. El costo de rehacer crece con lo construido encima, de modo que descubrirlo al final es lo más caro.

SE-181 subraya que el modelo **no es ingenuo ni obsoleto**: funciona donde el trabajo es conocido, los requisitos estables, las interfaces con terceros están acordadas y cambiar es caro. Por eso en la plataforma de entregas la integración con el sistema de calificaciones de secretaría, con fecha fija y proveedor externo, se planifica de forma predictiva con un contrato de interfaz acordado de antemano, mientras que la experiencia de entrega (alta incertidumbre) se construye en ciclos.

La clase lo contrasta con los otros dos modelos con un análisis de costos: lo que enseña no es el número sino la **forma** del costo. En el predictivo, el costo de un error de requisito crece con el avance; en el iterativo, se paga una sobrecarga por ciclo a cambio de errores más baratos. La decisión depende de cuánto desconocido hay.

## Ejemplo

Un contrato de interfaz con un proveedor de calificaciones: formatos, campos, plazos y pruebas de aceptación acordados al inicio, con fecha de entrega fija. Se analiza, se diseña la interfaz, se construye y se prueba contra el entorno del proveedor, y se entrega en la fecha. Cambiar el formato a mitad de camino sería caro, y por eso el contrato lo fija. (Ilustración del caso de SE-181.)

## Errores y confusiones comunes

- **Usarlo cuando hay mucha incertidumbre**: el malentendido se descubre tarde.
- **Considerarlo anticuado por definición.**
- **Comprometer alcance, coste y plazo sin margen para riesgos.**
- **Confundir predictivo con planificar**: todo modelo planifica; difiere cuánto se compromete y cuándo se revisa.

## Límites y cuándo no aplica

No aplica bien a productos nuevos con usuarios que no saben qué necesitan, ni a entornos donde los requisitos cambian durante el desarrollo. Los números del análisis de costos de SE-181 son supuestos del autor. En la práctica casi todos los proyectos mezclan modelos según la parte del trabajo.
