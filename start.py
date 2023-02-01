
import turtle
t=turtle.Turtle()
Window=turtle.setup(width=700,height=700)
screen=turtle.Screen()
screen.setworldcoordinates(-600,-600,screen.window_width()-1,screen.window_height()-1)
t.speed(20)
colorlist=['red','purple','green','orange','blue']
t.penup()
t.goto(-200,50)
t.pendown()

def draw(turtle,size):
    if size<=20:
        return
    else:
        for i in range(5):
            t.forward(size)
            t.pensize(i/1+2)
            t.color(colorlist[i%6])
            draw(turtle,size/3)
            t.left(216)
draw(t,360)
turtle.done()