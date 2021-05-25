#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

#€

#Cristian Pérez
precio_pan = 3.49
valor_descuento = 0.4

print("Bienvenido a su Panaderia.../n")

numero_panes = int(input("Ingrese la cantidad de panes que no fueron del dia: "))
pan_descuento = precio_pan*valor_descuento
total_compra = pan_descuento*numero_panes 

print(f"""

Precio barra de pan habitual: {precio_pan} €
Precio barra de pan con descuento: {round(pan_descuento,2)} €
Precio total de la compra : {round(total_compra,2)} €

Gracias por su compra...
""")



#Juan David
precio_pan = 3.49
precio_descuento = precio_pan*0.4
panes = int(input("introduzca numero de panes: "))
print(str(precio_pan) + "€  precio habitual")
print(str(round(precio_descuento,2)) + ("€  precio por cada pan con el descuento"))
print(str(panes*precio_descuento) + ("€  valor total"))

#Juan Diego

barrasdepan = 3.49

descuento = 0.4

panrebaja = barrasdepan*descuento

panes_no_frescos = int(input("Ingrese la cantidad de panes que no son del dia: "))

costefinal = panrebaja*panes_no_frescos


print(f""" 
El precio habitual de un pan es: {barrasdepan} €
El descuento que se le hace por no ser fresco es: (60%) 
El coste final total es: {round(costefinal,2)} €

Esperamos vuelva pronto :) """)


