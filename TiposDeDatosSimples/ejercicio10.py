#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#Juan David
payasos = int(input("ingrese el numero de payasos "))
muñecas = int(input("ingrese el numero de muñecas "))
print("el peso total es " + str((payasos*112)+(muñecas*75))+ " gramos")


#Cristian Pérez
peso_payaso = 112
peso_muñeca = 75

payasos = int(input("Ingrese cantidad de payasos: "))
muñecas = int(input("Ingrese cantidad de muñecas: "))

total_peso_payasos = payasos*peso_payaso
total_peso_muñecas = muñecas*peso_muñeca

total_peso = total_peso_payasos + total_peso_muñecas

print(f"""

  Total Payasos: {payasos} unidades
  Total Muñecas: {muñecas} unidades
  
  Total Peso Payasos: {total_peso_payasos} gr
  Total Peso Muñecas: {total_peso_muñecas} gr

  Total peso de la carga: {total_peso} gr

""")


#Juan Diego
payasos = int(input("Introduzca el numero de payasos vendidos en el ultimo pedido: "))
muñecas = int(input("Introduzca el numero de muñecas vendidos en el ultimo pedido: "))

peso_total = 112*payasos + 75*muñecas

print(f"El peso total del paquete que sera enviado es: {peso_total} gramos")