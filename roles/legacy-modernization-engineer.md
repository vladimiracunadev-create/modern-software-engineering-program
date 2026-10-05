# 🏚️ Legacy Modernization Engineer

> Comprende y cambia sistemas críticos existentes sin perder continuidad, datos ni
> conocimiento; moderniza por evidencia, no por desprecio a lo antiguo.
>
> **Entrada habitual:** senior · **Foco:** brownfield, compatibilidad y migraciones ·
> **Evidencia central:** cambio incremental reversible sobre un sistema ajeno

## 🧭 Qué es y por qué importa

Legacy no significa simplemente tecnología vieja. Es software valioso cuyo cambio es
arriesgado por acoplamiento, conocimiento perdido, dependencias obsoletas o falta de
pruebas. Modernizar requiere arqueología, caracterización y estrategia. Reescribir es
una opción extrema, no el punto de partida.

## 🗓️ Un día en el puesto

- entrevistar usuarios y operadores para recuperar conocimiento;
- mapear dependencias, datos y flujos sin documentación confiable;
- capturar comportamiento con pruebas de caracterización;
- aislar un límite mediante adapter o anti-corruption layer;
- ejecutar migración progresiva y reconciliar resultados;
- planificar deprecación, archivo, retención y retiro seguro.

## ✅ Responsabilidades y límites

- Preserva comportamiento valioso antes de cambiarlo.
- Declara incertidumbre y crea checkpoints reversibles.
- No reescribe para mejorar estética ni adoptar una moda.
- No migra datos sin conciliación, backup y rollback.
- No retira un sistema sin ownership, retención y dependencias verificadas.

## 🧠 Qué necesitas saber

- lectura de código, depuración e ingeniería inversa;
- characterization tests, dependency mapping y análisis de datos;
- strangler fig, branch by abstraction y anti-corruption layer;
- rehost, replatform, refactor, rearchitect y rewrite;
- migraciones de API, esquema y datos con compatibilidad;
- EOL, decommissioning, archivo, retención y borrado seguro.

## 📚 Tu ruta en el programa

1. Parte 08 para investigación y debugging; partes 12–13 para reconstruir contratos.
2. Partes 16–17 para historia, colaboración y documentación.
3. Partes 24–28 para refactorización, arquitectura, datos e integración.
4. Partes 30–35 para caracterización, resiliencia, seguridad, entrega y observabilidad.
5. [Parte 36 — Mantenimiento y modernización legacy](../classes/part-36-mantenimiento-y-modernizacion-legacy/README.md).
6. Partes 37–39 para cambio organizacional e IA controlada sobre brownfield.

## 🧪 Evidencia de portafolio

- mapa de contexto, dependencias y conocimiento faltante;
- suite de caracterización que captura comportamientos relevantes;
- ADR comparando seis estrategias de modernización;
- migración dual-read/dual-write o equivalente con conciliación;
- rollout progresivo con criterios de abortar;
- plan de retiro con archivo, retención y borrado verificable.

## 📈 Progresión

Senior Engineer → Modernization Lead → Staff/Principal o Architect. También existe como
especialidad temporal en consultoría. El valor está en reducir riesgo y recuperar
capacidad de cambio, no en la cantidad de código reemplazado.

## ⚠️ Mitos frecuentes

- “Legacy es código malo.” Puede contener décadas de reglas no documentadas.
- “Una rewrite será más rápida.” Reinicia aprendizaje y suele subestimar paridad.
- “Mover a cloud moderniza.” Rehost cambia ubicación, no diseño ni operación.
- “Cuando el nuevo sistema arranca, el viejo se apaga.” Dependencias y datos pueden sobrevivir años.

## 🚀 Siguientes pasos

1. Toma un sistema pequeño ajeno y reconstruye su mapa de comportamiento.
2. Añade caracterización antes de refactorizar.
3. Extrae una capacidad detrás de un contrato compatible.
4. Ensaya reversión y documenta qué incertidumbre permanece.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
