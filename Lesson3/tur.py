from turtle import *

def draw_shell(t, size):
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def draw_head(t, size):
    t.begin_fill()
    t.right(90)
    t.forward(size * 0.6)
    t.right(90)
    t.circle(size * 0.4)
    t.right(90)
    t.forward(size * 0.6)
    t.end_fill()

def draw_legs(t, size):
    for _ in range(4):
        t.penup()
        t.goto(-size * 0.5, size * (0.5 if _ < 2 else -0.5))
        t.pendown()
        t.begin_fill()
        t.circle(size * 0.15)
        t.end_fill()

def draw_tail(t, size):
    t.penup()
    t.goto(size * 0.5, -size * 0.5)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.1)
    t.end_fill()

def draw_turtle(t, size):
    t.color('green')
    draw_shell(t, size)
    t.color('brown')
    draw_head(t, size)
    draw_legs(t, size)
    draw_tail(t, size)

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

size = 100
draw_turtle(my_turtle, size)

my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()