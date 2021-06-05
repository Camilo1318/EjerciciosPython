#La descripcion del ejercicio se encuentra en la seccion Retos de discord

#Cristian Pérez

def procesar_cadena(c):
  datos = c.split("&")
  
  if datos[0] == "1":
    retiro(int(datos[1]))
  elif datos[0] == "2":
    print("Deposito")
  elif datos[0] == "3":
    print(" Consultar Retiro")
  elif datos[0] == "4":
    print("Consultar Deposito")  
  elif datos[0] == "5":
    print("Finalizando Transaccion")

def retiro(valor):
    b50 = valor//50
    b20 = 0
    b10 = 0
    m50 = valor%50 
    if m50 != 0:
        b20 = m50//20
        m20 = m50%20
    elif m20 !=0:
        b10 = m20//10
        
        
    print(f"Retirando billetes son -> 50:{b50}, 20:{b20}, 10:{b10}.")

opciones = 0
while opciones != "5":
  opciones = (input("Ingrese una operacion: "))
  procesar_cadena(opciones)

