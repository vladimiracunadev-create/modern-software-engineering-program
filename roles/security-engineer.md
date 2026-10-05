# 🔐 Security Engineer

> Integra prevención, detección y recuperación en productos y plataformas sin convertir
> seguridad en una revisión tardía o una lista de herramientas.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** secure design, AppSec y supply
> chain · **Evidencia central:** riesgo trazado a controles y pruebas negativas

## 🧭 Qué es y por qué importa

Security engineering aplica ingeniería al riesgo deliberado: abuso, compromiso de
dependencias, escalada de privilegios, fuga de datos y manipulación del ciclo de entrega.
Trabaja con desarrollo y plataforma para que el camino seguro sea viable. No elimina
todo riesgo; lo hace visible, reduce exposición y prepara respuesta.

## 🗓️ Un día en el puesto

- modelar amenazas de una función o arquitectura;
- revisar autenticación, autorización y límites de confianza;
- investigar un hallazgo SAST/SCA sin aceptar falsos positivos a ciegas;
- diseñar una prueba negativa o control preventivo;
- mejorar secretos, IAM o procedencia de artefactos;
- coordinar remediación y evidencia con ingeniería y compliance.

## ✅ Responsabilidades y límites

- Responde por asesoría accionable y mecanismos verificables.
- Diferencia riesgo, vulnerabilidad, exploitabilidad e impacto.
- No usa el escáner como oráculo ni bloquea sin explicar amenaza.
- No promete cumplimiento solo porque existe un control.
- No reemplaza pentesting especializado ni respuesta forense cuando se requieren.

## 🧠 Qué necesitas saber

- redes, sistemas, web, APIs, datos e identidad;
- threat modeling, secure design y least privilege;
- OWASP, NIST SSDF, SAST, DAST, SCA y fuzzing;
- secretos, IAM, containers, cloud y seguridad de pipelines;
- SBOM, firma, provenance, SLSA y riesgos de paquetes;
- respuesta a incidentes, privacidad y evidencia de cumplimiento.

## 📚 Tu ruta en el programa

1. Partes 02–03, 05 y 09 para sistemas, red, programación y dependencias.
2. Partes 12–14 para requisitos, contratos, privacidad y experiencia.
3. Partes 20, 22 y 29 para APIs, dispositivos y cloud.
4. Parte 30 para pruebas y [Parte 32 — Seguridad, privacidad y cumplimiento](../classes/part-32-seguridad-privacidad-y-cumplimiento/README.md).
5. Partes 33–35 para supply chain, pipeline, observabilidad e incidentes.
6. Partes 38–39 para riesgos de código y agentes generativos.

## 🧪 Evidencia de portafolio

- threat model con activos, límites, amenazas y decisiones;
- autorización probada con casos de abuso;
- pipeline con SAST/SCA/secret scanning y triaje documentado;
- SBOM, firma y procedencia verificadas;
- cadena regulación → requisito → control → prueba → evidencia;
- tabletop o incidente simulado con contención y aprendizaje.

## 📈 Progresión

Software/Infrastructure Engineer → Security Engineer → Senior → Staff/Product
Security, AppSec, Cloud Security o Security Architecture. La progresión aumenta el
alcance de los sistemas protegidos y la capacidad de influir sin crear cuellos de botella.

## ⚠️ Mitos frecuentes

- “Más escáneres significa más seguridad.” Sin triaje generan ruido y bypass.
- “Cumplir equivale a ser seguro.” Compliance define evidencia mínima, no ausencia de riesgo.
- “Shift-left significa mover todo a desarrollo.” También hay runtime y respuesta.
- “La IA arregla vulnerabilidades automáticamente.” También introduce APIs falsas y código inseguro.

## 🚀 Siguientes pasos

1. Modela amenazas de un flujo real antes de elegir herramientas.
2. Implementa un control y una prueba que demuestre su límite.
3. Introduce una dependencia comprometida en un laboratorio controlado.
4. Practica comunicación de riesgo con una recomendación priorizada.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
