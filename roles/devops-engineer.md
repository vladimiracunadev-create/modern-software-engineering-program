# 🚚 DevOps Engineer

> Construye automatización para que cambios pequeños lleguen a entornos reales de
> forma repetible, segura, observable y reversible.
>
> **Entrada habitual:** semi-senior · **Foco:** CI/CD, infraestructura y entrega ·
> **Evidencia central:** pipeline reproducible con promoción y rollback comprobados

## 🧭 Qué es y por qué importa

DevOps nació como una forma de trabajo que une desarrollo y operación; en muchas
empresas también nombra a quienes construyen pipelines, infraestructura y automatización.
El rol reduce variabilidad y tiempo de feedback sin convertir el equipo en una mesa
de tickets. Su producto es un flujo de entrega que otros pueden usar y comprender.

## 🗓️ Un día en el puesto

- corregir un pipeline fallido o reducir su tiempo de feedback;
- modelar infraestructura declarativa y revisar su plan;
- publicar, promover o retirar un artefacto verificable;
- mejorar secretos, identidad y permisos de un workflow;
- automatizar despliegue progresivo y rollback;
- investigar con desarrollo una falla que cruza aplicación e infraestructura.

## ✅ Responsabilidades y límites

- Responde por repetibilidad, trazabilidad y seguridad del camino de entrega.
- Diseña autoservicio y documentación, no dependencia personal.
- No es “la persona que hace deploys” para todos.
- No usa YAML como sustituto de diseño ni crea pipelines imposibles de depurar.
- No mide éxito solo por frecuencia; también importan fallos y recuperación.

## 🧠 Qué necesitas saber

- Linux/Windows, shells, redes, procesos, paquetes y contenedores;
- Git, artefactos, SemVer, configuración y secretos;
- CI/CD, IaC, GitOps, entornos y progressive delivery;
- IAM, supply chain, SBOM, firma y procedencia;
- observabilidad, capacidad, backups y recuperación;
- DORA, feedback loops y límites de las métricas.

## 📚 Tu ruta en el programa

1. Partes 02–03 y 08–09 para sistemas, redes, depuración y empaquetado.
2. Partes 16–18 para Git, documentación y automatización.
3. [Parte 29 — Cloud, plataforma e infraestructura](../classes/part-29-cloud-plataforma-e-infraestructura/README.md).
4. Partes 31 y 33 para resiliencia, build, release y supply chain.
5. [Parte 34 — CI/CD, IaC y platform engineering](../classes/part-34-ci-cd-iac-y-platform-engineering/README.md).
6. Parte 35 para observabilidad e incidentes; partes 38–39 para automatización con agentes.

## 🧪 Evidencia de portafolio

- pipeline desde commit hasta entorno con artefacto inmutable;
- IaC con plan, política, destrucción y recuperación;
- identidad efímera y permisos mínimos por job;
- SBOM, firma y procedencia verificadas al desplegar;
- canary o blue/green con criterio automático y rollback;
- medición de lead time, failure rate y recovery con interpretación honesta.

## 📈 Progresión

Systems/Software Engineer → DevOps Engineer → Senior → Platform, SRE, DevSecOps o
Staff Infrastructure. Crecer significa convertir conocimiento operativo en una
capacidad compartida y sostenible.

## ⚠️ Mitos frecuentes

- “DevOps es un equipo que recibe tickets.” Eso recrea el silo que intentaba resolver.
- “Automatizado significa confiable.” Un error automatizado escala más rápido.
- “Contenedor significa reproducible.” Imagen, dependencias y entorno también importan.
- “Más despliegues siempre es mejor.” Sin demanda, calidad y recuperación es gaming.

## 🚀 Siguientes pasos

1. Automatiza build y prueba de un artefacto pequeño.
2. Añade procedencia y promoción entre entornos sin reconstruir.
3. Implementa un despliegue fallido deliberado y recupera.
4. Documenta el golden path y observa a otra persona usarlo.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
