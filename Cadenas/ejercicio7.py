zxs#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

#Cristian Pérez

correo = input("Ingrese correo: ")
position_a_in_user = correo.find("@")
print(f"Nuevo Correo: {correo[:position_a_in_user]}@ceu.es")

# u s e r @ g m a i l .  c  o  m  => 3
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13


#Yosi
email = input("Ingrese su correo electronico: ")
num = email.find("@")
suma = email[0:num+1]
dominio = suma + "ceu.es"
print("El nuevo correo es: ", dominio )


#Juan Diego

correo = input("Introduzca su correo electronico: ")
partedelante = correo.find("@")
print(f"Nuevo correo: {correo[0:partedelante]}@ceu.es") 