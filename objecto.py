
diccionario={}


def ingresarelemento():
    clave=input("Ingresa la clave:\n")
    valor=input("Ingresa el valor de la clave: \n")
    diccionario[clave]=valor


def eliminarclave(clave):
    for j in diccionario:
        if j==clave:
            del(diccionario[j])
            print("La clave "+clave+" ha sido eliminada exitosamente.")
    else:
        print("no existe")


while True:
    respuesta=input("¿Ingresarás un nuevo atributo al diccionario?  s/n\n")
    if respuesta=="s":
        ingresarelemento()
    elif respuesta=="n":
        break


for i in diccionario:
    print(i+": "+diccionario[i])


respuesta2=input("¿Deseas eliminar una clave?   s/n \n")
if respuesta2=="s":
    eliminarclave(input("ingresa la clave que quieres eliminar"))
if respuesta=="n":
    print("ok")


for i in diccionario:
    print(i+": "+diccionario[i])


#print(diccionario)