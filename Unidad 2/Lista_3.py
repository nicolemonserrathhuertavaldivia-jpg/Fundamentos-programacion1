#Van a crear una lista vacia con su nombre y van a agregar 5 elementos con imput:(Nombre,preparatoria,lugar de referencia,edad,carrera)
#Se crea una lista llamada lista_datos
lista_datos = []

print(" Lista de mis datos")
#Agregar producto
dato1 = input(" Agregar tu nombre: ")
lista_datos.append(dato1)

#Agregar producto
dato2 = input("Agrega tu preparatoria: ")
lista_datos.append(dato2)

dato3 = input("Agrega tu lugar de referencia: ")
lista_datos.append(dato3)

dato4 = input("Agrega tu edad ")
lista_datos.append(dato4)

dato5 = input("Agrega tu carrera ")
lista_datos.append(dato5)

print("\n📌 Tu lista de datos es:")
for producto in lista_datos:
    print(f"- {datos}")

print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/