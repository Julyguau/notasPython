
#para definir variables 
numero = 2

palabra = "july gomez"

arreglo = [1,2,3,4]

print (numero,palabra,arreglo)


#imprime valores de otras variables dentro de un print
#con f
print(f"El siguiente arreglo de numero {arreglo}  ")

resultado= numero * 15

print(f"El resultado de multiplicar {numero} X 15 es {resultado}")

"texto" + str(arreglo) 


"""
así se imprime entre comentarios
"""

print("casa"*numero)

print(palabra[:3])

print(palabra[5:])

#x=0
#for x in palabra:

#    print(palabra[:x])
#    x+=1


#imprime cadena al revès

print(palabra[len(palabra)::-1])


cadena1="hola "
cadena2="¿cómo estás? "
cadena3="bien."

print(cadena1+cadena2+cadena3)

#para declarar variables es del tipo _ ejemplo 

num_grande= 2000040324324

#podemos separar numeros por guiones bajos, ejemplo

num_grande2= 20_312321_32312_23232
print("ingresa el nombre ")


x=input()


print(f"El nombre es {x}")
x=input(print("x:"))

"""
si quisiera ahorrarme espacio con esto, podría hacerlo como
x=input(print("x:"))
true false van siempre con mayúsculas al inicio

True False 

"""

"""

CICLOS 

para los if 

if True:
    pass
elif False:
    pass
elif (True and False):
    pass
else:
    pass

para los While

while True:
    pass
while True:
    if x>1:
        while x not 8:
            while x+=1


tupla = (1,2,3,4)
lista = ["A","B","C"]

dentro de una lista puedes incluir otra lista del modo
lista = ["A","B","C",[1,2,3]]

diccionario={

    key:"value",
    key2:"valor2"
    key3:none
    
    #puedo meter otro diccionario dentro de otro diccionario
    diccionario2:{
        key4:"dos"
        key5:"seis"
    }
}

lista.Add("z")
entonces aparecerá la z al final 
lista.remove(-1)
remueve z 


para copiar elementos de una lista se hace del modo

lista = ["A","B","C",[1,2,3]]

lista2=lista.copy()

funciones de listas son
lista.add() #añade en cierto indice
lista.append
lista.push()
lista.pop()
lista.remove()
.map()
.filter()



"""

#try catch de java funciona del modo

"""

try:
    pass

except:
    raise TypeError
finally:
    pass



"""
#syntax declarar funciones es
"""
def mi_funcion (arg1,arg2):
    pass
o puedo poner
    return x
o usar
    return none
o usar
    return mi_funcion(x,y,-1)
o usar
    return a+b
"""
