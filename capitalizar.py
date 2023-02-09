

def valorAscii(cadena):
    cadenaLista=list(cadena)
    for i in range(0,len(cadenaLista)):
        # esta línea obtiene el valor dentro de la tabla ascii del caracter   print(ord(i))
       # if ord(i)>=65 and ord(i)<=90:   #mayúsculas rango  esta linea se simplifico a còmo esta abajo
        if 65 <= ord(cadenaLista[i]) <= 90:
            nuevoCaracter=ord(cadenaLista[i])+32
            cadenaLista[i]=chr(nuevoCaracter)
        # sin simplificar elif ord(i)>=97 and ord(i)<=122
        elif 97 <= ord(cadenaLista[i]) <= 122:
            nuevoCaracter=ord(cadenaLista[i])-32
            cadenaLista[i]=chr(nuevoCaracter)
    cadena=''.join(cadenaLista)
    print(cadena)


frase=input("Ingresa tu frase:")


valorAscii(frase)