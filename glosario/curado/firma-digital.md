# Firma digital

## Definición

Una **firma digital** es un valor calculado con una clave privada sobre unos datos, que cualquiera puede verificar con la clave pública correspondiente. `SE-473` (firmas, checksums y verificación) la define así; `SE-225` la presenta como prueba de que el publicador es quien dice ser y de que el contenido no cambió, y `SE-262` subraya que quien no tiene la clave privada no puede producirla. Prueba procedencia (de la clave) e integridad (de esos bytes).

## Por qué importa

Quien instala o actualiza software decide en qué confiar antes de ejecutarlo. `SE-473` existe para que sepas qué ataque detiene cada comprobación y cuál no: una huella (checksum) detecta corrupción pero no a un atacante que reemplaza archivo y huella; una firma sí, mientras la clave privada permanezca secreta.

## Cómo funciona

El publicador firma los datos con su clave privada; el verificador comprueba la firma con la clave pública. Dos propiedades de diseño que `SE-473` destaca:

- **No hay secreto compartido.** Publicador y verificador no comparten un secreto, y cualquiera puede comprobar (a diferencia de un código de autenticación con clave compartida).
- **Qué prueba y qué no.** Una verificación correcta prueba que quien posee la clave privada firmó *exactamente esos bytes*. No prueba quién es esa persona, que la clave sea de quien se cree, que el contenido sea benigno ni que sea reciente.

Ed25519, algoritmo moderno especificado en el RFC 8032, usa claves de 32 bytes y firmas de 64, con verificación rápida. Lo que une la clave pública con una identidad es otro mecanismo (certificados, una raíz de confianza); y lo que impide reinstalar una versión vieja firmada es un número de secuencia dentro de lo firmado.

## Ejemplo

La API de entregas de `SE-473` publica un manifiesto (`release.json`) con nombre, versión, número de secuencia y las huellas de los artefactos; la firma cubre el manifiesto. Quien instala verifica la firma y luego compara las huellas. Ilustración propia del paso: `verificar(clave_publica, manifiesto, firma)` devuelve verdadero o falso; si el atacante cambia un byte del manifiesto, falla.

## Errores y confusiones comunes

- **Confundir firma con huella:** la huella no prueba procedencia.
- **Creer que firmado significa seguro:** prueba quién firmó, no que el contenido sea benigno.
- **Ignorar la actualidad:** una versión vieja firmada sigue verificando; hace falta número de secuencia.
- **Guardar la clave privada en el repositorio o en el mismo equipo que compila sin protección.**

## Límites y cuándo no aplica

No resuelve la distribución de la clave pública: si el atacante cambia esa clave, todo verifica. No protege contra un publicador comprometido. Las pruebas de la clase usan datos sintéticos; no sustituyen una cadena de suministro con procedimientos de gestión de claves y revocación.
