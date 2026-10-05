# 🏛️ Software Architect

> Alinea contexto, restricciones, atributos de calidad y evolución; hace explícitas
> decisiones difíciles sin convertirse en una autoridad separada de la implementación.
>
> **Entrada habitual:** senior/staff · **Foco:** límites y decisiones sistémicas ·
> **Evidencia central:** arquitectura defendible que sobrevive al contacto con operación

## 🧭 Qué es y por qué importa

La arquitectura son decisiones de alto impacto y alto coste de cambio. El rol ayuda a
formular el problema, comparar alternativas y mantener coherencia entre equipos. Puede
ser una responsabilidad distribuida o un cargo formal. En ambos casos, la credibilidad
depende de conectar diagramas con código, datos, despliegue y consecuencias.

## 🗓️ Un día en el puesto

- facilitar discovery de atributos de calidad y restricciones;
- revisar un ADR/RFC y tensionar supuestos;
- modelar límites, flujos de datos y escenarios de fallo;
- acompañar un spike o implementación para validar una hipótesis;
- coordinar evolución entre equipos y contratos;
- revisar costes, riesgos, observabilidad y estrategia de migración.

## ✅ Responsabilidades y límites

- Responde por la calidad de la decisión y su trazabilidad, no por dibujar cajas.
- Mantiene opciones reversibles cuando la evidencia es insuficiente.
- No prescribe tecnología sin contexto ni benchmark pertinente.
- No centraliza cada decisión ni bloquea a los equipos.
- No desaparece después del diseño: verifica comportamiento en producción.

## 🧠 Qué necesitas saber

- requisitos y atributos de calidad;
- modularidad, DDD, integración, datos y sistemas distribuidos;
- estilos arquitectónicos y sus costes operacionales;
- seguridad, privacidad, resiliencia, rendimiento y compliance;
- economía, build-vs-buy, FinOps y evolución legacy;
- facilitación, negociación, comunicación visual y escritura de ADR/RFC.

## 📚 Tu ruta en el programa

1. Partes 00 y 10–17 para profesión, producto, requisitos y decisiones.
2. Partes 20 y 23 para servicios y restricciones de dominio.
3. Parte 24 y [Parte 25 — Arquitectura de software y dominio](../classes/part-25-arquitectura-de-software-y-dominio/README.md), seguidas por datos, eventos, distribución y cloud.
4. Partes 30–35 para calidad, seguridad, entrega y operación.
5. Partes 36–37 para evolución y arquitectura sociotécnica.
6. Partes 38–39 para revisar arquitectura y agentes sin delegar criterio.

## 🧪 Evidencia de portafolio

- escenarios de atributos de calidad vinculados a requisitos;
- ADR con alternativas, costes, señales de revisión y decisión reversible;
- vistas de contexto, contenedores, datos y despliegue interpretadas;
- experimento que invalida o sostiene una decisión;
- plan de migración compatible con checkpoints y rollback;
- revisión posterior que compara predicción con comportamiento observado.

## 📈 Progresión

Senior Engineer → Staff/Principal → Architect o Domain/Enterprise Architect. También
puede ser una rotación temporal de liderazgo técnico. El alcance crece desde un sistema
hacia portafolios y organización; la profundidad práctica no debería desaparecer.

## ⚠️ Mitos frecuentes

- “Arquitectura ocurre antes de programar.” Evoluciona con evidencia.
- “El arquitecto decide solo.” Las decisiones necesitan contexto y ownership distribuido.
- “Microservicios son arquitectura moderna.” Son un trade-off con coste operacional.
- “El diagrama es la verdad.” Debe reconciliarse con código y runtime.

## 🚀 Siguientes pasos

1. Escribe atributos de calidad como escenarios observables.
2. Compara tres alternativas incluyendo no cambiar nada.
3. Ejecuta un spike sobre la incertidumbre más cara.
4. Registra la decisión y programa cuándo revisarla.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
