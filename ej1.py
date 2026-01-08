#Ejercicio 1: Agenda Telefónica con Validación
#Descripción: Crea un programa que funcione como una agenda de contactos. El programa debe almacenar
#los contactos en un diccionario donde la clave es el nombre y el valor es el número de teléfono.
#Instrucciones:
#1. El programa iniciará con un menú repetitivo (while) con las opciones:
#1. Añadir/Modificar contacto.
#2. Buscar contacto.
#3. Borrar contacto.
#4. Mostrar todos los contactos.
#5. Salir.
#2. Manejo de Excepciones: Al añadir un contacto, el programa debe asegurar que el número de teléfono
#sea un valor numérico entero. Si el usuario introduce letras, debe saltar una excepción
#(ValueError), mostrar un mensaje de error amigable ("Error: El teléfono debe ser un número") y
#volver a pedir el dato sin que el programa se rompa.
#3. Al buscar o borrar, si el nombre no existe en el diccionario, el programa debe informar al usuario
#(puedes hacerlo con if/else o capturando KeyError si intentas acceder directamente)
agenda = {}
while True:
    print("\nAgenda Telefónica")
    print("1. Añadir/Modificar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("introduzca la opción deseada (1-5): ")

    # Añadir/Modificar contacto
    if opcion == '1':
        nombre = input("Introduzca el nombre del contacto: ")
        try:
            telefono = input("Introduzca el número de teléfono: ")
            telefono = int(telefono)
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' con telefono '{telefono}' añadido/modificado con éxito.")
        except ValueError:
            print("Error: El teléfono debe ser un número. Por favor, inténtelo de nuevo.")
    # Buscar contacto
    elif opcion == '2':
        nombre = input("introduce el nombre de usuario a buscar: ")
        if nombre in agenda:
            print(f"El número de teléfono de '{nombre}' es: {agenda.get(nombre)}")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")
    # Borrar contacto
    elif opcion == '3':
        nombre = input("introduce el nombre de usuario a buscar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"El contacto '{nombre}' ha sido borrado.")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")
    # Mostrar todos los contactos
    elif opcion == '4':
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    # Salir
    elif opcion == '5':
        print("Saliendo de la agenda telefónica. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
