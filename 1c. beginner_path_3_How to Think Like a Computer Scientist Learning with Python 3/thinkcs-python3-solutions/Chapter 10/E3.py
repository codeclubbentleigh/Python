import turtle  # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(0)
red = turtle.Turtle()
green = turtle.Turtle()
orange = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()


def initialization(obj, color, position):
    obj.hideturtle()
    obj.speed(0)
    obj.forward(40)
    obj.left(90)
    obj.forward(50)
    obj.shape("circle")
    obj.shapesize(3)
    obj.fillcolor(color)
    obj.forward(position)


initialization(red, "red", 140)
initialization(green, "green", 0)
initialization(orange, "orange", 70)

state_num = 0
wn.listen()  # Listen for events


# red and green light will last for 3 seconds, while orange light will last for 2 second.
def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        orange.showturtle()
        green.hideturtle()
        wn.ontimer(advance_state_machine, "2000")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        red.showturtle()
        orange.hideturtle()
        wn.ontimer(advance_state_machine, "3000")
        state_num = 2
    else:  # Transition from state 2 to state 0
        green.showturtle()
        red.hideturtle()
        wn.ontimer(advance_state_machine, "3000")
        state_num = 0


wn.ontimer(advance_state_machine, "3000")
green.showturtle()
wn.mainloop()
