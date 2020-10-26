#I learned python using this awesome book when I was in 11th grade. I completed most of the exercises during that time. Pull requests are welcome if you find any mistakes.

#Note that some of the exercises require the use of the unit tester. You need to place a copy of unit_tester.py in your python's Lib directory for it to be loaded.

import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()


def DrawASquare(sidelength, CentXcor, CentYcor):
    Tom.penup()
    Tom.goto(CentXcor, CentYcor)
    Tom.goto(Tom.xcor() - sidelength / 2, Tom.ycor())
    Tom.pendown()
    Tom.goto(Tom.xcor(), Tom.ycor() + sidelength / 2)
    Tom.goto(Tom.xcor() + sidelength, Tom.ycor())
    Tom.goto(Tom.xcor(), Tom.ycor() - sidelength)
    Tom.goto(Tom.xcor() - sidelength, Tom.ycor())
    Tom.goto(Tom.xcor(), Tom.ycor() + sidelength / 2)
    Tom.penup()
    Tom.goto(CentXcor, CentYcor)


for i in range(0, 5):
    DrawASquare(20, 40 * i, 0)
Window.mainloop()
