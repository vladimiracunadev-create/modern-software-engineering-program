# Operabilidad

## Definición

La **operabilidad** es la capacidad de un dispositivo de ser mantenido durante su vida útil por personas que no lo construyeron. Es el sentido de `SE-276` (proyecto: dispositivo simulado operable y actualizable). Aquí se aplica a un dispositivo; la idea general (que un sistema pueda operarse con seguridad por otros) la comparten otros textos del programa, pero esta entrada sigue la definición de la clase.

## Por qué importa

Un dispositivo desplegado vive años. Si cada incidente exige a quien lo construyó, el sistema solo funciona mientras esa persona esté. `SE-276` lo plantea así: un dispositivo operable tolera cortes, cuelgues y actualizaciones sin visita.

## Cómo funciona

Un dispositivo es operable si una persona que no lo construyó puede mantenerlo vivo durante años. `SE-276` lista lo que esa persona debe saber hacer:

- **Actualizarlo** (y volver atrás si falla).
- **Saber qué pasa cuando falla.**
- **Retirar una clave.**
- **Detectar que dejó de enviar.**

La clase define la operabilidad como el conjunto de las defensas de la parte visto desde quien las usa: la actualización con ranuras, el temporizador de vigilancia, la rotación de claves y revocación, la telemetría. Se hace explícita en el **paquete del dispositivo**, un documento de nueve secciones que hace revisable lo decidido.

## Ejemplo

El equipo de la plataforma en `SE-276` entrega el paquete de los 200 nodos: la identidad es una clave derivada por dispositivo desde un secreto maestro que nunca está en el nodo; el firmware tiene dos ranuras con reversión a los 60 s; las claves se rotan cada doce meses con una lista de revocación; los umbrales son de 5 a 40 °C con variación máxima de 3 °C por muestra y una referencia independiente de CO₂.

## Errores y confusiones comunes

- **El paquete pasa el validador y falla en la flota:** el validador comprobaba forma, no sentido. Corrección: reglas de sentido y revisión humana (`SE-276`).
- **Nadie sabe qué hacer ante un nodo mudo:** falta el procedimiento y la responsabilidad.
- **Confundirla con facilidad de uso:** se mide por lo que un tercero puede hacer sin ayuda del autor.
- **Documentar sin probar:** operar exige haber ensayado la actualización y el retroceso.

## Límites y cuándo no aplica

La clase usa un dispositivo simulado: no prueba que un dispositivo físico sea operable. La operabilidad no sustituye la seguridad ni el diseño del producto; es una propiedad sobre cómo se mantiene. Y depende de que alguien asuma la responsabilidad que el paquete declara.
