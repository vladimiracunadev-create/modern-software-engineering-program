# Contribuir

1. Determina el repositorio propietario usando el manifiesto.
2. Define competencia y evidencia antes de crear material.
3. Lee y aplica `docs/PEDAGOGICAL-STANDARD.md`; una plantilla no demuestra calidad.
4. Evita duplicar contenido especializado.
5. Verifica fuentes temporales y fecha.
6. Ejecuta `python scripts/build_program_blueprint.py --check`.
7. Ejecuta `python scripts/build_phase2.py --check`.
8. Ejecuta `python scripts/build_phase3.py --check` si modificas las etapas A o C.
9. Ejecuta `python scripts/validate_class_contracts.py`, `python scripts/validate_phase3.py`, `python scripts/validate_encoding.py` y `python scripts/validate_site.py`.
10. Ejecuta `python scripts/validate_repository.py --strict` y las pruebas.
11. Revisa seguridad, accesibilidad, licencias y continuidad.

Una clase solo cambia a `GUIDED` después de revisar su explicación completa,
temario, ejemplos, glosario, práctica, reto, errores, FAQ y fuentes. La presencia
de secciones o un conteo de palabras no autoriza el cambio de madurez.

Una contribución transversal debe actualizar la matriz o un proyecto; un enlace suelto no constituye integración.
