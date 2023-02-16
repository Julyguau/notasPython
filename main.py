#COLLECIONES
'''

my_list = [] de esta manera indicamos que una lista está vacía
my_list = [3,2.5] de esta manera metemos valores a esta lista

para  acceder a la posición

my_list[1]

para cambiar el dato de la posición

my_list[9]="Adiós"

para agregar un elemento a una lista, lo hacemos del modo:
añade al final
my_list.append(8)

para eliminar un elemento específico

del(my_lista[x])        x es cualquier númerico

my_lista.pop()
my_lista.pust(3.5)

my_tupla=()
my_other_tupla=(3,6,5.7,"33")

my_new_tupla=my_other_tuplan+(4,8,"ABC") esto nos dará como resultado = (3,6,5.7,"33",4,8,"ABC")

my_other_tupla[5]
my_other_tupla=[2]

new_tuple[1]="ERRE" ESTO NO FUNCIONARÁ


ACÁ PARA TRABAJAR CON CONJUNTOS LO HACEMOS DE MODO QUE SE LLAMAN "SET"

my_set=set() ACÁ ES PARA INDICAR QUE ESTÁ VACÍO
new_set={1,"dos",3,4.5}     ACÁ YA INDICAMOS QUE TIENE ESTOS ELEMENTOS
my_set.add("Hola")      ACÁ AÑADE es importante recordar que lo añade sin orden pues los conjuntos no tienen orden al momento de imprimir
my_set.add("dos")

para concatenar se añade a otra variable

other_set=my_set.union(new_set)
imprime ("Hola",1,3,4.5,"dos")

my_other_set=my_set.intersection(new_set)
imprime ("dos")



DICCIONARIOOOOOS


dict={} acá es un diccionario vacío

new_dict={

"clave 1":"valor 1",
"clave 2":"valor 2"

}

new_dict["clave 1"]   te imprime valor 1
new_dict[1] va a imprimir valor 2
new_dict[1]="Valor 2"

AHORA PARA AÑADIR ELEMENTOS EN DICCIONARIOS

my_dict["nuevo_clave"]="nuevo valor"
del(my_dict["nueva_clave"])

'''

my_dict={

    "clave 1" : "hola",
    "clave 2" : "buenas",
    "clave 3" : "tardes",
    "clave 4" : 3

}

print(my_dict.keys())
print(my_dict.keys())
print(my_dict.keys())
