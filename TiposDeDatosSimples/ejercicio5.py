#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


#Juan David
horas= int(input("cuantas horas trabajas?"))
valor_hora= int(input("cuanto vale cada hora?"))
valor_jornada= (horas*valor_hora)
print(f"El resultado es: {valor_jornada}")


#Juan Diego
horastrabajadas = int(input("Ingrese el numero de horas que trabaja: "))
costohora = int(input("Cuanto cobras por hora: "))
valordiario = horastrabajadas*costohora
print(f"Su paga diaria es: {valordiario}")



#Cristian Pérez
numeroHoras = int(input("Ingrese el numero de horas trabajadas: "))
precioHora = int(input("A como te pagan la hora? : "))
paga = numeroHoras*precioHora
print(f"El total de tu paga es de : {paga}")


#Yosi 

numeroHoras= int(input("Ingrese el número de horas trabajadas"))
coste = int(input("Ingrese su costo por hora"))
print("La paga que le corresponde a usted por su trabajo es: ", numeroHoras*coste)