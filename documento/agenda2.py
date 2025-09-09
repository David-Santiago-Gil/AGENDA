def guardar_contactos_iniciales():
    """Guarda los contactos iniciales en el archivo agenda.txt."""
    contactos = [
        "Tipo de Documento: CC, Número de Documento: 1001202162, Nombre: JOAN SEBASTIAN, Apellidos: BORDA CASTIBLANCO, Celular: 3105885793, Correo Electrónico: johansebastianborda@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1015397949, Nombre: DAVID ALEJANDRO, Apellidos: APARICIO ROMERO, Celular: 3204308710, Correo Electrónico: davidaar05@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1016009825, Nombre: MIGEL ESTEBAN, Apellidos: MARTINEZ VARON, Celular: 3219404978, Correo Electrónico: miguelmartinezvaron32143@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1019989868, Nombre: STEBAN, Apellidos: CARRIZOSA ORTEGON, Celular: 3006898362, Correo Electrónico: carrizosaortegon.steban@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1028481891, Nombre: DAVID SANTIAGO, Apellidos: CAMELO CRUZ, Celular: 3193866413, Correo Electrónico: dilanbcm@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1029520748, Nombre: JOSEPH NICOLAS, Apellidos: TORRES CASTELBLANCO, Celular: 3122224003, Correo Electrónico: josephnicolastorres6@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1047041996, Nombre: ANDRES CAMILO, Apellidos: GUARDIA ALTAMAR, Celular: 3017852867, Correo Electrónico: chamolocoporsiempre@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1070384473, Nombre: NATALIA, Apellidos: AVILAN LAROTTA, Celular: 3105281043, Correo Electrónico: nataliaavilan24@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1141114537, Nombre: OSCAR FELIPE, Apellidos: GUACANEME SANCHEZ, Celular: 3125056545, Correo Electrónico: guacanemeoscarfelipe@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1142714477, Nombre: DANNA VALENTINA, Apellidos: DIAZ GUALDRON, Celular: 3229150145, Correo Electrónico: dannadiazgualdron@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1193552312, Nombre: DIEGO ALEJANDRO, Apellidos: SANCHEZ LOPEZ, Celular: 3026826919, Correo Electrónico: hiphopclan99@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 80154727, Nombre: MARIO DAVIS, Apellidos: AGUILLON PUENTES, Celular: 3188676690, Correo Electrónico: aguillondavis@gmail.com",
        "Tipo de Documento: TI, Número de Documento: 1013117356, Nombre: JULIAN ANDRES, Apellidos: MONROY MELO, Celular: 3112237515, Correo Electrónico: julianjamm321123@gmail.com",
        "Tipo de Documento: TI, Número de Documento: 1028486643, Nombre: SAMUEL ANDRES, Apellidos: PINZON MONROY, Celular: 3203985749, Correo Electrónico: yosoyanel02@gmail.com",
        "Tipo de Documento: TI, Número de Documento: 1071914553, Nombre: JHOJAN STIVEN, Apellidos: SILVA GARCIA, Celular: 3115867655, Correo Electrónico: jhojansilva0302@gmail.com",
        "Tipo de Documento: TI, Número de Documento: 1072746935, Nombre: JOHAN SEBASTIAN, Apellidos: RODRIGUEZ GONZALEZ, Celular: 3053039737, Correo Electrónico: johansebastian201107@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 1001329164, Nombre: MISCHAELL ANDRES, Apellidos: PULIDO SALDAÑA, Celular: 3227336328, Correo Electrónico: katerinaguilar12345@gmail.com",
        "Tipo de Documento: CC, Número de Documento: 80166347, Nombre: ERWIN, Apellidos: JOYA PULIDO, Celular: 3196479318, Correo Electrónico: ejoya7@soy.sena.edu.co",
        "Tipo de Documento: CC, Número de Documento: 1013117179, Nombre: DAVID SANTIAGO, Apellidos: GIL CIFUENTES, Celular: 3133568187, Correo Electrónico: gilsantiagodepa@gmail.com"
    ]
    try:
        with open("agenda.txt", "w", encoding="utf-8") as agenda_file:
            for contacto in contactos:
                agenda_file.write(contacto + "\n")
        print("Agenda inicial guardada con los nuevos datos.")
    except Exception as e:
        print(f"Ocurrió un error al guardar la agenda: {e}")

