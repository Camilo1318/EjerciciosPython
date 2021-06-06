#Reto de Cajero automatico: El challange se puede encontrar en el canal del discord Seccion Retos

#Cristian Pérez

def procesar_cadena(c, mayor_retiro, menor_retiro,menor_deposito,mayor_deposito,primer_retiro,primer_deposito,total_dinero):
  datos = c.split("&")
  
  if datos[0] == "1":
    retiro(int(datos[1]))
    total_dinero -=int(datos[1])
    resultado = elige_mayor_menor(int(datos[1]),mayor_retiro,menor_retiro,datos[2],primer_retiro)
    mayor_retiro = resultado[0]
    menor_retiro = resultado[1]
    primer_retiro  = resultado[2]
    
  elif datos[0] == "2":
    dinero_depositado = deposito(datos[1:4])
    total_dinero += dinero_depositado
    resultado = elige_mayor_menor(dinero_depositado,mayor_deposito,menor_deposito,datos[4],primer_deposito)
    mayor_deposito = resultado[0]
    menor_deposito = resultado[1]
    primer_deposito  = resultado[2]
    
  elif datos[0] == "3":
    valor = consultar_valor(datos[1],mayor_retiro, menor_retiro)
    print(f"El {datos[1]} retiro ha sido de: {valor[0]} ({valor[1]})")
  elif datos[0] == "4":
    valor = consultar_valor(datos[1],mayor_deposito, menor_deposito)
    print(f"El {datos[1]} deposito ha sido de: {valor[0]} ({valor[1]})")
  elif datos[0] == "5":
    print("Finalizando Transaccion")
    
  return [mayor_retiro,menor_retiro,mayor_deposito,menor_deposito,primer_retiro,primer_deposito,total_dinero]

def retiro(valor):
        
    b50 = valor//50
    b20 = 0
    b10 = 0
    m50 = valor%50
    m20 = m50%20
    if m50 != 0:
        b20 = m50//20
        m20 = m50%20
    elif m20 !=0:
        b10 = m20//10       
    print(f"Retirando billetes son -> 50:{b50}, 20:{b20}, 10:{b10}.")

def deposito(cantidades):
  total = 0
  total+= int(cantidades[0])*50
  total+= int(cantidades[1])*20
  total+= int(cantidades[2])*10
      
  print(f"Total Depositado: {total}")
  
  return total

def elige_mayor_menor(numero,mayor,menor,razon,primera_transaccion):
    if primera_transaccion:
        primera_transaccion = False
        mayor = [numero,razon]
        menor= [numero,razon]
    else:
        if numero>mayor[0]:
          mayor = [numero,razon]
        elif numero<menor[0]:
          menor = [numero,razon]
    return [mayor,menor,primera_transaccion]
    
def consultar_valor(tipo,mayor,menor):
    if tipo == "mayor":
        return mayor
    elif tipo == "menor":
        return menor
# Main

c_50 = 10 #int(input("Ingrese el total de billetes de 50: "))
v_20 = 10 #int(input("Ingrese el total de billetes de 20: "))
c_10 = 10 #int(input("Ingrese el total de billetes de 10: "))

total_dinero = 200
mayor_retiro = [0,"Sin movimientos"]
menor_retiro = [0,"Sin movimientos"]
mayor_deposito = [0,"Sin movimientos"]
menor_deposito = [0,"Sin movimientos"]

primer_retiro = True
primer_deposito = True

opciones = 0
while opciones != "5":
  opciones = (input("Ingrese una operacion: "))
  estado = procesar_cadena(opciones,mayor_retiro, menor_retiro,menor_deposito,mayor_deposito,primer_retiro,primer_deposito,total_dinero)
  mayor_retiro = estado[0]
  menor_retiro = estado[1]
  mayor_deposito = estado[2]
  menor_deposito = estado[3]
  primer_retiro = estado[4]
  primer_deposito = estado[5]
  total_dinero = estado[6]