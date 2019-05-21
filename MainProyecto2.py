#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Proyecto #2 de Algoritmos y Estructuras de Datos
#Recomendacion de Amigos
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

#from Proyecto2 import *

print("----------   ¡Bienvenidos a MeetMe!   ----------")

menu = ("Estas son las opciones que puede realizar:" +
        "\n1. Agregar una persona a la base de datos." +
        "\n2. Ingresar un nombre para conocer personas con los mismos gustos." +
        "\n3. Salir.")

opcion = 0

while opcion != 5:
    print(menu)
    opcion = input("Ingrese una opcion: ")
    if opcion==1:
        nombre = input("Ingrese su nombre completo: ")
        addPersona(nombre)
        personalidad = []
        tipos = ["1. Pacificador", "2. Reformador", "3.Triunfador", "4. Ayudador", "5. Romántico", "6. Investigador", "7. Leal", "8. Entusiasta", "9. Desafiador", "10. Extrovertido", "11. Introvertido", "12. Ninguna de las anteriores"]
        for i in tipos:
            print(i)
            
        addPersonalidad(nombre,personalidad)
        amimstad = input("¿Qué valora de la amistad?")
        musica = input("¿Cuáles son sus géneros musicales faovritos?")
        ocupacion = input("Ingrese 0 si estudia, ingrese 1 si trabaja o ingrese 3 si ambas: ")
        actividad = input("¿Qué actividades realiza en su tiempo libre?")
        
    else:
        print("La opcion no es valida.\n")
        print(menu)
        opcion = input("Ingrese una opcion: ")
