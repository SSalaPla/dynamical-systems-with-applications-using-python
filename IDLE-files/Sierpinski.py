from turtle import *
def Sierpinski(length, level):  # Function.
    speed(0)                    # Fastest speed.
    if level==0:
        return
    begin_fill()                # Fill shape.
    color("red")

    for i in range(3):
        Sierpinski(length/2,level-1)
        fd(length)
        lt(120)
    end_fill()


    


