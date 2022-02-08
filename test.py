
archivo = open("car.data","r", encoding = "utf-8")
contenido = archivo.readlines()

salida = open("datos.txt","w")
def transforma1(parametro):
    if(parametro == "vhigh"):
        parametro = "1"
    if(parametro == "high"):
        parametro = "2"
    if(parametro == "med"):
        parametro = "3"
    if(parametro == "low"):
        parametro = "4"
    return parametro

def transforma2(parametro):
    if(parametro == "5more"):
        parametro = "4"
    if(parametro == "more"):
        parametro = "3"
    if(parametro == "small"):
        parametro = "1"
    if(parametro == "med"):
        parametro = "2"
    if(parametro == "big"):
        parametro = "3"
    if(parametro == "low"):
        parametro = "1"
    if(parametro == "high"):
        parametro = "3"
    return parametro

for i in range(0,len(contenido),1):
    dato = contenido[i]    
    posComa = dato.find(",")
    buying = dato[:posComa]
    dato = dato[posComa+1:]
    posComa = dato.find(",")
    maint = dato[:posComa]
    dato = dato[posComa+1:]
    posComa = dato.find(",")
    doors = dato[:posComa]
    dato = dato[posComa+1:]
    posComa = dato.find(",")
    persons = dato[:posComa]
    dato = dato[posComa+1:]
    posComa = dato.find(",")
    lug_boot = dato[:posComa]
    dato = dato[posComa+1:]
    posComa = dato.find(",")
    safety = dato[:posComa]
  
    salida.write(transforma1(buying)+","+transforma1(maint)+","+transforma2(doors)+","+transforma2(persons)+","+transforma2(lug_boot)+","+transforma2(safety)+"\n")
    # salida.write(buying)
salida.close()

