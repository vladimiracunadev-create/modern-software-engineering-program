# Proceso

## Definición

Un **proceso** es una instancia en ejecución de un programa, con espacio de direcciones propio, identificador, credenciales, descriptores o manejadores, entorno y estado planificable (`SE-019`, `SE-028`). `SE-253` lo precisa para aplicaciones móviles y de escritorio: la unidad de ejecución que el sistema operativo crea y puede terminar; contiene la memoria de la aplicación y no equivale a una ventana. Un *programa* es la descripción en un archivo; el proceso es su ejecución.

## Por qué importa

Es la unidad de aislamiento y de administración del sistema operativo: se lanza, se mide, se limita, se señala y se termina. Entenderlo evita errores concretos, como creer que cerrar una ventana cierra la aplicación o que guardar estado solo en memoria sobrevive a que el sistema termine el proceso. También es la base de contenedores, servicios y concurrencia.

## Cómo funciona

Un archivo de programa puede originar múltiples procesos. Cada uno posee espacio de direcciones virtual, identificador, recursos y estado administrado por el sistema (`SE-019`). El aislamiento limita el acceso accidental a la memoria de otro, pero no es una frontera de seguridad absoluta sin permisos y controles. Un proceso puede contener varios hilos que comparten su memoria. Termina con un código de salida que comunica el resultado al proceso padre (`SE-028`).

En plataformas móviles (`SE-253`), el sistema puede terminar procesos en segundo plano para recuperar memoria sin aviso. Por eso lo que importa debe guardarse en disco al pasar a segundo plano y restaurarse en el arranque.

## Ejemplo

```python
import subprocess, sys
r = subprocess.run([sys.executable, "-c", "print('hola')"], capture_output=True, text=True)
print(r.returncode, r.stdout)   # proceso hijo con su propia memoria y su propio código de salida
```

En `SE-253`, el texto de un borrador desaparece al volver a la aplicación porque el estado vivía solo en memoria y el sistema terminó el proceso.

## Errores y confusiones comunes

- **Programa igual a proceso.** Causa: se confunde archivo con ejecución; corrección: distinguir descripción e instancia (`SE-019`).
- **El texto del borrador desaparece al volver a la aplicación.** Causa: el estado vivía solo en memoria; corrección: guardar en disco al pasar a segundo plano y restaurar al arrancar (`SE-253`).
- **Medir CPU como si fuera espera.** El tiempo de CPU aproxima el trabajo ejecutado por el proceso, no la espera externa (`SE-019`).

## Límites y cuándo no aplica

El aislamiento entre procesos no equivale a seguridad: un proceso con los mismos permisos puede afectar a otro. Los procesos son más costosos que los hilos y su comunicación requiere mecanismos explícitos. Y en entornos con contenedores o máquinas virtuales, lo que «parece» un proceso aislado depende de la configuración del anfitrión.
