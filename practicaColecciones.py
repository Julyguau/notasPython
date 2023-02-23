

canciones={

    "cancion1":"getaway car",
    "cancion2":"speak now",
    "cancion3":"miau",
    "cancion4":"our song",
    "cancion5":"mine",
    "cancion6":"mean",
    "cancion7":"haunted",
    "cancion8":"lover",
    "cancion9":"delicate",
    "cancion10":"so it goes..."

}

def buscar(elemento):
    if elemento=="claves":
        for i in canciones.keys():
            print(i)

    elif elemento=="valores":
        for j in canciones:
            print(canciones[j])


variable=int(input("selecciona 1 ->claves \n selecciona 2 -> valores"))
if variable==1:
    buscar("claves")
elif variable==2:
    buscar("valores")