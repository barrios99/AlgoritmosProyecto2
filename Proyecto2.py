#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Proyecto #2 de Algoritmos y Estructuras de Datos
#Recomendacion de Amigos
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="1111")

#Crea un nuevo nodo en la base de datos
def addPersona(nombre, correo):
    persona= gdb.nodes.create(name=nombre,email=correo)
    persona.labels.add("persona")

#Crea nuevas relaciones entre nodos
def addPersonalidad (nombre, tipos):
    persona= gdb.labels.get("persona")
    persona.all()
    personalidad=gdb.labels.get("personalidad")
    personalidad.all()
    persona.get(name=nombre)[0].relationships.create("mipersonalidad",personalidad.get(tipo=tipos)[0])

def addAmistad (nombre, valores):
    persona= gdb.labels.get("persona")
    persona.all()
    valor=gdb.labels.get("amistad")
    valor.all()
    persona.get(name=nombre)[0].relationships.create("valoro",valor.get(valor=valores)[0])

def addMusica (nombre, generos):
    persona= gdb.labels.get("persona")
    persona.all()
    musica=gdb.labels.get("musica")
    musica.all()
    persona.get(name=nombre)[0].relationships.create("musicapref",musica.get(generom=generos)[0])

def addOcupacion (nombre, clases):
    persona= gdb.labels.get("persona")
    persona.all()
    ocupacion=gdb.labels.get("ocupacion")
    ocupacion.all()
    persona.get(name=nombre)[0].relationships.create("Ocupadoen",ocupacion.get(clase=clases)[0])

def addActividad (nombre, actividades):
    persona= gdb.labels.get("persona")
    persona.all()
    actividad=gdb.labels.get("actividad")
    actividad.all()
    persona.get(name=nombre)[0].relationships.create("tiempolibre",actividad.get(hacer=actividades)[0])

#-------------------------------------------------------------------------------------------------------------------------------------------

#Devuelve una lista con todas las caracteristicas de una persona 
def getPersona(nombre):
    buscar="match (persona{name:'"+nombre+"'})-[x]->(d) return x,d"
    resultados = gdb.query(buscar, data_contents=True)
    listado = resultados.rows
    loficial=[]
    if listado is not None:
        for x in listado:  
            for i in x: 
                for c in i:
                    if c is not None:
                        loficial.append(i[c])
    return loficial

#Devuelve una lista con los nombres de todas las personas en la bd
def getPersonas():
    buscar="match (n:persona) return n"
    resultados = gdb.query(buscar, data_contents=True)
    listado=resultados.rows
    loficial=[]
    if listado is not None:
        for x in listado:  
            for i in x:
                if i["name"] is not None:
                    loficial.append(i["name"])
    return loficial

#Retorna una lista de todos los correos correspondientes a cada una de las personas
def getCorreos():
    buscar="match (n:persona) return n"
    resultados = gdb.query(buscar, data_contents=True)
    listado=resultados.rows
    loficial=[]
    if listado is not None:
        for x in listado:  
            for i in x:
                if i["email"] is not None:
                    loficial.append(i["email"])
    return loficial

#Devuelve una lista que contiene las listas de los gustos de todas las personas en la BD
def gustosPersonas(persona, personas):
    loficial=[]
    for x in personas:
        a=getPersona(x)
        if a is not None:
            loficial.append(a)
    return loficial

#Busca una persona en una lista
def buscaruno(persona, personas):
    a=-1
    if persona in personas:
        a=personas.index(persona)
    return a

#Algoritmo de recomendacion
def algoritmo(persona, personas, correos):
    indice=buscaruno(persona, personas)
    tamaño=len(personas)
    comun=[]
    total=[]
    prop=0
    recomendados=[]
    cdec=[]
    comdc=[]
    dev=[]
    correoc=[]
    #Obtiene los gustos de todas las personas
    gustos=gustosPersonas(persona, personas)
    #para cada persona en la bd
    for i in range(0,tamaño):
        com=0
        tot=0
        #obtiene los comunes
        com=comunes(gustos[indice],gustos[i])
        comun.append(len(com))
        cdec.append(com)
        #obtiene las caracteristicas totales
        tot=(len(gustos[i])+len(gustos[indice]))-len(com)
        total.append(tot)
    for s in range(0, tamaño):
        #formula de similitud
        prop=1-(comun[s]/total[s])
        #si supera la similitud establecidad
        #devuelve el nombre de la persona, su correo y las cosas en comun
        if (prop<=0.5):
            if personas[s] is not personas[indice]:
                if personas[s] not in recomendados:
                    recomendados.append(personas[s])
                    correoc.append(correos[s])
                    comdc.append(cdec[s])
    dev.append(recomendados)
    dev.append(comdc)
    dev.append(correoc)
    return dev

#Obtiene los gustos en comun entre dos personas
def comunes(buscador, buscado):
    com=[]
    for x in buscado:
        if x in buscador:
            if x not in com:
                com.append(x)
    return com