def buscar_contacto():
    """Busca y muestra un contacto por número de documento o celular."""
    try:
        termino_buscar = input("Ingresa el número de documento o celular que quieres buscar: ")
        with open("agenda.txt", "r", encoding="utf-8") as agenda_file:
            encontrado = False
            print("\n--- Resultados de la búsqueda ---")
            for linea in agenda_file:
                if termino_buscar in linea:
                    print(linea.strip())
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró un contacto con el término '{termino_buscar}'.")
    except FileNotFoundError:
        print("El archivo agenda.txt no se encontró.")

def modificar_contacto():
    """Modifica un contacto existente por su número de documento o celular."""
    try:
        termino_modificar = input("Ingresa el número de documento o celular del contacto a modificar: ")
        with open("agenda.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
        
        encontrado = False
        with open("agenda.txt", "w", encoding="utf-8") as file:
            for linea in lineas:
                if termino_modificar in linea:
                    print(f"Contacto encontrado: {linea.strip()}")
                    tipo_doc = input("Ingresa el nuevo Tipo de Documento: ")
                    num_doc = input("Ingresa el nuevo Número de Documento: ")
                    nombre = input("Ingresa el nuevo Nombre: ")
                    apellidos = input("Ingresa los nuevos Apellidos: ")
                    celular = input("Ingresa el nuevo Número de Celular: ")
                    correo = input("Ingresa el nuevo Correo Electrónico: ")
                    
                    nueva_linea = f"Tipo de Documento: {tipo_doc}, Número de Documento: {num_doc}, Nombre: {nombre}, Apellidos: {apellidos}, Celular: {celular}, Correo Electrónico: {correo}"
                    
                    file.write(nueva_linea + "\n")
                    encontrado = True
                else:
                    file.write(linea)
        
        if encontrado:
            print("El contacto ha sido modificado exitosamente.")
        else:
            print(f"No se encontró un contacto con el término '{termino_modificar}'.")
    
    except FileNotFoundError:
        print("El archivo agenda.txt no se encontró.")
        
def eliminar_contacto():
    """Elimina un contacto por su número de documento o celular."""
    try:
        termino_eliminar = input("Ingresa el número de documento o celular del contacto a eliminar: ")
        with open("agenda.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
        
        encontrado = False
        with open("agenda.txt", "w", encoding="utf-8") as file:
            for linea in lineas:
                if termino_eliminar not in linea:
                    file.write(linea)
                else:
                    encontrado = True
        
        if encontrado:
            print(f"El contacto con el término '{termino_eliminar}' ha sido eliminado.")
        else:
            print(f"No se encontró un contacto con el término '{termino_eliminar}'.")
    
    except FileNotFoundError:
        print("El archivo agenda.txt no se encontró.")

def ver_agenda():
    """Muestra todas las entradas de la agenda."""
    try:
        with open("agenda.txt", "r", encoding="utf-8") as agenda_file:
            print("\n--- Tu agenda completa ---")
            print(agenda_file.read())
    except FileNotFoundError:
        print("Aún no tienes entradas en tu agenda.")

def main():
    """Función principal del programa."""
    guardar_contactos_iniciales()
    while True:
        print("\n--- Menú de Agenda ---")
        print("1. Buscar un contacto")
        print("2. Ver toda la agenda")
        print("3. Modificar un contacto")
        print("4. Eliminar un contacto")
        print("Escribe 'salir' para terminar")
        
        choice = input("Elige una opción: ").strip().lower()
        
        if choice == '1':
            buscar_contacto()
        elif choice == '2':
            ver_agenda()
        elif choice == '3':
            modificar_contacto()
        elif choice == '4':
            eliminar_contacto()
        elif choice == 'salir':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()