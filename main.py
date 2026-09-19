import agregar
import mostrar
import eliminar


mis_tareas = []


while True:
    print("\n--- BIENVENIDO AL GESTOR DE TAREAS ---")
    print("Menu de Opciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opcion (1/2/3/4): ")

    if opcion == "1":
        mostrar.mostrar_tareas(mis_tareas)

    elif opcion == "2":
        nueva_tarea = input("Escribe la nueva tarea: ")
        agregar.agregar_tarea(mis_tareas, nueva_tarea)

    elif opcion == "3":
        mostrar.mostrar_tareas(mis_tareas)

        if mis_tareas:
            try:
                indice = int(input("Escribe el numero de la tarea a eliminar: "))
                eliminar.eliminar_tarea(mis_tareas, indice)
            except ValueError:
                print("Debes ingresar un numero.")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opcion no valida. Intenta nuevamente.")