"""
Equipo 2:
Francisco Vázquez, A00827546
Nicolás Herrera, A01114972
Ana Paula López, A01378255
"""

from turtle import *
from random import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
foodNewPos = vector(0, -10)

"""
   Comentario por Francisco Vázquez 
"""

def foodColor():
    #Ramdomize food color on startup
    number = randrange(1,5)
    if(number == 1):
        fColor = 'yellow'
    if(number == 2):
        fColor = 'blue'
    if(number == 3):
        fColor = 'magenta'
    if(number == 4):
        fColor = 'cyan'
    if(number == 5):
        fColor = 'pink'
    return fColor

fColor = foodColor()

def snakeColor():
    #Ramdomize snake color on startup
    number = randrange(1,5)
    if(number == 1):
        sColor = 'gray'
    if(number == 2):
        sColor = 'black'
    if(number == 3):
        sColor = 'green'
    if(number == 4):
        sColor = 'violet'
    if(number == 5):
        sColor = 'brown'
    return sColor

sColor = snakeColor()

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def changeFood():
    direction = [10, -10]
    foodNewPos.x = choice(direction)
    foodNewPos.y = choice(direction)
    return foodNewPos

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insideFood(food):
    "Return True if food inside boundaries."
    return -150 < food.x < 150 and -150 < food.y < 150



def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    food.move(changeFood())


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, sColor)

    square(food.x, food.y, 9, fColor)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()