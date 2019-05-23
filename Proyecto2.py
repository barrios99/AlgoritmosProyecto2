#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Proyecto #2 de Algoritmos y Estructuras de Datos
#Recomendacion de Amigos
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

import random
from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="1111")

nombres = ["Aaron López","Benjamin Gracía", "Samuel Morales", "David Ajú", "Daniel Hernández", "Alex Pérez", "Alexis González", "Eusebio Florido", "Elean Rivas", "Markus Florido", "Rodrigo Zea", "Mario Hernández", "Florencio Pérez", "Julio Garrido", "Oscar Navas", "Gustavo Sanchez", "Andy Salas", "Cristian Alvarado", "Cristian Escobar", "Josue Flores","Carlos Rojas", "Helen Nataly Pérez", "Benja Garicia", "Wilson Mux", "Edgardo Loncho", "Luis Pedro Rosales", "Frank Becerra", "Adolfo Velásquez", "Joel Gutierrez", "Fernanda Villa", "Vale Escamilla", "Gabriel Gonzalez", "Richard Lara", "Dante Romeo", "Liggia Gutierrez", "Diego Sánchez", "Valentin Novo", "Ian Rovelo", "Erick Mejicanos", "Edgar Aju", "Elena Aju", "Martín Isaac Juárez", "Alberto Rivia", "Byron Yac", "Karen Galaviz Huerta","Luis Ángel Meléndez Reyes", "Pablo Orozco", "Ramon Poncho Rocha Arana", "Diego López", "José Aroche", "Lesvia de Leon", "Efrain Flores", "José G Barrón", "Amy Perez", "Victoria Umul", "Daniela Luna Gómez", "Alejandro Mora", "Lizz Perez", "Miguel Angel Morales Arjonilla", "Abel Yac", "Fernando Alfonso", "Ivan Xicay", "Kevin Aguilar", "Eva Guerra", "Paulina Piñón Delgadillo", "Edgar Rosales", "Gehovani Linares", "Katy Guzman", "Mynor Josué Rodríguez Díaz", "Lupe Nájera", "David Alberto Avila Belisle", "Sofia Limatú", "Axel Aju Yac", "Mishelle Menéndez", "Esteban Andrade", "Marce Cuellar", "Mauricio Pérez", "Julia de Leon", "Adrian Tello", "Andreé Ruano", "Kenny Salazar", "Isaac Gómez Rivera", "Denilson Alvarado", "Didier Estrada Luna", "Leonardo Lopez", "Ade Pérez", "Luis García", "Mario Casanova Jerónimo", "Leonardo Aju Yac", "Alejandro Hurtado Agustin", "Byron Castillo", "Alejandro Salazar", "Luis Pedro Valenzuela Ambrosy", "Pati Barillas", "Jose Castellanos", "Karla González", "Mafer Siliezar", "Daniel Eduardo Conde", "Alejandro Martínez", "Angel Bucaro", "Lucía Estrada", "Diego Govea", "Lucía Arias López", "Geovanni Polanco", "Herber David Joj Oxlaj", "Cristian Emiliano Godínez", "Diana Laura Rodríguez Oliveros", "Bruno Calcaneo", "Juan Pablo Rodriguez", "Dulce Morales", "Leo Ramírez", "Diana Vasquez", "Susan Pérez", "Dennice Solis", "Diego Alvarado", "Angel Arroyo", "Jorge Eduardo Gomez Martinez", "Alejandra Celis", "Cristopher Ovando", "Cristian Solares", "Diana Martinez", "Pily Calderón", "Pablo Noriega", "Isaim Palacios", "Susana Cruz", "Angel Sandoval", "Rodrigo González", "Sofia Arriola Vielman", "Maria Luisa Maas Gamboa", "Rocío Rodríguez", "Ana Pellecer", "Manuel Miranda", "Andrea Mendoza", "Sofia Mejia", "Monse Erazo", "Marcela Lira", "Luz Rivas", "Melida Perez", "Mariel Rodríguez", "Pablo Aldana", "Víctor Eduardo Rodríguez Oliveros", "Natalia Garza", "Alejandro Ajú", "Samuel Perez", "Alejandra Ortiz Felipe", "Karen Perez", "Evelyn Juarez", "Cristopher Salazar", "Sarahí Mejía", "Kathy Zaragoza", "Ricardo Paniagua", "Javier Díaz", "Gabriela Gómez", "Maria Jose Rodriguez", "Adriana Mendoza", "Sofia Dardon", "Anderson Lopez", "Carlos Mejicanos", "Pedro Rodríguez", "Gabriela Guzman", "Juan Chiroy", "Gaby Hurtarte", "Miriam Zuleta", "Marcela Diaz", "Sebastian Rovelo", "Nicolle Larios", "Jennifer Laparra", "Mafer Mendoza", "Julia Ramirez", "Eduardo González", "Diego Barrios", "Roberto Monzón", "Marlon Daniel Roldan Zamora", "Luis Rodas", "Josselin Celada", "Julio Castellanos", "Max Mérida", "Andreé Zepeda", "Lester Marroquín", "Alex Azurdia Maltez", "Cesar Javier Cabrera", "Diana Montenegro", "Sofia Herrera", "Gabriela Aguilar", "Pedro Pablo Mancilla", "Andrés Vásquez", "Laura Vasquez", "Cristian Ixcoy", "Diego Reyes", "Rosa Santos", "José Pablo Cifuentes", "Carlos Eduardo Ruano", "Ana Paula Gómez Ruano", "Josue Galindo", "Alan Mendoza", "Samantha Guzmán", "Luisa Fernanda Velásquez", "David Caceres", "Beto Juarez Morales", "Alexis Lopez", "Karina Solis", "José Pablo Valdés", "Pamela Rendon", "Alejandro Cuellar", "Carlos Ruiz", "Anahi Figueroa", "Jorge Orozco", "Marisol Morales", "Josué Mendoza", "Nicole Castellanos", "Joshua Girón", "Pablo Hernández", "Ricardo Santamarina", "Isabel Pellecer", "Eleonora Pereira Miranda", "Luis Rodriguez", "Andrea Blanco", "Axel Mejia", "José Esteban Montúfar Alveño", "Cristian Santos", "Diana Navarro", "Diego Castañeda", "Jesús Recinos", "David Morales", "Erick Muñoz", "Pablo Ponciano", "Karla Velásquez", "Herminio Gomez", "Willy Cuellar", "Sara Garcia", "Sofia Lopez", "Pamela Chavez", "Rodrigo Cruz", "Pablo Vicente Borrego", "Sara Pac", "Alma Chavez", "Alejandro Lima", "Andrea Zúñiga", "Priscila Flores", "Andrea Ochoa", "Natalia Díaz", "Marleny Pérez", "Stephany Castellanos", "Sulay León", "Natalie Peralta", "Kendra Perez", "Julieta Mendez", "Anderson Ordoñez", "Emmanuel Ruiz", "Otto Galicia", "Áxel Rivera Corona", "Adrian Ocampo", "Sofy Fernandez", "Fátima Fuentes", "Fernando Fuentes", "Paulina Sitán", "Alejandra Ordoñez", "Alex Vasquez", "Julio López", "Alexander Aragón", "Rossana Jiménez", "Abner Vasquez", "Andrea Chiroy", "Gilberto Cuellar", "Zugely Ramos", "Zugely Ramos", "Sofía Pac", "Lucia Castro", "David Letona", "Delmy de Leon", "Monica Marroquin", "Gustavo Martinez", "Cesar Palencia Mazariegos", "Luis David Mendoza", "Carmen Garcia", "Bryan Gaytan", "Nicole Rivera", "Katherine Aguilar", "Mónica Corado", "Lourdes Mël", "Luisa Fernanda Muñoz", "María José Rodriguez", "Claudia Alvarez", "Santos Perez", "Flor Díaz González", "Pablo Medrano", "Douglas De Leon", "Sergio Balderas", "Jimena Castañeda", "Paula Dardon", "Andres Marquez Maldonado", "Emanuel Vivar", "Adriana Villaseñor", "Luis Toj", "Eduardo López", "Paula Castillo", "Jasson Aguirre", "Allan Perez", "Darym Garcia", "Desiree Maldonado"]
correos=["gator@comcast.net", "konit@msn.com", "dinther@icloud.com", "stecoop@live.com", "kempsonc@aol.com", "naoya@me.com", "techie@outlook.com", "sonnen@comcast.net", "philb@yahoo.com", "cmdrgravy@msn.com", "corrada@att.net", "grinder@me.com", "hling@mac.com", "rattenbt@yahoo.com", "cvrcek@verizon.net", "stomv@live.com", "mgreen@mac.com", "bescoto@me.com", "violinhi@hotmail.com", "philen@msn.com", "gtaylor@sbcglobal.net", "matsn@sbcglobal.net", "mhouston@aol.com", "pavel@mac.com", "xnormal@att.net", "miturria@mac.com", "smallpaul@msn.com", "bjornk@mac.com", "bsikdar@icloud.com", "ducasse@hotmail.com", "andrei@yahoo.ca", "british@live.com", "slaff@att.net", "dbindel@gmail.com", "zavadsky@att.net", "alias@yahoo.com", "hllam@icloud.com", "gemmell@yahoo.com", "darin@msn.com", "murdocj@me.com", "aaribaud@sbcglobal.net", "mstrout@hotmail.com", "calin@att.net", "kspiteri@msn.com", "mxiao@me.com", "muadip@yahoo.ca", "mfleming@comcast.net", "srour@yahoo.com", "matthijs@att.net", "adhere@optonline.net", "studyabr@icloud.com", "campbell@optonline.net", "hoyer@aol.com", "munjal@verizon.net", "szymansk@hotmail.com", "gbacon@icloud.com", "scitext@yahoo.com", "brickbat@att.net", "jipsen@mac.com", "cgarcia@comcast.net", "amichalo@sbcglobal.net", "pontipak@me.com", "chlim@att.net", "liedra@yahoo.ca", "pplinux@icloud.com", "pplinux@sbcglobal.net", "alastair@yahoo.ca", "padme@yahoo.ca", "kayvonf@yahoo.ca", "inico@yahoo.ca", "pspoole@verizon.net", "bryam@me.com", "cgreuter@verizon.net", "bartlett@verizon.net", "miami@icloud.com", "afeldspar@msn.com", "jgoerzen@comcast.net", "mkearl@msn.com", "earmstro@live.com", "library@icloud.com", "camenisch@hotmail.com", "gavollink@verizon.net", "duchamp@hotmail.com", "aibrahim@gmail.com", "hmbrand@yahoo.ca", "jimxugle@msn.com", "paley@outlook.com", "yzheng@hotmail.com", "psharpe@me.com", "parsimony@me.com", "hahsler@msn.com", "jimmichie@optonline.net", "imightb@hotmail.com", "guialbu@me.com", "ccohen@sbcglobal.net", "microfab@mac.com", "gregh@hotmail.com", "errxn@msn.com", "oechslin@mac.com", "ilikered@hotmail.com", "dougj@verizon.net", "attenbt@hotmail.com", "jandrese@aol.com", "sinkou@me.com", "carroll@yahoo.com", "mgreen@yahoo.ca", "bolow@att.net", "kimvette@icloud.com", "janneh@sbcglobal.net", "sartak@hotmail.com", "maneesh@verizon.net", "curly@msn.com", "shaffei@verizon.net", "maikelnai@att.net", "froodian@yahoo.com", "dowdy@att.net", "zyghom@icloud.com", "hillct@icloud.com", "durist@aol.com", "raines@me.com", "jshearer@outlook.com", "bescoto@yahoo.com", "linuxhack@att.net", "sjava@msn.com", "gospodin@att.net", "crowl@verizon.net", "goresky@msn.com", "enintend@me.com", "jshirley@icloud.com", "noneme@mac.com", "dmbkiwi@yahoo.ca", "isorashi@icloud.com", "kewley@optonline.net", "bader@yahoo.com", "jesse@optonline.net", "snunez@aol.com", "miturria@sbcglobal.net", "marin@verizon.net", "philb@hotmail.com", "overbom@sbcglobal.net", "avalon@gmail.com", "gomor@icloud.com", "itstatus@sbcglobal.net", "amaranth@outlook.com", "jnolan@msn.com", "koudas@sbcglobal.net", "tbmaddux@outlook.com", "treit@optonline.net", "wildixon@comcast.net", "rgarcia@icloud.com", "overbom@verizon.net", "dcoppit@verizon.net", "skajan@aol.com", "cyrus@verizon.net", "tubesteak@me.com", "tezbo@yahoo.ca", "jadavis@hotmail.com", "hampton@verizon.net", "thassine@verizon.net", "aibrahim@att.net", "madanm@msn.com", "jdray@me.com", "jugalator@icloud.com", "comdig@mac.com", "mrdvt@yahoo.com", "msroth@live.com", "joglo@outlook.com", "panolex@mac.com", "amichalo@mac.com", "webinc@hotmail.com", "flavell@yahoo.com", "carmena@gmail.com", "lcheng@optonline.net", "pontipak@hotmail.com", "catalog@aol.com", "bryanw@icloud.com", "schumer@live.com", "jcholewa@aol.com", "mxiao@optonline.net", "kohlis@hotmail.com", "jshirley@comcast.net", "mobileip@verizon.net", "ccohen@icloud.com", "knorr@att.net", "emmanuel@aol.com", "dougj@icloud.com", "whimsy@icloud.com", "aegreene@verizon.net", "jesse@live.com", "mnemonic@aol.com", "rupak@yahoo.ca", "dartlife@gmail.com", "heidrich@msn.com", "boomzilla@optonline.net", "sokol@yahoo.com", "unreal@msn.com", "inico@hotmail.com", "smallpaul@live.com", "mcnihil@hotmail.com", "avalon@me.com", "juerd@att.net", "qrczak@live.com", "offthelip@live.com", "cgcra@aol.com", "tmaek@optonline.net", "mjewell@icloud.com", "rupak@verizon.net", "kuparine@msn.com", "ideguy@yahoo.ca", "mastinfo@icloud.com", "frikazoyd@sbcglobal.net", "vlefevre@optonline.net", "kwilliams@sbcglobal.net", "pierce@live.com", "zavadsky@live.com", "itstatus@gmail.com", "fukuchi@yahoo.com", "ardagna@gmail.com", "afifi@me.com", "samavati@att.net", "choset@yahoo.com", "geeber@aol.com", "quantaman@hotmail.com", "mwilson@gmail.com", "salesgeek@hotmail.com", "cfhsoft@comcast.net", "campware@msn.com", "fudrucker@att.net", "mhassel@live.com", "ghaviv@comcast.net", "bader@live.com", "carreras@mac.com", "skoch@live.com", "jorgb@gmail.com", "gomor@sbcglobal.net", "hstiles@sbcglobal.net", "tamas@msn.com", "evans@outlook.com", "padme@verizon.net", "bahwi@outlook.com", "chaki@yahoo.com", "pedwards@icloud.com", "drolsky@icloud.com", "jgwang@yahoo.com", "jmgomez@verizon.net", "scottlee@mac.com", "gomor@hotmail.com", "ardagna@hotmail.com", "dgatwood@me.com", "policies@verizon.net", "sjmuir@outlook.com", "mhouston@optonline.net", "tarreau@msn.com", "ngedmond@live.com", "jlbaumga@hotmail.com", "esasaki@att.net", "lushe@comcast.net", "yfreund@aol.com", "bcevc@yahoo.ca", "solomon@sbcglobal.net", "chlim@hotmail.com", "engelen@att.net", "bowmanbs@aol.com", "chunzi@att.net", "stecoop@att.net", "pappp@aol.com", "chrisk@verizon.net", "laird@comcast.net", "north@comcast.net", "grossman@gmail.com", "seasweb@hotmail.com", "themer@icloud.com", "dinther@gmail.com", "goresky@mac.com", "mkearl@yahoo.com", "jacks@yahoo.com", "scotfl@msn.com", "afeldspar@live.com", "nelson@mac.com", "phizntrg@gmail.com", "frosal@yahoo.com", "paina@optonline.net", "bhtower@outlook.com", "danzigism@verizon.net", "shawnce@yahoo.com", "arandal@gmail.com", "mbalazin@comcast.net", "pavel@outlook.com", "seemant@sbcglobal.net", "natepuri@yahoo.ca", "jkegl@outlook.com", "ovprit@comcast.net", "mfleming@sbcglobal.net", "hllam@comcast.net", "ajohnson@hotmail.com", "akoblin@att.net", "arnold@outlook.com", "duncand@hotmail.com", "heroine@me.com", "panda@gmail.com"]

