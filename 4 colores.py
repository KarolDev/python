import turtle        
tortuga = turtle.Pen()
turtle.bgcolor("black")
colores = ["turquoise","tan","thistle","snow"]
for distancia in range(150):
    tortuga.pencolor(colores[distancia%4])
    tortuga.circle(distancia)
    tortuga.left(90)
