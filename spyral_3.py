import turtle
lados = eval(input("Pon un número de lados del 2 al 10: "))
velocidad = eval(input("Del 1 al 10 que tan rápido quieres que dibuje,si me me quieres lo más rápido posible escoge 0: "))
tortuga = turtle.Pen()
turtle.bgcolor("black")
tortuga.speed(velocidad)
#Spyralhjisdj[
colores = ["pink","violet red","turquoise","sienna","peru","papaya whip","purple","yellow","blue","gray"]
for distancia in range(1000):
    tortuga.left(3)
    tortuga.pencolor(colores[distancia%lados])
    tortuga.forward(distancia*3/lados+distancia)
    tortuga.left(360/lados+1)
    tortuga.width(distancia*lados/200)
    