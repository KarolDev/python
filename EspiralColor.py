import turtle
tortuga = turtle.Pen()
turtle.bgcolor("black")
colores = ["hotpink","aquamarine","mediumorchid","steelblue", "pink","blue","yellow","violet"]
lados = int(turtle.numinput("Número de lados  ", "Cuantos lados quieres tener (1-8) ?",4,1,8))
for x in range(360):
    tortuga.pencolor(colores[x%lados])
    tortuga.forward(x*3/lados+x)
    tortuga.left(360/lados+1)
    tortuga.width(x*lados/200)









