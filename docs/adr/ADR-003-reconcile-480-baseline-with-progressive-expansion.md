# ADR-003 — Reconciliar la línea base de 480 clases con la expansión progresiva

- Estado: aceptada
- Fecha: 2026-10-04
- Alcance: arquitectura curricular, preservación y control de crecimiento

## Contexto

El programa ya tiene una arquitectura pública de 40 partes y 480 identificadores
consecutivos. Doce clases tienen contenido desarrollado; las demás conservan borradores
o estructura curricular. Un mandato posterior amplía la cobertura esperada y
propone aproximarse a 500 clases, pero también prohíbe reconstruir, renumerar, inflar
conteos o confundir archivos generados con aprendizaje desarrollado.

Reemplazar las 480 clases destruiría trazabilidad, enlaces, navegación y trabajo
pedagógico válido. Añadir veinte títulos de inmediato produciría exactamente el
relleno que el mandato intenta evitar.

## Decisión

1. Los IDs `SE-001`–`SE-480`, las 40 partes y las ocho etapas siguen siendo la línea
   base canónica.
2. La progresión profesional de doce momentos se aplica como una lente acumulativa,
   no como una renumeración:

   | Progresión profesional | Etapas actuales que la desarrollan |
   | --- | --- |
   | Fundamentos y comprensión | A–B |
   | Práctica y construcción | B–D |
   | Integración y producción | C–F |
   | Operación y sistemas complejos | E–G |
   | Arquitectura y liderazgo | E–G |
   | Evolución y retiro | G, con trazas desde A |

3. Primero se profundiza y valida lo ya anunciado. Un tema faltante se integra en
   una clase existente cuando comparte problema, prerrequisitos y evidencia sin
   sobrecargarla.
4. Una clase nueva después de `SE-480` requiere simultáneamente:
   - una competencia observable no cubierta;
   - un problema profesional y un artefacto verificable propios;
   - fuentes primarias u oficiales localizadas;
   - ubicación, prerrequisitos y continuidad explícitos;
   - análisis de duplicación y propiedad entre repositorios;
   - actualización atómica de manifiesto, navegación, fuentes, portal y validadores.
5. “Aproximadamente 500” es una dirección de cobertura, no una cuota. El programa
   puede permanecer en 480 mientras agregar clases implique relleno, y puede superar
   500 si una auditoría futura demuestra competencias independientes.
6. Cada parte se publica en un commit propio después de revisión estructural y
   cualitativa. Un cambio de arquitectura o conteo usa además un ADR separado.

## Brechas candidatas, no clases aprobadas

La auditoría inicial detecta temas que deben intentarse primero como profundización:
métodos formales aplicados (incluidos TLA+ y Alloy como casos), API en tiempo real y
deprecación, estimación probabilística, InnerSource y OSPO, DevEx/SPACE, ingeniería de
compliance, green software medible, análisis de peligros y rutas profesionales. Solo
se convertirán en nuevas clases si el desarrollo de las partes existentes demuestra
que no caben sin perder coherencia.

## Alternativas descartadas

- **Renumerar a 500:** rompe enlaces y oculta la historia.
- **Añadir veinte scaffolds:** mejora una métrica sin mejorar aprendizaje.
- **Mantener 480 como límite inmutable:** impide responder a brechas demostradas.
- **Duplicar repositorios especializados:** diluye propiedad y mantenimiento.

## Consecuencias

- Los conteos actuales siguen siendo 40 partes y 480 clases.
- El objetivo público debe distinguir arquitectura, borradores y contenido desarrollado.
- La expansión futura será aditiva y trazable.
- La matriz de brechas pasa a ser entrada obligatoria de cada incremento curricular.

## Criterios de aceptación

- no se elimina ni renumera contenido existente;
- la definición del programa y su expansión queda en el roadmap;
- existe una matriz `Área | Estado | Archivos existentes | Profundidad | Brechas | Acción`;
- validadores y enlaces impiden que estos documentos queden huérfanos;
- ninguna clase se presenta como desarrollada solo por efecto de esta decisión.
