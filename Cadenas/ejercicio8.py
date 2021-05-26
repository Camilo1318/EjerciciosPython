#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

#Cristian Pérez
precio_producto = int(input("Precio del producto: "))
posicion_dot = precio_producto.find('.')

print(f"""
  Euros: {precio_producto[:posicion_dot]}
  Centavos: {precio_producto[posicion_dot+2:]}
""")


 #[    INICIO    :   FIN      ]

#Yosi
precio = input("Ingrese el precio del producto: ")
num = precio.find(".")
parte1 = precio[:num]
parte2 = precio[num+1:]

print(f"La primera parte es:  {parte1} la segunda parte es: {parte2}" )


12.98

#Juan Diego

precio = int(input("Precio del producto: "))
numeroeuros = precio.find('.')
parte1 = precio[:numeroeuros]
parte2 = precio[num+1:]
print(f"""
Euros: {parte1} 
Centimos: {parte2}
""")
