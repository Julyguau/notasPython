'''

try:

pass

except ZeroDivisionError:
si falla error específico

except Exception as e:

si falla cualquier otro error
pass
raise

else:
si el try se ejecutò sin error
pass

finally:
se hace independientemente pass
de si hubo error o no



'''
from math import sqrt


def num(n):

    try:
       numeroentero=int(n)
    except TypeError:
        print("Ingresa un numero entero")
    except ValueError:
        numeroentero=float(n)
    else:
       print(sqrt(numeroentero))


def numeroCuadrado(x):
    try:
        numeropotencia=int(x)
    except TypeError:
        print("Ingresa un numero valido")
    except ValueError:
        numeropotencia=float(x)
    else:
        print(numeropotencia**2)



print("Ingresa tu numero:")
numero=input()
num(numero)
#numeroCuadrado(numero)


