#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

#Cristian Pérez
asignaturas = ['Matematicas','Ingles']
notas = []
for indice in asignaturas:
  calificacion = float(input(f"Ingrese la nota de {indice} "))
  notas.append(calificacion)

for j in range(len(asignaturas)):
  print(f"""En {asignaturas[0]} has sacado: {str(notas[0])}""")



#Juan David
n_mat = float(input("ingrese nota matematica: "))
n_fis = float(input("ingrese nota fisica: "))
n_qui = float(input("ingrese nota quimica: "))
n_his = float(input("ingrese nota historia: "))
n_len = float(input("ingrese nota lengua: "))
asignaturas = ["Matematicas " + str(n_mat), "Fisica " + str(n_fis), "Quimica " + str(n_qui) , "Historia " + str(n_his), "Lengua " + str(n_len)]
print(asignaturas[:])


#Juan Diego


asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
notas = []

for i in asignaturas:
  calificacion = float(input(f"Ingrese la nota de {i} "))
  notas.append(calificacion)

for j in range(len(asignaturas)):
  print(f"""En {asignaturas[0]} has sacado: {str(notas[0])}""")







