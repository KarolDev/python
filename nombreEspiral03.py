import turtle
tortuga = turtle.Pen()
turtle.bgcolor("black")
colores = ["hotpink","aquamarine","mediumorchid","steelblue"]
nombre = turtle.textinput("Pon tu nombre", "Cual es tu nombre?")
for x in range(100):
    tortuga.pencolor(colores[x%4])
    tortuga.penup()
    tortuga.forward(x*4)
    tortuga.pendown()
    tortuga.write(nombre,font=("arial",int((x+4)/4),"bold"))
    tortuga.left(92)









