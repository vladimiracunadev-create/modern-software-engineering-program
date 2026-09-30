# Contrato de integración

## Regla de propiedad

Cada conocimiento tiene un propietario principal definido en `manifest/repositories.json`. La suite puede resumirlo para conectar el ciclo de vida, pero no mantiene una segunda implementación completa.

## Contratos de entrada y salida

### Programación

Entrada: problema canónico, invariantes y pruebas. Salida: implementaciones equivalentes y diferencias semánticas.

### Datos

Entrada: dominio, patrones de acceso, garantías y escala. Salida: modelos, consultas, operación, recuperación y ADR.

### Frameworks

Entrada: contrato externo, UI, atributos y entorno. Salida: adaptadores, pruebas equivalentes, operación y comparación.

### Suite

Entrada: necesidad de producto. Salida: fragmento vertical operable, trazable y defendible.

## Definición transversal de terminado

- requisito con criterio verificable;
- decisión registrada;
- código o artefacto ejecutable;
- pruebas proporcionales al riesgo;
- datos sintéticos y migrables;
- seguridad y accesibilidad revisadas;
- telemetría y diagnóstico;
- despliegue y rollback documentados;
- recuperación probada cuando existe estado;
- fuentes y versiones trazables;
- portafolio actualizado.

## Cambio de dominio canónico

1. Proponer RFC en la suite.
2. Identificar consumidores.
3. Versionar contrato o mantener compatibilidad.
4. Actualizar datos y pruebas en el propietario.
5. Migrar adaptadores.
6. Actualizar blueprint, matrices y portal.
7. Registrar ruptura y procedimiento de adopción.

## Integración incompleta

Se considera incompleta cuando solo se agrega un enlace, catálogo o logo sin competencia, práctica, prueba y resultado observable.