for x in range(300):
    addPersona(nombres[x], correos[x])
  
for x in nombres:
    n = random.randint(1, 11)
    if n == 1:
        addPersonalidad(x,"Pacificador")
    elif n == 2:
        addPersonalidad(x,"Reformador")
    elif n == 3:
        addPersonalidad(x,"Triunfador")
    elif n == 4:
        addPersonalidad(x,"Ayudador")
    elif n == 5:
        addPersonalidad(x,"Romántico")
    elif n == 6:
        addPersonalidad(x,"Investigador")
    elif n == 7:
        addPersonalidad(x,"Leal")
    elif n == 8:
        addPersonalidad(x,"Entusiasta")
    elif n == 9:
        addPersonalidad(x,"Desafiador")
    elif n == 10:
        addPersonalidad(x,"Extrovertido")
    elif n == 11:
        addPersonalidad(x,"Introvertido")
        

for x in nombres:
    n = random.randint(1, 11)
    if n == 1:
        addAmistad(x,"Confianza")
    elif n == 2:
        addAmistad(x,"Lealtad")
    elif n == 3:
        addAmistad(x,"Honestidad")
    elif n == 4:
        addAmistad(x,"Apoyo mutuo")
    elif n == 5:
        addAmistad(x,"Humildad")
    elif n == 6:
        addAmistad(x,"Solidaridad")
    elif n == 7:
        addAmistad(x,"Compañerismo")
    elif n == 8:
        addAmistad(x,"Tolerancia")
           


