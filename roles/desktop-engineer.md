# 🖥️ Desktop Engineer

> Construye aplicaciones de escritorio integradas con el sistema operativo, capaces
> de instalarse, actualizarse y recuperar estado con seguridad.
>
> **Entrada habitual:** junior/semi-senior · **Foco:** clientes ricos y distribución
> · **Evidencia central:** aplicación instalable con actualización y rollback probados

## 🧭 Qué es y por qué importa

Una aplicación de escritorio administra ventanas, archivos, procesos, integración
nativa y largos periodos de uso. Debe sobrevivir a cierres abruptos, configuraciones
heterogéneas y actualizaciones que no pueden dejar al usuario sin herramienta.

## 🗓️ Un día en el puesto

- depurar un fallo específico de Windows, macOS o Linux;
- diseñar persistencia local y recuperación tras cierre inesperado;
- revisar firma, empaquetado, permisos e instalador;
- medir arranque, memoria y responsividad;
- validar teclado, escalado, lectores de pantalla y actualización.

## ✅ Responsabilidades y límites

- Responde por ciclo de vida, integración nativa y distribución del cliente.
- Declara con precisión plataformas y versiones probadas.
- No trata el sistema de archivos del usuario como almacenamiento descartable.
- No afirma portabilidad basándose solo en que el framework compila.

## 🧠 Qué necesitas saber

Procesos, archivos, IPC, UI y accesibilidad; almacenamiento y migración local;
empaquetado, firma y actualización; concurrencia, rendimiento, crash diagnostics,
seguridad de plugins y diferencias entre plataformas.

## 📚 Tu ruta en el programa

1. Partes 01–09 para máquina, sistema operativo y construcción.
2. Partes 13–14 y 17–18 para contratos, UX, documentación y procesos.
3. [Parte 21](../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) como núcleo.
4. Partes 26, 30–33 y 35 para persistencia, pruebas, supply chain y diagnóstico.
5. Parte 36 para migración, compatibilidad y retiro.

## 🧪 Evidencia de portafolio

- instaladores reproducibles para dos plataformas declaradas;
- recuperación de documento tras cierre forzado;
- actualización firmada con rollback;
- matriz de accesibilidad, rendimiento y compatibilidad observada.

## 📈 Progresión

Desktop Junior → Desktop Engineer → Senior → Staff Client Platform o Architect.

## ⚠️ Mitos frecuentes

- “Desktop está obsoleto.” Sigue siendo apropiado para integración, offline y trabajo intensivo.
- “Electron/nativo resuelve portabilidad.” Cada opción cambia coste, superficie y operación.
- “Actualizar es reemplazar un binario.” Incluye datos, plugins y procesos activos.

## 🚀 Siguientes pasos

1. Define plataformas soportadas y un entorno de prueba real.
2. Provoca una interrupción durante guardado y recuperación.
3. Empaqueta, firma y revierte una actualización controlada.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
