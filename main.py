import os
import random
from turtle import *

FONT = ('Arial', 16, "normal")
TURTLE_SIZE = 20
TIMER = 5
score = 0
game_active = False


def get_previous_high_score():
    fpath = os.getcwd() + "/high_score_file.txt"
    if os.path.isfile(fpath) and os.path.getsize(fpath) > 0:
        with open(fpath, "r") as f:
            hs = int(f.read())
            return hs
    else:
        return 0


def check_high_score(sc):
    global high_score
    if sc > high_score:
        high_score = sc
        return True
    return False


def random_move_horizontal():
    h = random.choice(range(int((-1 * (my_screen.window_width() / 2) + TURTLE_SIZE * 2)),
                            int(((my_screen.window_width() / 2) - TURTLE_SIZE * 2))))
    return h


def random_move_vertical():
    w = random.choice(range(int((-1 * (my_screen.window_height() / 2) + TURTLE_SIZE * 4)),
                            int(((my_screen.window_height() / 2) - TURTLE_SIZE * 2))))
    return w


def turtle_mover(rand_turtle):
    rand_turtle.goto(random_move_horizontal(), random_move_vertical())


def game_starter(x, y):
    global score, game_active
    score = 0
    game_active = True
    starter_turtle.clear()
    starter_turtle.hideturtle()
    countdown(TIMER)


def increase_score(x, y):
    global score
    if game_active:
        turtle_mover(turtle)
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align='center', font=FONT)


def countdown(time):
    global game_active, score
    timer_turtle.clear()
    timer_turtle.write(f"Time: {time}", align='center', font=FONT)
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align='center', font=FONT)
    if time > 0:
        turtle_mover(turtle)
        turtle.onclick(increase_score)
        timer_turtle.write(f"Time: {time}", align='center', font=FONT)
        my_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_active = False
        score_turtle.clear()
        if check_high_score(score):
            with open("high_score_file.txt", mode="w") as myFile:
                myFile.write(f"{score}")
            score_turtle.write(f"New High Score: {score}!", align='center', font=FONT)
        else:
            score_turtle.write(f"Score: {score} --- High Score: {high_score}", align='center', font=FONT)
        timer_turtle.clear()
        timer_turtle.write("Game Over...", align='center', font=FONT)
        starter_turtle.write('Press to play again:', align='center', font=FONT)
        starter_turtle.showturtle()


high_score = get_previous_high_score()

my_screen = Screen()
my_screen.bgcolor('light blue')
my_screen.title("Catch The Turtle")

timer_turtle = Turtle(shape='turtle', visible=False)
timer_turtle.penup()
timer_turtle.goto(0, my_screen.window_height() / 2 - TURTLE_SIZE * 2)
timer_turtle.pendown()
timer_turtle.color('blue')

score_turtle = Turtle(visible=False)
score_turtle.penup()
score_turtle.goto(0, my_screen.window_height() / 2 - TURTLE_SIZE * 3)
score_turtle.pendown()
score_turtle.color('blue')
score_turtle.write(f"Score: {score}", align='center', font=FONT)

turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')
turtle.shapesize(2, 2, 1)
turtle.penup()
turtle.speed(10)

starter_turtle = Turtle(shape='arrow', visible=False)
starter_turtle.color("red")
starter_turtle.penup()
starter_turtle.goto(0, my_screen.window_height() / 2 - TURTLE_SIZE * 5)
starter_turtle.pendown()
starter_turtle.showturtle()
starter_turtle.write('Start The Game', align='center', font=FONT)
starter_turtle.onclick(game_starter)

my_screen.mainloop()
