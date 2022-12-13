import turtle
import math
import time

colors=["red", "purple", "blue", "green", "yellow", "orange"]

def paintSinCosTan():
    for x in range(360):
        t.pencolor("red")
        #t.up()
        t.setpos(x, math.sin(x/10)*100)
        #qt.dot(2)
    t.up()
    t.setpos(1,1)
    t.down()
    for x in range(360):
        t.pencolor("blue")
        #t.up()
        t.setpos(x, math.cos(x/10)*100)
    t.up()
    t.setpos(1,1)
    t.down()
    for x in range(360):
        t.pencolor("green")
        #t.up()
        t.setpos(x, math.tan(x/10)*100)


def paintKreisBogen(radius):
    #t.reset()
    t.setpos(0,0)
    t.pencolor("green")
    t.dot(5)
    t.setpos(0,-radius*100)
    t.down()
   
    bogenlaenge=3
    umfang= 2*radius*math.pi
    t.pencolor("red")
    grad = 360/umfang*bogenlaenge
    print(t.pos())
    print(turtle.heading())
    t.circle(radius*100,360)
    t.pencolor("blue")
    t.circle(radius*100,grad)
    t.up()
    t.circle(radius*100,360-grad)




t=turtle.Pen()
t.speed(5)
turtle.bgcolor("black")
paintKreisBogen(1)
paintKreisBogen(2)
paintKreisBogen(4)

time.sleep(10)
