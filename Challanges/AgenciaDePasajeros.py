#Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#-Agregar pasajeros a la lista de viajeros.
#-Agregar ciudades a la lista de ciudades.
#-Dado el DNI de un pasajero, ver a qué ciudad viaja.
#-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#-Dado el DNI de un pasajero, ver a qué país viaja.
#-Dado un país, mostrar cuántos pasajeros viajan a ese país.
#-Salir del programa.

pasajeros = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]

ciudades = [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]


def agregaPasajeros():
  nombre = input("Ingrese el nombre del pasajero: ")
  dni = int(input("Ingrese su cedula: "))
  destino = input("Ingrese la ciudad de destino: ")
  pasajero = nombre,dni,destino
  pasajeros.append(pasajero)
  print(" Resultado ".center(70,"#"))
  print("Pasajero agregado con exito")

def agergaCiudades():
  destino = input("Ingrese una nueva ciudad destino: ")
  pais = input("Ingrese el pais de la ciudad: ")
  ciudad = destino,pais
  ciudades.append(ciudad)
  print(" Resultado ".center(70,"#"))
  print("ciudad agregada con exito")

  

def getCityByDni(dni):
  resultado = [elemento for elemento in pasajeros if elemento[1] == dni]
  if resultado == []:
    print(" Resultado ".center(70,"#"))
    print("Pasajero no encontrado")
  else:
    nombre,dni,destino = resultado[0]
    print(" Resultado ".center(70,"#"))
    print(f"El pasajero con dni: {dni} y nombre: {nombre} tiene destino: {destino}")

def countPasajerosByCity(ciudad):
  resultado = [pasajero for pasajero in pasajeros if pasajero[2] == ciudad]
  cantidad = len(resultado)
  print(" Resultado ".center(70,"#"))
  print(f"La cantidad de pasajeros que tienen como destino {ciudad} son: {cantidad}")

def getCountryByDni(dni): 
  for pasajero in pasajeros:
    for ciudad in ciudades:
      if pasajero[2] == ciudad[0] and pasajero[1] == dni:
        print(" Resultado ".center(70,"#"))
        print(f"El pasajero tiene destino al pais de: {ciudad[1]}")
        break

def countPasajerosByCountry(country):
  count = 0
  for pasajero in pasajeros:
      for ciudad in ciudades:
        if pasajero[2] == ciudad[0] and ciudad[1] == country:
          count+=1
  print(" Resultado ".center(70,"#"))
  print(f"La cantidad de pasajeros con destino a {country} es de: {count}")

#Main
opcion = -1
while(opcion != 7):
  print("Menu".center(70,"#"))
  print('''Agencia de Viajes
  Ingrese una opcion de las establecidad para realizar una consulta:
  1-Agregar pasajeros a la lista de viajeros.
  2-Agregar ciudades a la lista de ciudades.
  3-Dado el DNI de un pasajero, ver a qué ciudad viaja.
  4-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
  5-Dado el DNI de un pasajero, ver a qué país viaja.
  6-Dado un país, mostrar cuántos pasajeros viajan a ese país.
  7-Salir del programa.

  ''')
  try:
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
      agregaPasajeros()
    elif opcion == 2:
      agergaCiudades()
    elif opcion == 3:
      dni = int(input("Ingrese un dni de pasajero: "))
      getCityByDni(dni)
    elif opcion == 4:
      ciudad = input("Ingrese una ciudad de destino: ")
      countPasajerosByCity(ciudad)
    elif opcion == 5:
      dni = int(input("Ingrese el dni del pasajero: "))
      getCountryByDni(dni)
    elif opcion == 6:
      pais = input("Ingrese el nombre del pais: ")
      countPasajerosByCountry(pais) 
    elif opcion == 7:
      print("Hasta Pronto!")
    else:
      print("Error, ingrese una opcion valida!") 
  
  except:
    print("Opcion no valida, ingrese un numero")

  









