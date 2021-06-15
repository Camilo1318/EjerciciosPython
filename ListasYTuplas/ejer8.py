#Defina una funcion max() que tome como argumento tres numeros y devuelva el mayor de ellos

#Cristian Pérez

def max(n1,n2,n3):

  if n1>n2 and n1>n3:
    return n1
  elif n2>n1 and n2>n3 :
    return n2
  else:
    return n3

x = max(200,100,3000)

print("Numero mayor:",x)