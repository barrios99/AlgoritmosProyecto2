#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Proyecto #2 de Algoritmos y Estructuras de Datos
#Recomendacion de Amigos
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="1111")

def addPersona(nombre):
    persona= gdb.nodes.create(name=nombre)
    persona.labels.add("persona")

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

def getPersona(nombre):
    buscar="match (persona{name:'"+nombre+"'})-[x]->(d) return x,d"
    resultados = gdb.query(buscar, data_contents=True)
    listado = resultados.rows
    loficial=[]
    for x in listado:  
        for i in x: 
            for c in i:
                if c is not None:
                    loficial.append(i[c])
    return loficial

def getPersonas():
    buscar="match (n:persona) return n"
    resultados = gdb.query(buscar, data_contents=True)
    listado=resultados.rows
    loficial=[]
    for x in listado:  
        for i in x: 
            for c in i:
                if c is not None:
                    loficial.append(i[c])
    return loficial

def gustosPersonas(persona, personas):
    loficial=[]
    for x in personas:
        a=getPersona(x)
        if a is not None:
            loficial.append(a)
    return loficial

def buscaruno(persona, personas):
    return personas.index(persona)

def algoritmo(persona, personas):
    indice=buscaruno(persona, personas)
    tamaño=len(personas)
    comun=[]
    total=[]
    for i in range(0,tamaño):
        com=0
        tot=0
        for x in personas[i]:
            if x is personas[indice]:
                com=com+1
        comun.append(com)
        tot=(len(personas[i])+len(personas[indice]))-com
        total.append(tot)
    otro=[]
    otro.append(comun)
    otro.append(total)
    return otro
    
            
            

nombre=input("Ingrese un nombre completo")
print(algoritmo(nombre, getPersonas()))