for x in nombres:
    n = random.randint(1, 18)
    if n == 1:
        addActividad(x,"Practicar deporte")
    elif n == 2:
        addActividad(x,"Ver películas o series")
    elif n == 3:
        addActividad(x,"Salir a comer")
    elif n == 4:
        addActividad(x,"Visitar familiares o amigos")
    elif n == 5:
        addActividad(x,"Ir a una fiesta")
    elif n == 6:
        addActividad(x,"Cocinar")
    elif n == 7:
        addActividad(x,"Bailar")
    elif n == 8:
        addActividad(x,"Escuchar música")
    elif n == 9:
        addActividad(x,"Jugar videojuegos")
    elif n == 10:
        addActividad(x,"Leer")
    elif n == 11:
        addActividad(x,"Voluntariado")
    elif n == 12:
        addActividad(x,"Pintar o dibujar")
    elif n == 13:
        addActividad(x,"Componer música")
    elif n == 14:
        addActividad(x,"Ordenar tu cuarto")
    elif n == 15:
        addActividad(x,"Aprender algo nuevo")
    elif n == 16:
        addActividad(x,"Recurrir a redes sociales")
    elif n == 17:
        addActividad(x,"Dormir")
    elif n == 18:
        addActividad(x,"Manualidades")



for x in nombres:
    n = random.randint(1, 14)
    if n == 1:
        addMusica(x,"Disco")
    elif n == 2:
        addMusica(x,"Reggaeton")
    elif n == 3:
        addMusica(x,"Salsa")
    elif n == 4:
        addMusica(x,"Pop")
    elif n == 5:
        addMusica(x,"Rock")
    elif n == 6:
        addMusica(x,"Electrónica")
    elif n == 7:
        addMusica(x,"Rap")
    elif n == 8:
        addMusica(x,"Trap")
    elif n == 9:
        addMusica(x,"Hip-hop")
    elif n == 10:
        addMusica(x,"Cristiana")
    elif n == 11:
        addMusica(x,"Jazz")
    elif n == 12:
        addMusica(x,"Metal")
    elif n == 13:
        addMusica(x,"Cumbia")
    elif n == 14:
        addMusica(x,"Merengue")




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
    prop=0
    recomendados=[]
    cdec=[]
    comdc=[]
    dev=[]
    gustos=gustosPersonas(persona, personas)
    for i in range(0,tamaño):
        com=0
        tot=0
        com=comunes(gustos[indice],gustos[i])
        comun.append(len(com))
        cdec.append(com)
        tot=(len(gustos[i])+len(gustos[indice]))-len(com)
        total.append(tot)
    for s in range(0, tamaño):
        prop=1-(comun[s]/total[s])
        if (prop<=0.5):
            if personas[s] is not personas[indice]:
                recomendados.append(personas[s])
                comdc.append(cdec[s])
    dev.append(recomendados)
    dev.append(comdc)
    return dev

def comunes(buscador, buscado):
    com=[]
    for x in buscado:
        if x in buscador:
            com.append(x)
    return com

def verificarNum(x):
    resultado = x.isnumeric()
    return resultado

nombre=input("Ingrese un nombre completo")
amigos=algoritmo(nombre, getPersonas())
for f in range(0, len(amigos[0])):
    print("\n")
    print(amigos[0][f])
    print("Cosas en comun con esta persona:")
    for d in amigos[1][f]:
        print(d)

