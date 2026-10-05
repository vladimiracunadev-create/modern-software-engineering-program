# 📦 Build & Release Engineer

> Convierte código fuente revisado en artefactos reproducibles, verificables y
> distribuibles con una historia de procedencia y reversión.
>
> **Entrada habitual:** semi-senior · **Foco:** builds, artefactos y releases
> · **Evidencia central:** release reconstruible, firmado y reversible

## 🧭 Qué es y por qué importa

El software que no puede reconstruirse ni atribuirse es difícil de parchear y confiar.
Build & Release Engineering gobierna toolchains, dependencias, versionado, artefactos,
promoción y entrega para reducir variación y riesgo de supply chain.

## 🗓️ Un día en el puesto

- investigar una compilación no determinista;
- actualizar toolchain o dependencia fijada;
- revisar SBOM, provenance y firmas;
- coordinar freeze, promoción, notas y rollback;
- medir duración, flakiness y tasa de fallos del pipeline.

## ✅ Responsabilidades y límites

- Responde por reproducibilidad, integridad y trazabilidad del artefacto.
- Separa construir, promover y desplegar.
- No firma artefactos que no puede relacionar con fuente y proceso.
- No sacrifica recuperabilidad para aumentar frecuencia de releases.

## 🧠 Qué necesitas saber

Compiladores, gestores de paquetes, lockfiles, cachés, hermeticidad, versionado,
repositorios de artefactos, SBOM, signing, provenance, SLSA, CI/CD, secretos,
release strategies y respuesta a dependencias comprometidas.

## 📚 Tu ruta en el programa

1. Partes 01–09 para toolchains, paquetes y automatización.
2. Partes 16–18 para Git, releases y documentación.
3. Parte 29 y [Parte 33 — Build, release y supply chain](../classes/part-33-build-release-y-cadena-de-suministro/README.md).
4. Partes 30–35 para gates, seguridad, despliegue y observación.
5. Parte 36 para parches y EOL.

## 🧪 Evidencia de portafolio

- build repetido con comparación de artefactos;
- SBOM, firma y provenance verificables;
- pipeline con separación de permisos y promoción;
- simulación de dependencia comprometida y revocación.

## 📈 Progresión

Developer/DevOps → Build Engineer → Release Engineer → Staff Developer Productivity.

## ⚠️ Mitos frecuentes

- “CI verde significa release confiable.” Puede faltar procedencia o recuperación.
- “El lockfile resuelve supply chain.” Fija selección, no legitimidad ni seguridad.
- “Rollback es volver al binario.” Datos y contratos también evolucionan.

## 🚀 Siguientes pasos

1. Reconstruye el mismo commit en dos entornos.
2. Verifica firma, SBOM y origen antes de promover.
3. Revierte una entrega que incluya cambio compatible de datos.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
