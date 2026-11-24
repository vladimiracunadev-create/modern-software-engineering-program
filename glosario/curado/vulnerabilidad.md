# Vulnerabilidad

## Definición

Una **vulnerabilidad** es una debilidad en un sistema que una persona atacante puede aprovechar para vulnerar una propiedad de seguridad (`SE-465`): confidencialidad, integridad o disponibilidad.

## Por qué importa

La palabra se usa para todo, desde un error teórico hasta una brecha explotada; lo que cambia la decisión es cuán explotable es en *tu* contexto y qué activo pone en riesgo. Confundir presencia con riesgo lleva a discutir puntajes en vez de actuar.

## Cómo funciona

`SE-465` trata la gestión: un canal de reporte con responsable y plazo (por ejemplo, un archivo `security.txt`, un buzón con suplentes y acuse automático) y una evaluación que no se reduce al puntaje CVSS. CVSS describe la gravedad técnica de un defecto en abstracto; el riesgo depende además de la exposición, de si hay explotación conocida y del activo afectado. Por eso la clase pide dejar el vector a la vista, calcular el puntaje ambiental y adjuntar evidencia de explotación.

## Ejemplo

Dos dependencias vulnerables con el mismo puntaje base: una está en un servicio expuesto a internet y la otra en una herramienta interna sin datos. Se corrige primero la expuesta.

## Errores y confusiones comunes

- **Un reporte se publica sin respuesta.** El canal no tiene responsable ni plazo; `security.txt`, buzón con suplentes y acuse automático.
- **Se discute el puntaje en vez del riesgo.** CVSS tratado como medida; vector a la vista, puntaje ambiental y evidencia de explotación.

## Límites y cuándo no aplica

Una vulnerabilidad conocida no implica que haya sido explotada, ni su ausencia en una base pública que el sistema sea seguro: solo se reportan las que alguien encontró y publicó.
