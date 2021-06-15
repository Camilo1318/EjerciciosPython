#La descripcion del ejercicio se encuentra en la seccion Retos de discord


#00000101010101010101
#00101010101101110111
#00100010010000001001

#Cristian Pérez
#Base de datos

muestra = "00101010101011111101"
longitud = len(muestra)

sospechosos = ["Pedro","Juan","Diego"]
cromosomas = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]
cont = 0
datos_obtenidos = []
for j in cromosomas:
    for i in range(longitud):
        if muestra[i] == cromosomas[0][i]:
            cont+=1

