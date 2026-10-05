# ⏱️ Performance Engineer

> Convierte objetivos de velocidad, capacidad y eficiencia en experimentos
> reproducibles, diagnósticos causales y decisiones de arquitectura.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** profiling, carga y capacidad
> · **Evidencia central:** cuello de botella demostrado y mejora medida sin regresión

## 🧭 Qué es y por qué importa

Performance engineering no optimiza por intuición. Define carga, presupuesto y
percentiles; mide el sistema completo, localiza la restricción y comprueba que la
mejora no trasladó el problema a coste, corrección o mantenibilidad.

## 🗓️ Un día en el puesto

- diseñar benchmark o perfil de carga representativo;
- analizar CPU, memoria, I/O, red y colas;
- correlacionar trazas con percentiles y saturación;
- validar una optimización y sus trade-offs;
- proyectar capacidad y riesgo de crecimiento.

## ✅ Responsabilidades y límites

- Responde por método, representatividad y reproducibilidad de mediciones.
- Distingue latencia, throughput, utilización y saturación.
- No publica un promedio cuando la cola importa.
- No optimiza código sin confirmar el cuello de botella.

## 🧠 Qué necesitas saber

Arquitectura de computadores, runtimes, profiling, benchmarking, estadística básica,
carga/stress/spike/soak, colas, caché, bases de datos, redes, tracing, capacity
planning, performance budgets y coste.

## 📚 Tu ruta en el programa

1. Partes 01–08 para máquina, algoritmos, medición y profiling.
2. Partes 19–20 y 26–29 para superficies, datos y distribución.
3. [Parte 31 — Calidad, rendimiento y resiliencia](../classes/part-31-calidad-rendimiento-y-resiliencia/README.md).
4. Partes 34–35 para entrega, observación y capacidad.

## 🧪 Evidencia de portafolio

- benchmark con entorno, carga, warm-up y variabilidad declarados;
- perfil que localice el cuello de botella;
- resultados p50/p95/p99 antes/después;
- modelo de capacidad y presupuesto con límites.

## 📈 Progresión

Software/SRE Engineer → Performance Engineer → Senior/Staff Performance o Architect.

## ⚠️ Mitos frecuentes

- “Más rápido en mi equipo es mejor.” Sin entorno y carga no hay comparación.
- “El promedio representa usuarios.” Las colas aparecen en percentiles y tails.
- “Optimizar siempre compensa.” Puede añadir complejidad mayor que el beneficio.

## 🚀 Siguientes pasos

1. Define una pregunta y presupuesto antes de medir.
2. Repite la carga y cuantifica variabilidad.
3. Cambia una causa, vuelve a medir y busca regresiones.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
