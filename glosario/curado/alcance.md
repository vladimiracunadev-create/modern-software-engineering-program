# Alcance

## Definición

**Alcance** es la extensión dentro de la cual algo es válido o produce efecto. El programa usa la palabra con tres sentidos que conviene no mezclar:

- **Dominio de validez de un identificador o configuración** (`SE-032`, `SE-038`, `SE-064`): el conjunto de usuarios, proyectos o sistema afectado, o la región donde un nombre se resuelve.
- **Alcance de red** (`SE-038`): hasta dónde es válida una dirección. Una dirección MAC identifica una interfaz en su enlace, no una identidad global ni una ruta por Internet.
- **Alcance de un efecto** (`SE-582`): hasta dónde llegan las consecuencias de una acción.

## Por qué importa

Casi todo error de «funcionaba aquí» es un error de alcance: un identificador se usó fuera de donde significa algo, una instalación global afectó a otro proyecto, una acción «local» tuvo consecuencias externas. Preguntar «¿dónde es válido esto?» antes de actuar cambia decisiones concretas: dónde instalar una dependencia, cómo acotar un dominio de difusión, o qué acciones puede ejecutar un agente sin pedir confirmación.

## Cómo funciona

El mecanismo común es que un valor solo tiene significado respecto a un contexto que lo resuelve.

- **Instalación** (`SE-032`): un paquete en alcance global lo resuelven todos los proyectos; una actualización puede romper otro. Aislar por proyecto y conservar manifiesto y bloqueo acota el alcance.
- **Nombres** (`SE-064`): una variable se resuelve en la región donde se define y en las que la contienen; fuera, no existe.
- **Redes** (`SE-038`): los conmutadores aprenden asociaciones dirección-puerto con expiración; un enrutador separa dominios de difusión y un conmutador no (salvo VLAN). Acotarlos limita ruido y ciertos ataques.
- **Efectos** (`SE-582`): se clasifica una acción por su alcance (interno o externo al proyecto) y su reversibilidad.

## Ejemplo

`SE-582` ofrece una escala: borrar un archivo versionado es de alcance interno y reversible; borrar uno sin versionar, interno e irreversible; escribir en la carpeta personal sin copia, externo al proyecto e irreversible; enviar un mensaje o eliminar un recurso remoto, externo e irreversible. Cuanto mayor el alcance y menor la reversibilidad, más control exige la acción.

## Errores y confusiones comunes

- **Una actualización rompe otro proyecto.** Causa: alcance global sin control de resolución; corrección: aislar por proyecto y conservar manifiesto y bloqueo (`SE-032`).
- **Tomar la dirección MAC como identidad global.** Solo vale en su enlace (`SE-038`).
- **Tratar sentidos distintos como uno solo.** Alcance de nombres, de red y de efectos no se intercambian.

## Límites y cuándo no aplica

La palabra no es un criterio único: en cada clase el sentido cambia, y hay que fijar de cuál se habla. Acotar el alcance reduce el daño posible pero no lo elimina; un alcance «interno» mal evaluado sigue siendo un riesgo. La escala de `SE-582` es una clasificación didáctica del programa, no una norma.
