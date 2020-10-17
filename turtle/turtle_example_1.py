#https://docs.python.org/3/library/turtle.html#:~:text=The%20turtle%20module%20is%20an,)%20100%25%20compatible%20with%20it.

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()