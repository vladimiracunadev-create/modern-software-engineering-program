# ⚙️ Systems Programmer

> Construye software cercano al sistema operativo y al runtime con control explícito
> de memoria, concurrencia, recursos, interfaces y portabilidad.
>
> **Entrada habitual:** semi-senior · **Foco:** runtimes, procesos y rendimiento
> · **Evidencia central:** componente medido con invariantes y fallos de recursos probados

## 🧭 Qué es y por qué importa

Systems programming crea runtimes, motores, drivers, bases de datos, herramientas y
componentes donde una abstracción insuficiente se convierte en corrupción, deadlock o
degradación. Exige razonar desde hardware y sistema operativo hasta API pública.

## 🗓️ Un día en el puesto

- depurar memoria, syscall, bloqueo o carrera;
- perfilar CPU, caché e I/O;
- diseñar una interfaz estable y manejo de recursos;
- revisar comportamiento indefinido y portabilidad;
- ejecutar fuzzing, sanitizers y benchmarks.

## ✅ Responsabilidades y límites

- Responde por seguridad de memoria, recursos y semántica de concurrencia.
- Elige C, C++, Rust u otra herramienta por restricciones verificadas.
- No usa bajo nivel como sinónimo de rendimiento sin medir.
- No expone primitivas peligrosas sin contrato y encapsulación.

## 🧠 Qué necesitas saber

Arquitectura de computador, memoria, procesos, syscalls, compilación, linking,
ABI, concurrencia, estructuras de datos, redes, archivos, debugging, profiling,
property testing, fuzzing, portabilidad y reproducible builds.

## 📚 Tu ruta en el programa

1. [Parte 01 — Computadores y representación](../classes/part-01-computadores-y-representacion-de-informacion/README.md) y partes 02–09 como núcleo de máquina, programación y herramientas.
2. Partes 18 y 22 para servicios, automatización y embedded.
3. Partes 24, 26 y 28 para diseño, almacenamiento y concurrencia.
4. Partes 30–33 para pruebas, resiliencia, seguridad y build.

## 🧪 Evidencia de portafolio

- biblioteca o servicio con contrato de recursos;
- benchmark y perfil reproducibles;
- prueba de carrera, agotamiento y recuperación;
- build portable con sanitizers, fuzzing y artefacto verificable.

## 📈 Progresión

Software Engineer → Systems Programmer → Senior/Staff Systems → Runtime/Platform Architect.

## ⚠️ Mitos frecuentes

- “Bajo nivel siempre es más rápido.” Diseño y acceso a datos suelen dominar.
- “Compilar significa seguro.” No prueba carreras ni límites de recursos.
- “Portabilidad es evitar APIs nativas.” Requiere contratos y entornos comprobados.

## 🚀 Siguientes pasos

1. Define invariantes de memoria, tiempo y recursos.
2. Mide antes de reemplazar una abstracción.
3. Inyecta agotamiento, cancelación y concurrencia adversa.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
