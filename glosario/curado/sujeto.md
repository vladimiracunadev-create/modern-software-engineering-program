# Sujeto

## Definición

**Sujeto** es la identidad, o el objeto, a quien se refiere una afirmación de seguridad. El programa lo usa con tres sentidos relacionados:

- **Identidad autenticada que realiza una solicitud** (`SE-245`): la parte de un token que dice *quién* actúa.
- **Proceso y contexto de identidad que solicita una acción** (`SE-027`): quien intenta usar un recurso en un sistema operativo.
- **Artefacto al que se refiere una atestación** (`SE-472`): el objeto sobre el que se afirma algo, identificado por su huella.

En `SE-484` se emplea para la afirmación de un token de identidad: repositorio, rama o entorno que pide una credencial.

## Por qué importa

Toda decisión de acceso se toma sobre un sujeto. Si el sujeto se define de forma laxa (con prefijo o comodín), un tercero que coincida con el patrón obtiene acceso. Si el rol del sujeto se toma de datos que controla el cliente, el control es ilusorio. La decisión que cambia es de dónde se deriva el sujeto y con qué exactitud se compara.

## Cómo funciona

**En tokens** (`SE-245`): un token firmado transporta un sujeto y unas afirmaciones; su verificación exige comprobar el algoritmo, la firma, el emisor, la audiencia y la vigencia. El sujeto y el rol se derivan del token verificado, no de lo que el cliente declara.

**En identidad de integración continua** (`SE-484`): el *job* pide a la plataforma un token de identidad (firmado, con repositorio, rama, entorno, emisor, audiencia y vigencia); la nube lo valida y comprueba una **regla de confianza** del tipo «acepto tokens cuyo sujeto sea exactamente este repositorio y esta rama». Si coincide, entrega una credencial temporal. Solo el sujeto exacto y la vida corta dejan fuera los casos ilegítimos y mantienen los legítimos.

**En atestaciones** (`SE-472`): el sujeto es el artefacto, identificado por su huella; así un SBOM o una declaración de procedencia queda vinculado al objeto exacto.

## Ejemplo

```text
sujeto aceptado:   repo:universidad/api-entregas:environment:produccion
sujeto rechazado:  repo:universidad/api-entregas-fork:ref:refs/heads/feature   (otro repositorio / rama sin proteger)
regla:             igualdad exacta, no prefijo ni comodín; token con vida máxima de 15 minutos
```

## Errores y confusiones comunes

- **Un repositorio ajeno obtiene credenciales.** Causa: sujeto con prefijo o comodín; corrección: sujeto exacto y pruebas con tokens manipulados (`SE-484`).
- **El rol llega en un encabezado del cliente.** Causa: contexto tomado de datos controlados por el cliente; corrección: derivar rol y sujeto del token verificado (`SE-245`).
- **Un SBOM válido describe otro artefacto.** Causa: sin vínculo por huella; corrección: sujeto identificado por la huella del artefacto (`SE-472`).

## Límites y cuándo no aplica

El sentido de la palabra cambia con el contexto: no es lo mismo el sujeto de una solicitud que el de una atestación. La regla de confianza de `SE-484` protege si el emisor del token es de fiar; si la plataforma de integración continua está comprometida, un sujeto exacto no basta. Y un sujeto bien verificado solo responde «quién»: «qué puede hacer» es autorización.
