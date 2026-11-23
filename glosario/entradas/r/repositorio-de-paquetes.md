# Repositorio de paquetes

[↑ Glosario](../../README.md) · [← Reposición](./reposicion.md) · [Repository →](./repository.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Servicio e índice desde el que un gestor obtiene metadatos y artefactos.

Definición de trabajo de [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md).

## Por qué importa

La clase donde se define, [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), existe con este propósito: la clase existe para distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.

## Cómo funciona

[SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md):

Una actualización global rompe dos proyectos. El equipo migra la herramienta a entornos por proyecto, fija resoluciones y prueba desinstalación. Documenta que quedan cachés y datos, en vez de afirmar una reversión perfecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)) son:

- **Se instala un paquete homónimo** — causa: se confió solo en el nombre. Corrección: verificar ecosistema, publicador, URL y firma/metadatos.
- **Una actualización rompe otro proyecto** — causa: se usó alcance global sin control de resolución. Corrección: aislar por proyecto y conservar manifiesto/bloqueo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)) son: No realizamos auditoría completa de cadena de suministro ni declaramos seguro un paquete por estar firmado. Incluso una instalación correcta puede fallar; la siguiente clase desarrolla logs y observabilidad para reconstruir qué ocurrió.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Índice](../i/indice.md), [Metadatos](../m/metadatos.md), [Servicio](../s/servicio.md), [Alcance](../a/alcance.md), [Dependencia](../d/dependencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — WinGet](https://learn.microsoft.com/windows/package-manager/winget/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Debian Administrator's Handbook — APT](https://www.debian.org/doc/manuals/debian-handbook/apt.en.html) — delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.
- [Homebrew Documentation](https://docs.brew.sh/) — delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.
- [Python Packaging User Guide](https://packaging.python.org/en/latest/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Reposición](./reposicion.md) · [Repository →](./repository.md)
