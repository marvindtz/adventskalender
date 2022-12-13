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
    
    t.up() # nicht malen
    t.setpos(0,0)
    t.pencolor("green")
    t.dot(5) # mittelpunkt
    t.setpos(0,-radius*100)
    t.down() #wieder malen
   
    #berechnen vom umfang und alpha für eine Bogenlänge von 3
    bogenlaenge=3
    umfang= 2*radius*math.pi
    grad = 360/umfang*bogenlaenge

    t.pencolor("red")
    t.circle(radius*100,360) # kompletter kreis 
    t.pencolor("blue")
    t.circle(radius*100,grad) # teil kreis
    
    t.up() # nicht malen
    t.circle(radius*100,360-grad) # kreis fertig malen mait turtle wieder beim nächsten kreis von vorne beginnt


t=turtle.Pen()
t.speed(5)
turtle.bgcolor("black")

paintKreisBogen(1)

paintKreisBogen(2)

paintKreisBogen(4)

input("Press key to exit")
