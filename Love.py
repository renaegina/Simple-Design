import turtle

vr = turtle.Turtle()

turtle.Screen().bgcolor('black')
turtle.pensize(4)
vr.speed(5)

def drawcurve():
    for i in range(200):
        vr.right(1)
        vr.forward(1)

def text():
    vr.up()
    vr.setpos(-68, 88)
    vr.down()
    vr.color('white')
    vr.write("I LOVE YOU", font=(
        "Verdana", 18, "Bold"
    ))

vr.color('Red')
vr.begin_fill()
vr.left(140)
vr.forward(111.650)
drawcurve()
vr.left(120)
drawcurve()
vr.forward(111.65)
vr.end_fill()
vr.penup()
vr.goto(77, -40)
vr.pendown()
vr.hideturtle()
text()
turtle.done
