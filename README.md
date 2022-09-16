# Integrantes

- Carlos Salguero ~ A00833341 (PacMan).
- Maria del Pilar Davila Verduzco ~ A01708943 (TIC TAC TOE).
- Miguel Angel Tena Garcia ~ A01709653 (Memory).

# PacMan

Clasico juego de pacman tomado de freegames.com

## Cambios

Los cambios realizados fueron los siguientes:

- Implementación del estilo PEP8. El estilo puede ser comprobado con el siguiente comando

    ```
    python3 -m flake8 pacman.py
    ```

- Cambiar el tablero: cambios en los espacios disponibles para mover al personaje de pacman. El cambio se realizó al modificar los 0s y 1s del mapa. Los datos con valor 1 son los que permiten mover a los fantasmas y personajes a través del mapa y los que tienen valor 0 son los muros o parte del programa donde no puedes mover a pacman.

- Hacer que los fantasmas vayan más rápido: cambios en la velocidad de los fantasmas, de velocidad 10 a 15

# Como correr el juego

Para correr el proyecto es necesario tener instalado Python 3 y las librerias de freegames, turtle y tkinter. Al tener instalados estas librerias, en la terminal escribe la siguiente linea

```
python3 pacman.py
```
