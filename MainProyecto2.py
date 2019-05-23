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

print("----------   ¡Bienvenidos a MeetMe!   ----------")

menu = ("\nEstas son las opciones que puede realizar:" +
        "\n1. Agregar una persona a la base de datos." +
        "\n2. Ingresar un nombre para conocer personas con los mismos gustos." +
        "\n3. Salir.")

opcion = 0

while (opcion != 3):
    print(menu)
    opcion = int(input("\nIngrese una opcion: "))
    if opcion==1:
        #Agrega una nueva persona a la base de datos
        nombre = input("Ingrese su nombre completo: ")
        #addPersona(nombre)

        #Agrega el tipo de personalidad de la persona
        tipos = ["\n0. Pacificador", "1. Reformador", "2. Triunfador", "3. Ayudador", "4. Romántico", "5. Investigador", "6. Leal", "7. Entusiasta", "8. Desafiador", "9. Extrovertido", "10. Introvertido", "11. Ninguna de las anteriores \n"]
        for i in tipos:
            print(i)
        personalidad = []
        parar = " "
        while parar != "n":
            tipos = input("Ingrese el número de opcion que define su personalidad: ")
            validar = verificarNum(tipos)
            while validar == False:
                print("Lo sentimos,el valor ingresado no es un numero.")
                tipos = input("Ingrese el número de opción que define su personalidad: ")
                validar = verificarNum(tipos)
            if validar == True:
                parar = input("¿Desea agregar otra personalidad? \nResponda 'n' para parar, o cualquier otra tecla para continuar: ")
                personalidad.append(tipos)
            #for i in personalidad:
                #addPersonalidad(nombre, i)
                
        #Agregar lo que valora en una amistad 
        else:
            valor = ["\n0. Confianza", "1. Lealtad","2. Honestidad","3. Apoyo mutuo","4. Humildad","5. Solidaridad","6. Compañerismo","7. Tolerancia \n"]
            for i in valor:
                print(i)
            amis = []
            parar = " "
            while parar != "n": 
                amistad = input("¿Qué valora de la amistad? \nIngrese la opción que considere importante: ")
                validar = verificarNum(amistad)
                while validar == False:
                    print("Lo sentimos,el valor ingresado no es un numero.")
                    amistad = input("¿Qué valora de la amistad? \nIngrese las opciones que considere importantes: ")
                    validar = verificarNum(amistad)
                if validar == True:
                    parar = input("¿Desea agregar otro valor para amistad? \nResponda 'n' para parar, o cualquier otra tecla para continuar")

            #Agregar sus generos musicales preferidos
            musica = input("¿Cuáles son sus géneros musicales faovritos?")
            ocupacion = input("Ingrese 0 si estudia, ingrese 1 si trabaja o ingrese 3 si ambas: ")
            actividad = input("¿Qué actividades realiza en su tiempo libre?")
