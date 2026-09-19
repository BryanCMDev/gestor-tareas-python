def eliminar_tarea(lista_tareas, indice):
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
        print(f"Tarea eliminada: '{tarea_eliminada}'")
    else:
        print("El indice no existe.")