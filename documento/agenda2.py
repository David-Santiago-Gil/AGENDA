def guardar_contactos_iniciales():
    """Guarda los contactos de la imagen en el archivo agenda.txt."""
    contactos = [
{"CC","1001202162","JOAN SEBASTIAN BORDA CASTIBLANCO","3105885793","johansebastianborda@gmail.com"},
{"CC","1015397949","DAVID ALEJANDRO	APARICIO ROMERO","3204308710","davidaar05@gmail.com"},
{"CC","1016009825","MIGEL ESTEBAN	MARTINEZ VARON","3219404978","miguelmartinezvaron32143@gmail.com"},
{"CC","1019989868","STEBAN	CARRIZOSA ORTEGON","3006898362","carrizosaortegon.steban@gmail.com"},
{"CC","1028481891","DAVID SANTIAGO	CAMELO CRUZ","3193866413","dilanbcm@gmail.com"},
{"CC","1029520748","JOSEPH NICOLAS	TORRES CASTELBLANCO","3122224003","josephnicolastorres6@gmail.com"},
{"CC","1047041996","ANDRES CAMILO	GUARDIA ALTAMAR","3017852867","chamolocoporsiempre@gmail.com"},
{"CC	1070384473	NATALIA	AVILAN LAROTTA	3105281043	nataliaavilan24@gmail.com"},
{"CC	1141114537	OSCAR FELIPE	GUACANEME SANCHEZ	3125056545	guacanemeoscarfelipe@gmail.com"},
{"CC	1142714477	DANNA VALENTINA	DIAZ GUALDRON	3229150145	dannadiazgualdron@gmail.com"},
{"CC	1193552312	DIEGO ALEJANDRO	SANCHEZ LOPEZ	3026826919	hiphopclan99@gmail.com"},
{"CC	80154727	MARIO DAVIS	AGUILLON PUENTES	3188676690	aguillondavis@gmail.com"},
{"TI	1013117356	JULIAN ANDRES	MONROY MELO	3112237515	julianjamm321123@gmail.com"},
{"TI	1028486643	SAMUEL ANDRES	PINZON MONROY	3203985749	yosoyanel02@gmail.com"},
{"TI	1071914553	JHOJAN STIVEN	SILVA GARCIA	3115867655	jhojansilva0302@gmail.com"},
{"TI	1072746935	JOHAN SEBASTIAN	RODRIGUEZ GONZALEZ	3053039737	johansebastian201107@gmail.com"},
{"CC	1001329164	MISCHAELL ANDRES 	PULIDO SALDAÑA	3227336328	katerinaguilar12345@gmail.com"},
{"CC	80166347	ERWIN	JOYA PULIDO	3196479318	ejoya7@soy.sena.edu.com"},
{"CC  1013117179  DAVID SANTIAGO GIL CIFUENTES 3133568187 gilsantiagodepa@gmail.com"}
    ]
    try:
        with open("agenda.txt", "w", encoding="utf-8") as agenda_file:
            for contacto in contactos:
                agenda_file.write(contacto + "\n")
        print("Agenda inicial guardada.")
    except Exception as e:
        print(f"Ocurrió un error al guardar la agenda: {e}")

def buscar_contacto():
    """Busca y muestra un contacto por número de teléfono."""
    try:
        telefono_buscar = input("Ingresa el número de teléfono que quieres buscar: ")
        with open("agenda.txt", "r", encoding="utf-8") as agenda_file:
            encontrado = False
            print("\n--- Resultados de la búsqueda ---")
            for linea in agenda_file:
                if telefono_buscar in linea:
                    print(linea.strip())
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró un contacto con el número '{telefono_buscar}'.")
    except FileNotFoundError:
        print("El archivo agenda.txt no se encontró.")

def modificar_contacto():
    """Modifica un contacto existente por su número de teléfono."""
    try:
        telefono_modificar = input("Ingresa el número del contacto que quieres modificar: ")
        with open("agenda.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
        
        encontrado = False
        nueva_linea = ""
        with open("agenda.txt", "w", encoding="utf-8") as file:
            for linea in lineas:
                if telefono_modificar in linea:
                    print(f"Contacto encontrado: {linea.strip()}")
                    nuevo_nombre = input("Ingresa el nuevo nombre completo: ")
                    nuevo_telefono = input("Ingresa el nuevo número de teléfono: ")
                    nueva_direccion = input("Ingresa la nueva dirección (o dejar en blanco): ")
                    nuevo_correo = input("Ingresa el nuevo correo electrónico (o dejar en blanco): ")
                    
                    nueva_linea = f"{nuevo_nombre}: Tel: {nuevo_telefono}"
                    if nueva_direccion:
                        nueva_linea += f", Dir: {nueva_direccion}"
                    if nuevo_correo:
                        nueva_linea += f", Correo: {nuevo_correo}"
                    
                    file.write(nueva_linea + "\n")
                    encontrado = True
                else:
                    file.write(linea)
        
        if encontrado:
            print("El contacto ha sido modificado exitosamente.")
        else:
            print(f"No se encontró un contacto con el número '{telefono_modificar}'.")
    
    except FileNotFoundError:
        print("El archivo agenda.txt no se encontró.")
        
def eliminar_contacto():
    """Elimina un contacto por su número de teléfono."""
    try:
        telefono_eliminar = input("Ingresa el número del contacto que quieres eliminar: ")
        with open("agenda.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
        
        encontrado = False
        with open("agenda.txt", "w", encoding="utf-8") as file:
            for linea in lineas:
                if telefono_eliminar not in linea:
                    file.write(linea)
                else:
                    encontrado = True
        
        if encontrado:
            print(f"El contacto con el número '{telefono_eliminar}' ha sido eliminado.")
        else:
            print(f"No se encontró un contacto con el número '{telefono_eliminar}'.")
    
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