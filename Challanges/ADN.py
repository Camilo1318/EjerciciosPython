#La descripcion del ejercicio se encuentra en la seccion Retos de discord


#00000101010101010101
#00101010101101110111
#00100010010000001001

#Juanda

muestra = "00101010101011111101"
longitud = len(muestra)

sospechosos = ["Pedro","Juan","Diego"]
cromosomas = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]
len_cromosomas = len(cromosomas)

datos_obtenidos = []

for j in range(len_cromosomas):
    cont = 0
    for i in range(longitud):
        if muestra[i] == cromosomas[j][i]:
            cont+=1
    datos_obtenidos.append(cont)
print(datos_obtenidos)
max_coin= max(datos_obtenidos)
indice_cul=datos_obtenidos.index(max_coin)
porcentaje= (max_coin/20)*100
print(porcentaje , "%")
print(sospechosos[indice_cul])


#Cristian Pérez

muestra = "00000101010101010101"
longitud = len(muestra)

sospechosos = ["Pedro","Juan","Diego"]
cromosomas = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]
len_cromosomas = len(cromosomas)

datos_obtenidos = []

for j in range(len_cromosomas):
    cont = 0
    for i in range(longitud):
        if muestra[i] == cromosomas[j][i]:
            cont+=1
    datos_obtenidos.append(cont)
    
max_coincidencias = max(datos_obtenidos)
index_culpable = datos_obtenidos.index(max_coincidencias)

porcentaje_culpable = (max_coincidencias*100//longitud)

print("Culpable:",sospechosos[index_culpable],porcentaje_culpable,"%")




#Juan Diego

muestra = "10101010001111101101" 
longitud = len(muestra)


sospechosos = ["Pedro", "Juan", "Diego"]
cromosomas = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]  
len_cromosomas = len(cromosomas)


datos_obtenidos = []

for j in range(len_cromosomas):
    cont = 0
    for i in range(longitud):
      if muestra[i] == cromosomas[j][i]:
        cont+=1
    datos_obtenidos.append(cont)

max_coincidencias = max(datos_obtenidos)
index_culpable = datos_obtenidos.index(max_coincidencias)

porcentaje_culpable = (max_coincidencias*100//longitud)


print("Culpable:",sospechosos[index_culpable],porcentaje_culpable, "%")
