# Módulo 10 — CI/CD y cadena de suministro

## Objetivos

- automatizar cambios reproducibles;
- proteger la cadena desde código hasta despliegue;
- diseñar promoción, aprobación y rollback;
- reducir tiempo sin ocultar fallos.

## Contenidos

Build hermético; bloqueos; artefactos; CI; pruebas; análisis; SBOM; firma y procedencia; secretos; entornos; migraciones; estrategias blue/green, canary y feature flags; rollback y roll-forward.

## Laboratorio

Diseña un pipeline que valide documentación, código, contrato, seguridad y artefacto. Simula una prueba fallida, una dependencia vulnerable y una migración incompatible. Define qué bloquea y quién aprueba.

## Restricción

JavaScript/TypeScript usa pnpm y lockfile. Ninguna automatización debe incluir credenciales en logs.

## Criterio

El mismo commit produce un artefacto identificable y existe un camino probado de recuperación.
