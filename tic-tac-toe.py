"""Tic Tac Toe

Exercises

Modificar el tamaño y el color de los símbolos "X" y "O" y centrarlos.

"""

from turtle import goto, up, down, circle, onscreenclick, pencolor
from turtle import done, hideturtle, setup, tracer, update, colormode, color

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-100, 300, -100, -300)
    line(100, 300, 100, -300)
    line(-300, -100, 300, -100)
    line(-300, 100, 300, 100)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    line(x, y, x + 200, y + 200)
    line(x, y + 200, x + 200, y)


def drawo(x, y):
    """Draw O player."""
    color('red')
    up()
    goto(x + 100, y + 5)
    down()
    circle(95)


def floor(value):
    """Round value down to grid with square size 200."""
    return ((value + 300) // 200) * 200 - 300


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
colormode()
pencolor()
onscreenclick(tap)
done()
# This is a new line that ends the file.
