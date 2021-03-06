"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges? (changed the "inside" boundaries slightly to allow this)
3. How would you move the food?              (changing the values so the food apears more far than usual (this change was made by Nelson Osdani))
4. Change the snake to respond to arrow keys (this was already controled by the arrows, so we made it with the w,a,s,d keys).

"""
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(20, 0)]
aim = vector(0, -20)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Changed boundaries to allow snake to touch edges --> used <= instead of < and moved certain boundaries 
def inside(head):
    "Return True if head inside boundaries."
    return -210 <= head.x <= 190 and -200 <= head.y <= 200

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-10, 10) * 20
        food.y = randrange(-10, 10) * 20
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()
