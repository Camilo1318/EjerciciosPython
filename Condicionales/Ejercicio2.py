#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = input("Ingresa tu contraseña: ")
repeatPassword = input("Ingresa nuevamente tu contraseña: ")


def verificarPassword(password, repeatPassword):
    if password.lower() == repeatPassword.lower():
        return "Exito Siga con su vida"
    else:
        return "No sumerced, por aqui no puede seguir"
        
print(verificarPassword(password, repeatPassword))