# Contribuir

1. Determina el repositorio propietario usando el manifiesto.
2. Define competencia y evidencia antes de crear material.
3. Lee y aplica `docs/PEDAGOGICAL-STANDARD.md`; una plantilla no demuestra calidad.
4. Evita duplicar contenido especializado.
5. Verifica fuentes temporales y fecha.
6. Ejecuta `python scripts/build_program_blueprint.py --check`.
7. Ejecuta `python scripts/build_phase2.py --check`.
8. Ejecuta `python scripts/build_phase3.py --check` si modificas las etapas A o C.
9. Ejecuta `python scripts/build_role_guides.py --check` si modificas rutas, clases
   asociadas o su presentación.
10. Ejecuta `python scripts/validate_class_contracts.py`, `python scripts/validate_phase3.py`, `python scripts/validate_encoding.py` y `python scripts/validate_site.py`.
11. Ejecuta `python scripts/validate_repository.py --strict` y las pruebas.
12. Revisa seguridad, accesibilidad, licencias y continuidad.

## Licencias y procedencia

Antes de enviar una contribución, clasifica cada archivo:

| Tipo | Licencia de contribución | Evidencia adicional |
| --- | --- | --- |
| código, script, workflow, configuración o contrato ejecutable | Apache-2.0 | dependencias, versiones y avisos cuando corresponda |
| clase, ruta, explicación, evaluación, rúbrica o diagrama pedagógico | CC BY-NC-SA 4.0 | fuentes que sostienen las afirmaciones |
| dato o catálogo | según `DATA_LICENSES.md` | procedencia, autorización, privacidad y método de generación |
| activo visual o binario | según `ASSET_LICENSES.md` | autor, fuente, licencia, transformaciones y atribución |
| material de terceros | licencia original compatible | enlace primario, permiso y texto de atribución |

Al contribuir declaras que tienes derecho a hacerlo y aceptas la licencia aplicable
a esa categoría. No copies una fuente por estar públicamente accesible: una cita o
un enlace no equivalen a permiso de redistribución. Si cambias una acción,
dependencia, herramienta, dato o activo, actualiza el inventario correspondiente y
ejecuta `python scripts/validate_licensing.py`.

Una clase solo se presenta como desarrollada después de revisar su explicación completa,
temario, ejemplos, glosario, práctica, reto, errores, FAQ y fuentes. La presencia
de secciones o un conteo de palabras no autoriza el cambio de madurez.

Una contribución transversal debe actualizar la matriz o un proyecto; un enlace suelto no constituye integración.
