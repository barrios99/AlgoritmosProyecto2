#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Proyecto #2 de Algoritmos y Estructuras de Datos
#Recomendacion de Amigos
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

#from Proyecto2 import *

#Verifica que el valor ingresado sea un numero
def verificarNum (x):
    resultado = x.isnumeric()
    return resultado

def opcion_rango (a,b,c):
    try:
        if a > b or a < c:
            return False
        else:
            return True
    except ValueError:
        return False

print("---------------   ¡Bienvenidos a MeetMe!   ---------------")

menu = ("\nEstas son las opciones que puede realizar:" +
        "\n1. Agregar una persona a la base de datos." +
        "\n2. Ingresar un nombre para conocer personas con los mismos gustos." +
        "\n3. Salir.")

opcion = 0

while (opcion != 3):
    print(menu)
    opcion = input("\nIngrese una opcion: ")
    validar = verificarNum(opcion)
    while validar == False:
        print("El dato ingresado es invalido.")
        opcion = input("Ingrese una opcion: ")
        validar = verificarNum(opcion)
    if validar == True:
        opcion = int(opcion)
        verificar = opcion_rango(opcion,3,0)
        while verificar == False:
            print("El dato ingresado es invalido.")
            opcion = input("Ingrese una opcion: ")
            opcion = int(opcion)
            verificar = opcion_rango(opcion,3,0)
        if verificar == True:
            #Agrega una nueva persona a la base de datos
            if opcion==1:
                print("---------------     1. INGRESAR UNA NUEVA PERSONA A LA BASE DE DATOS.     ---------------")
                nombre = input("Ingrese su nombre completo: ")
                correo = input("Por favor ingrese su correo electronico: ")
                #addPersona(nombre,correo)
                
                ocupacion = input("Ingrese '1' si estudia, ingrese '2' si trabaja o ingrese '3' si ambas: ")
                validar = verificarNum(ocupacion)
                while validar == False:
                    print("El dato ingresado es invalido.")
                    ocupacion = input("Ingrese '1' si estudia, ingrese '2' si trabaja o ingrese '3' si ambas: ")
                    validar = verificarNum(ocupacion)
                if validar == True:
                    ocupacion = int(ocupacion)
                    verificar = opcion_rango(ocupacion,3,0)
                    while verificar == False:
                        print("El dato ingresado es invalido.")
                        ocupacion = input("Ingrese '1' si estudia, ingrese '2' si trabaja o ingrese '3' si ambas: ")
                        ocupacion = int(ocupacion)
                        verificar = opcion_rango(ocupacion,3,0)
                    if verificar == True:
                        if ocupacion == 1:
                            e = "Estudiar"
                            #addOcupacion(nombre,e)
                        if ocupacion == 2:
                            t = "Trabajar"
                            #addOcupacion(nombre,t)
                        if ocupacion == 3:
                            et = ["Estudiar","Trabajar"]
                            #for i in et:
                                #addOcupacion(nombre,i)

                #Agrega el tipo de personalidad de la persona
                tipos = ["\n0. Pacificador", "1. Reformador", "2. Triunfador", "3. Ayudador", "4. Romántico", "5. Investigador", "6. Leal", "7. Entusiasta", "8. Desafiador", "9. Extrovertido", "10. Introvertido \n"]
                perso = ["Pacificador","Reformador","Triunfador","Ayudador","Romántico","Investigador","Leal","Entusiasta","Desafiador","Extrovertido","Introvertido"]
                for i in tipos:
                    print(i)
                personalidad = []
                parar = " "
                while parar != "n":
                    tipo = input("Ingrese el número de opcion que define su personalidad: ")
                    validar = verificarNum(tipo)
                    while validar == False:
                        print("Lo sentimos,el valor ingresado no es un numero.")
                        tipo = input("Ingrese el número de opción que define su personalidad: ")
                        validar = verificarNum(tipo)
                    if validar == True:
                        tipo = int(tipo)
                        verificar = opcion_rango(tipo,10,0)
                        while verificar == False:
                            print("El dato ingresado es invalido.")
                            tipo = input("Ingrese el número de opción que define su personalidad: ")
                            tipo = int(tipo)
                            verificar = opcion_rango(tipo,10,0)
                        if verificar == True:
                            parar = input("¿Desea agregar otra personalidad? \nResponda 'n' para parar, o cualquier otra tecla para continuar: ")
                            personalidad.append(tipo)
                            
                        #for i in personalidad:
                            #addPersonalidad(nombre, perso[i])
                        
                #Agregar lo que valora en una amistad 
                valor = ["\n0. Confianza", "1. Lealtad","2. Honestidad","3. Apoyo mutuo","4. Humildad","5. Solidaridad","6. Compañerismo","7. Tolerancia \n"]
                valores = ["Confianza","Lealtad","Honestidad","Apoyo mutuo","Humildad","Solidaridad","Compañerismo","Tolerancia"]
                for i in valor:
                    print(i)
                amis = []
                no = " "
                while no != "n": 
                    amistad = input("¿Qué valora de la amistad? \nIngrese la opción que considere importante: ")
                    validar = verificarNum(amistad)
                    while validar == False:
                        print("Lo sentimos,el valor ingresado no es un número.")
                        amistad = input("¿Qué valora de la amistad? \nIngrese las opciones que considere importantes: ")
                        validar = verificarNum(amistad)
                    if validar == True:
                        amistad = int(amistad)
                        verificar = opcion_rango(amistad,7,0)
                        while verificar == False:
                            print("El dato ingresado es invalido.")
                            amistad = input("¿Qué valora de la amistad? \nIngrese las opciones que considere importantes: ")
                            amistad = int(amistad)
                            verificar = opcion_rango(amistad,7,0)
                        if verificar == True:
                            no = input("¿Desea agregar otro valor para amistad? \nResponda 'n' para parar, o cualquier otra tecla para continuar: ")
                            amis.append(amistad)
                        #for i in amis:
                            #addAmistad(nombre, valores[i])
                    
                        #Agregar sus generos musicales preferidos
                generos = ["\n0. Disco", "1. Reggaeton", "2. Salsa","3. Pop","4. Rock","5. Electrónica","6. Rap","7. Trap","8. Hip-Hop","9. Cristiana","10. Jazz","11. Metal","12. Cumbia", "13. Merengue \n"]
                generosM = ["Disco", "Reggaeton", "Salsa","Pop","Rock","Electrónica","Rap","Trap","Hip-Hop","Cristiana","Jazz","Metal","Cumbia","Merengue"]
                for i in generos:
                    print(i)
                music = []
                mas = " "
                while mas != "n":
                    musica = input("Ingrese su género musical favorito: ")
                    validar = verificarNum(musica)
                    while validar == False:
                        print("Lo sentimos, el valor ingresado no es un número.")
                        musica = input("Ingrese su género musical favorito: ")
                        validar = verificarNum(musica)
                    if validar == True:
                        musica = int(musica)
                        verificar = opcion_rango(musica,13,0)
                        while verificar == False:
                            print("El dato ingresado es invalido.")
                            musica = input("Ingrese su género musical favorito: ")
                            musica = int(musica)
                            verificar = opcion_rango(musica,13,0)
                        if verificar == True:
                            mas = input("¿Desea agregar otro género musical? \nResponda 'n' para parar, o cualquier otra tecla para continuar.")                        
                            music.append(musica)
                        #for i in music:
                            #addMusica(nombre,generos[i])

                a= ["\n0. Practicar deporte","1. Ver películas o series","2. Salir a comer","3. Visitar familiares o amigos","4. Ir a una fiesta","5. Cocinar","6. Bailar","7. Escuchar música","8. Jugar videojuegos","9. Leer","10. Voluntariado","11. Pintar o dibujar","12. Componer música","13. Ordenar mi cuarto","14. Aprender algo nuevo","15. Recurrir a redes sociales","16. Dormir","17. Manualidades \n"]
                tLibre= ["Practicar deporte","Ver películas o series","Salir a comer","Visitar familiares o amigos","Ir a una fiesta","Cocinar","Bailar","Escuchar música","Jugar videojuegos","Leer","Voluntariado","Pintar o dibujar","Componer música","Ordenar mi cuarto","Aprender algo nuevo","Recurrir a redes sociales","Dormir","Manualidades"]
                for i in a:
                    print(i)
                libre = []
                agregar = " "
                while agregar != "n":
                    actividad = input("¿Qué actividades realiza en su tiempo libre?")
                    validar = verificarNum(actividad)
                    while validar == False:
                        print("Lo sentimos, el valor ingresado no es un número.")
                        actividad = input("¿Qué actividades realiza en su tiempo libre?")
                        validar = verificarNum(actividad)
                    if validar == True:
                        actividad = int(actividad)
                        verificar = opcion_rango(actividad,0,17)
                        while verificar == False:
                            print("El dato ingresado es invalido.")
                            actividad = input("¿Qué actividades realiza en su tiempo libre?")
                            actividad = int(actividad)
                            verificar = opcion_rango(actividad,0,17)
                        if verificar == True:
                            agregar = input("¿Desea agregar otra actividad? \nResponda 'n' para parar, o cualquier otra tecla para continuar.")                        
                            libre.append(actividad)
                        #for i in libre:
                            #addActividad(nombre,tLibre[i])

            #Recomendar personas ingresando un nombre
            elif opcion == 2:
                print("---------------     2. REALIZAR UNA RECOMENDACION POR MEDIO DE NUESTRO ALGORITMO.     ----------")
                nombre=input("Ingrese un nombre completo")
                amigos=algoritmo(nombre, getPersonas(), getCorreos())
                print("Se encontraron: "+str(len(amigos[0]))+" posibles amigos para ti")
                for f in range(0, len(amigos[0])):
                    print("\n")
                    print("*Nombre: "+amigos[0][f]+"\t Correo: "+amigos[2][f])
                    print("   Cosas en comun con esta persona:")
                    for d in amigos[1][f]:
                        print("\t-"+d)
                
else:
    print("\nGracias por visitar nuestro sistema de recomendaciones.")
