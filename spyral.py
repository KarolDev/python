import turtle
tortuga = turtle.Pen()
turtle.bgcolor("black")
#Spyralhjisdj[
lados = 3
colores = ["pink","violet red","turquoise","sienna","peru","papaya whip","purple","yellow","blue","gray"]
for distancia in range(1000):
    tortuga.pencolor(colores[distancia%lados])
    tortuga.forward(distancia*3/lados+distancia)
    tortuga.left(360/lados+1)
    tortuga.width(distancia*lados/200)