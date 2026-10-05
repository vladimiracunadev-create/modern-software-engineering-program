# 🌍 Internationalization Engineer

> Diseña productos que representan idioma, texto, tiempo, número y dirección sin
> codificar supuestos culturales imposibles de corregir al traducir.
>
> **Entrada habitual:** semi-senior · **Foco:** i18n, l10n y datos globales
> · **Evidencia central:** flujo probado en varios locales, zonas horarias y RTL

## 🧭 Qué es y por qué importa

Internationalization engineering separa contenido, representación y lógica para que
un producto pueda localizarse sin bifurcar código. Atiende Unicode, pluralización,
calendarios, moneda, zonas horarias, layout y operación del catálogo de traducciones.

## 🗓️ Un día en el puesto

- detectar texto concatenado o supuesto de formato;
- revisar identificadores y contexto de traducción;
- reproducir un fallo de zona horaria o normalización Unicode;
- probar expansión de texto y dirección RTL;
- coordinar localización, QA, contenido y release.

## ✅ Responsabilidades y límites

- Responde por arquitectura y herramientas de internacionalización.
- Distingue almacenar un instante de presentarlo en un contexto humano.
- No traduce mecánicamente términos de dominio sin contexto.
- No afirma soporte de un locale que no fue probado ni mantenido.

## 🧠 Qué necesitas saber

Unicode, normalización, graphemes, locale, CLDR, pluralización, fechas, calendarios,
zonas horarias, monedas, collation, RTL, recursos, pseudo-localización, accesibilidad,
testing y workflow de traducción.

## 📚 Tu ruta en el programa

1. Partes 01 y 03–09 para representación y software base.
2. Partes 10–13 para usuarios, dominio y contratos.
3. [Parte 14](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md) como núcleo.
4. Partes 19–21 y 26 para interfaces, APIs y persistencia.
5. Partes 30, 33–34 para pruebas, release y automatización.

## 🧪 Evidencia de portafolio

- matriz de locales, formatos, zonas y fallback;
- pseudo-localización en CI;
- pruebas de cambio horario, Unicode compuesto y RTL;
- proceso versionado de extracción, traducción y entrega.

## 📈 Progresión

Frontend/Mobile/Localization Engineer → I18n Engineer → Globalization Architect.

## ⚠️ Mitos frecuentes

- “i18n es traducir strings.” Los supuestos viven también en datos y layout.
- “UTF-8 resuelve Unicode.” No resuelve segmentación, normalización ni visualización.
- “UTC evita zonas horarias.” Ayuda a almacenar instantes, no decisiones civiles.

## 🚀 Siguientes pasos

1. Audita supuestos de idioma, longitud, tiempo y número.
2. Activa pseudo-localización y RTL antes de traducir.
3. Reproduce un cambio de horario y documenta la semántica correcta.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
