archivo=open("mirar.txt","w")
archivo.write("Hoy aprendemos un poco mas")
archivo.close()
print("documento en txt")


archivo=open("bots_bony.txt","w")
archivo.write("que hay de nuevo viejo")
archivo.close()
print("documento en txt")

archivo=open("saber.txt","w")
archivo.write("El poder es conosimiento")
archivo.close()
print("documento en txt")


archivo=open("saber.txt","r")
contenido=archivo.read()
archivo.close()
print("contenido del texto")
print(contenido)

for i in contenido:
    print (i)

archivo=open("asta.txt","a")
archivo.write ("introduccion")
archivo.close()
print("contenido del texto")
print(contenido)

import os

# Crear archivos
archivo=open("mirar.txt","w")
archivo.write("Hoy aprendemos un poco mas")
archivo.close()
print("documento en txt")

archivo=open("bots_bony.txt","w")
archivo.write("que hay de nuevo viejo")
archivo.close()
print("documento en txt")

archivo=open("saber.txt","w")
archivo.write("El poder es conosimiento")
archivo.close()
print("documento en txt")

archivo=open("saber.txt","r")
contenido=archivo.read()
archivo.close()
print("contenido del texto")
print(contenido)

for i in contenido:
    print (i)

archivo=open("asta.txt","a")
archivo.write ("introduccion")
archivo.close()
print("contenido del texto")
print(contenido)

# Funciones para comandos de os
def acciones_os():
    # Eliminar archivo mirar.txt si existe
    if os.path.exists("mirar.txt"):
        try:
            os.remove("mirar.txt")
            print("eliminar archivo")
        except Exception as e:
            print(f"Error al eliminar: {e}")
    else:
        print("mirar.txt no existe, no se elimina")

    # Verificar si existe bots_bony.txt
    if os.path.exists("bots_bony.txt"):
        print("El archivo 'bots_bony.txt' existe")
    else:
        print("El archivo 'bots_bony.txt' no existe")

    # Renombrar saber.txt a Jhojan.txt si existe saber.txt y no existe Jhojan.txt
    if os.path.exists("saber.txt"):
        try:
            os.rename("saber.txt","Jhojan.txt")
            print("renombrar archivo")
        except Exception as e:
            print(f"Error al renombrar: {e}")
    else:
        print("saber.txt no existe, no se puede renombrar")

# Ejecutar las acciones de os
acciones_os()

os.remove("mirar.txt")
print("eliminar archivo")

os.path.exists("bots_bony.txt")
print("El archivo 'bots_bony.txt' existe")


os.rename("saber.txt","Jhojan.txt")
print("renombrar archivo")