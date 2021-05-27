#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

#Juan David
nombre = input("¿cual es su nombre? ")
sexo = input("¿cual es su sexo? (F o M) ")

def grupo(nombre,sexo):
 
  primer_letra = nombre[0].lower()
  if (primer_letra < "m") and (sexo.lower() == "f"):
    return "perteneces al grupo A"
  elif (primer_letra > "n") and (sexo.lower() == "m"):
    return "perteneces al grupo A"
  else: 
    return  "perteneces al grupo B"
  
print(grupo(nombre, sexo))


#Cristian Pérez
name = input("nombre: ")
sexo = input("sexo (masculino/femenino): ")

def decideGrupo(name,sexo):
  primer_letra = name[0].lower()
  if sexo != 'masculino' or sexo !='femenino':
    
    return "Usted no es ni hombre ni mujer.."

  else:
    
    if primer_letra < 'm' and sexo.lower() == 'masculino':
      return f"{name} es hombre y pertenece al Grupo A"
    elif primer_letra>'n' and sexo.lower() == 'femenino':
      return f"{name} es mujer y pertenece al Grupo A"
    else:
      return f"{name} pertenece al Grupo B"
    
    

print(decideGrupo(name,sexo))    


#yosi
nombre=input("Ingrese su nombre: ")
genero=input("Ingrese su género por favor -femenino- o -masculino- : ")

def agrupar(nombre,genero):
  listaMujer = ["a","b","c","d","e","f","g","h","i","j","k","l"]
  listaHombre = ["o","p","q","r","s","t","u","v","w","x","y","z"]
 
  letra = nombre[0]
  if letra.lower() in listaMujer and genero.lower() == "femenino":
    print("Pertenece al grupo A")
  elif letra.lower() in listaHombre and genero.lower() == "masculino":
    print("Pertenece al grupo A")
  else:
    print("Pertenece al grupo B")

agrupar(nombre,genero)

#Juan Diego

nombre = input("Introduzca su nombre: ")
genero = input("Introduzca su genero (masculino o femenino): ")

def vergrupo(nombre, genero):
  primer_letra = nombre[0].lower()
  if genero == 'masculino' or genero == 'femenino':

    if primer_letra <'m' and genero.lower() == 'femenino':
      return "Pertenece al grupo A"
    elif primer_letra >'n' and genero.lower() == 'masculino':
      return "Pertenece al grupo A"
    else:
      return "Pertenece al grupo B"
    
  else:
    
    return "Introduzca un genero valido"
    
  

print(vergrupo(nombre, genero))
