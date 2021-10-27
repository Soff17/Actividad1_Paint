from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x,start.y) # marca el inicio
    down()
    begin_fill()
    for i in range(2):
        fd(2*end.x-start.x) # base del rectángulo
        rt(90) # gira 90 grados
        fd(end.x-start.x) # altura del rectángulo
        rt(90) # gira 90 grados
    end_fill() # rellena con color
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x,start.y) # marca el inicio
    down()
    begin_fill()
    for i in range(2):
        fd(end.x-start.x) # lado del triángulo
        lt(120) # gira 120 grados
    fd(end.x-start.x) # lado faltante
    end_fill() # rellena con color
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') # Se agregó un nuevo color (ROSA)
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
