# 🔌 Embedded & IoT Engineer

> Integra firmware, hardware, conectividad y operación de dispositivos dentro de
> presupuestos explícitos de tiempo, memoria, energía y seguridad.
>
> **Entrada habitual:** semi-senior · **Foco:** firmware, RTOS, telemetría y OTA
> · **Evidencia central:** dispositivo o simulación con deadlines y recuperación medidos

## 🧭 Qué es y por qué importa

Embedded engineering trabaja donde el software toca el mundo físico. Un bloqueo puede
agotar batería, perder telemetría o afectar un proceso real. IoT añade flotas, identidad,
redes inestables y actualizaciones remotas que deben fallar de forma segura.

## 🗓️ Un día en el puesto

- leer una hoja de datos y verificar una interfaz hardware/software;
- medir latencia, jitter, memoria o consumo;
- depurar una carrera, interrupción o watchdog;
- revisar protocolo, identidad y amenaza física;
- desplegar OTA por etapas y confirmar recuperación.

## ✅ Responsabilidades y límites

- Responde por comportamiento temporal, recursos y actualización del dispositivo.
- Distingue hard real-time de baja latencia deseable.
- No oculta incertidumbre física detrás de una abstracción de software.
- No ejecuta pruebas peligrosas en hardware sin entorno y procedimiento seguros.

## 🧠 Qué necesitas saber

Arquitectura de computadores, C/C++ o Rust según contexto, memoria, interrupciones,
RTOS, buses y protocolos; energía, telemetría, criptografía aplicada, secure boot,
OTA, edge, safety y diagnóstico con instrumentación.

## 📚 Tu ruta en el programa

1. Partes 00–09, con énfasis en 01–04 y 07–08.
2. [Parte 22 — Embedded, IoT y tiempo real](../classes/part-22-embedded-iot-y-tiempo-real/README.md).
3. Partes 23, 27–28 para dominio crítico, mensajería y concurrencia.
4. Partes 30–35 para pruebas, resiliencia, seguridad, entrega y telemetría.
5. Parte 36 para EOL y retirada de flotas.

## 🧪 Evidencia de portafolio

- simulación o placa con presupuesto temporal y energético;
- prueba de watchdog, brownout y pérdida de red;
- modelo de amenazas físicas y remotas;
- OTA firmada con partición de recuperación y plan de flota.

## 📈 Progresión

Firmware Junior → Embedded Engineer → Senior → Systems/Platform Lead o Architect.

## ⚠️ Mitos frecuentes

- “Tiempo real significa rápido.” Significa cumplir límites temporales definidos.
- “El dispositivo está aislado.” Fabricación, debug y OTA forman una cadena de confianza.
- “Una vez vendido, termina el soporte.” Vulnerabilidades y certificados siguen venciendo.

## 🚀 Siguientes pasos

1. Define presupuesto de memoria, tiempo y energía antes de implementar.
2. Inyecta reinicio y pérdida de conectividad en una simulación segura.
3. Documenta actualización, recuperación y retiro del dispositivo.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
