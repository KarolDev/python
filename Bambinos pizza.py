#input
pizza = eval(input("¿Cuantas pizzas quiere?: "))
#input
costo = eval(input("¿Cuanto cuesta esa pizza?: "))
#genericStep
costoTotal = pizza * costo
#genericStep
costoEnvio = costoTotal * .8
#genericStep
costoFinal = costoEnvio + costoTotal
#output
print("$",costoFinal," costo final + envío :)")
input("")
