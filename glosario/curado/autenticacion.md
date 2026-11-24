# Autenticación

## Definición

La **autenticación** es el proceso de establecer quién hace una solicitud: comprobar que quien llama controla la identidad que afirma. El programa la define así en `SE-245` («establecimiento de la identidad de quien hace una solicitud»), la precisa en `SE-458` como la prueba de que quien llama controla esa identidad mediante algo que sabe, tiene o es, y en `SE-027` como el proceso de establecer una identidad en un sistema operativo. Es distinta de la autorización: autenticar responde «quién eres», no «qué puedes hacer».

## Por qué importa

Toda decisión posterior de seguridad (permisos, auditoría, límites de uso) se apoya en la identidad que la autenticación establece. Si esa identidad es falsa o se acepta sin comprobar, el resto del control se aplica a la persona equivocada. Según `SE-245`, sin una verificación completa un token falsificado o ajeno se acepta como si fuera válido. Cambia una decisión profesional concreta: qué comprobaciones debe hacer el servidor sobre cada credencial y cuáles no puede delegar al cliente.

## Cómo funciona

Un patrón habitual es el token firmado: transporta un sujeto y unas afirmaciones, y el servidor lo verifica en varias comprobaciones (`SE-245`):

- que el algoritmo sea el que el servidor espera, no el que declara la cabecera del propio token;
- que la firma coincida con la clave del emisor;
- que el emisor y la audiencia sean los de esta API;
- que la hora actual esté entre `nbf` (no antes de) y `exp` (expiración).

La causa de cada fallo es una comprobación omitida: `alg: none` evita la firma, un token expirado se acepta para siempre, uno emitido para otra audiencia funciona en esta API. En `SE-458` la autenticación se mira como política con mediciones: los factores (saber, tener, ser), la sesión que sigue a la prueba y qué defensa pasa a ser decisiva cuando cambia un dato como la reutilización de contraseñas.

## Ejemplo

Ilustración mínima, no código de una clase:

```python
claims = decode(token, key, algorithms=["RS256"], audience="api-entregas",
                issuer="https://idp.ejemplo")
```

Fijar `algorithms`, `audience` y `issuer` en la llamada cierra los tres ataques anteriores. En la plataforma de entregas de tareas que `SE-458` usa como caso conductor, la política de autenticación y sesión es un artefacto que se mide, no una opinión.

## Errores y confusiones comunes

- **Un token vencido sigue funcionando.** Causa: el verificador no comprueba `exp`; corrección: comprobar vigencia con un margen de reloj acotado (`SE-245`).
- **Un token de otra API funciona aquí.** Causa: no se comprueba la audiencia; corrección: exigir audiencia y emisor (`SE-245`).
- **Confundir autenticación con autorización.** Haber demostrado quién eres no dice qué puedes hacer; `SE-459` trata esa segunda decisión por separado.

## Límites y cuándo no aplica

Autenticar bien no protege por sí solo: `SE-027` muestra casos donde el sistema funciona como debía (la identidad existe, no tiene el permiso, y la elevación exige una autenticación que ese contexto no ofrece). Una autenticación correcta tampoco impide el abuso por una persona legítima. Y las cifras de `SE-458` son de un caso de estudio: otro sistema pide otras mediciones.
