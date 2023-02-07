"""

desarrollar programa q solicite su nombre, apellido paterno y materno

de ahì, recorrer cada cadena de texto y capitalizarla (se imprima en mayusculas) despues concatenar
todas las cadenas a una nueva variable y usando slicing vamos a imprimir la primera mitad de la nueva cadena
y en una nueva linea imprimir la otra mitad al revès
preguntar al usuario cuàntas veces quiere que se imprima su nomber en pantalla y mostrarlo

"""


def capitalizar(x):
    return x.capitalize()


def concatenar(x,y,z):
    return x + " " + y + " " + z


def mitades(x):
    tam=int(len(x)/2)
    nuevaMitad=x[tam:]
    print("\nla primera mitad del nombre es: "+x[:tam])
    print("\nla segunda mitad al revés es: "+nuevaMitad[::-1])


def imprimir(x,y):
    i=0
    while i < int (x):
        print(y)

        i += 1


print("Ingresa tu nombre: ")
nombre = input()

apellidoMaterno=input("\nIngresa tu apellido materno:")

apellidoPaterno=input("\nIngresa tu apellido paterno:")

# ahora recorremos toda la cadena y la capitalizamos

nombre=capitalizar(nombre)
apellidoPaterno=capitalizar(apellidoPaterno)
apellidoMaterno=capitalizar(apellidoMaterno)

print(nombre)
print(apellidoMaterno)
print(apellidoPaterno)


# ahora mostramos còmo se concatena cada cadena

nombreCompleto=concatenar(nombre,apellidoPaterno,apellidoMaterno)

print(nombreCompleto)

mitades(nombreCompleto)

#ahora veremos cuantas veces quiere el usuario imprimir su nombre

veces=input("\n¿Cuántas veces deseas imprimir tu nombre?")

imprimir(veces,nombreCompleto)


