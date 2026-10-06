# Evidencia de validación de la Parte 02

Este registro se actualiza con resultados realmente ejecutados. Los workflows remotos
son la evidencia de Linux y macOS; una ejecución local no los sustituye.

## Entorno local

- fecha: 2026-10-06;
- runtime: CPython 3.12.9;
- sistema: Windows 11;
- dependencias externas: ninguna.

## Resultados

| Comprobación | Criterio | Resultado |
| --- | --- | --- |
| `python -m unittest discover -s labs/part-02-cross-platform-diagnostic-kit/tests -v` | diez pruebas sin fallos | PASS, 10/10 en CPython 3.12.9 |
| adaptadores PowerShell y Bash `--help` | ayuda y código 0 | PASS, ambos adaptadores |
| ciclo prepare → inspect → repair → clean | códigos y estados según contrato | PASS en PowerShell; prepare → inspect → clean también pasó en Git Bash |
| matriz remota Linux/Windows/macOS | jobs de portabilidad verdes | pendiente hasta publicar el commit |

## Límites

No se ha probado hardware, ACL corporativa, elevación, instalación de paquetes,
servicios reales, WSL ni aislamiento hostil. El laboratorio verifica el núcleo portable,
los adaptadores y las negativas de seguridad dentro de un workspace desechable.
