import turtle
tortuga= turtle.Pen()
numero_de_circulos= int(turtle.numinput("Número de circulos","¿cuantos circulos quieres en tu regilete?",6))
for x in range (numero_de_circulos):
    tortuga.circle(123)
    tortuga.left(360/numero_de_circulos)
