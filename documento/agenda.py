# Abrimos el archivo en modo de escritura
with open("agenda.txt", "w") as agenda_file:
    print("Ingresa tus citas o tareas. Escribe 'salir' para terminar.")
    
    while True:
        entry = input("> ")
        if entry.lower() == "salir":
            break
        
        # Escribimos la entrada en el archivo, seguida de un salto de línea
        agenda_file.write(entry + "\n")

print("Se han guardado tus entradas en agenda.txt")

try:
    # Abrimos el archivo en modo de lectura
    with open("agenda.txt", "r") as agenda_file:
        print("\n--- Tus entradas de la agenda ---")
        # Leemos todas las líneas del archivo y las imprimimos
        content = agenda_file.read()
        print(content)

except FileNotFoundError:
    print("El archivo agenda.txt no se encontró. ¡Primero crea tu agenda!")

def agregar_entrada():
    """ Agrega una nueva entrada a la agenda. """
    # Abrimos en modo de adición ('a') para no sobrescribir el contenido existente
    with open("agenda.txt", "a") as agenda_file:
        entry = input("Ingresa tu nueva cita o tarea: ")
        agenda_file.write(entry + "\n")
    print("Entrada guardada.")

def ver_agenda():
    """Muestra todas las entradas de la agenda."""
    try:
        with open("agenda.txt", "r") as agenda_file:
            print("\n--- Tu agenda ---")
            print(agenda_file.read())
    except FileNotFoundError:
        print("Aún no tienes entradas en tu agenda.")

def main():
    """Función principal del programa."""
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Agregar nueva entrada")
        print("2. Ver agenda")
        print("3. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == '1':
            agregar_entrada()
        elif choice == '2':
            ver_agenda()
        elif choice == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()