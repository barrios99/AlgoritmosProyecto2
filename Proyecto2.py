#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Proyecto #2 de Algoritmos y Estructuras de Datos
#Recomendacion de Amigos
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

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
