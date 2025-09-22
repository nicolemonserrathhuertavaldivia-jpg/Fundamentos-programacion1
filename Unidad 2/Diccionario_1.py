#Declaramos variables
edades = {
    "Brayan": 25,
    "Luis": 30,
    "José": 22,
}
#Imprimimos variables
print("Edad de Brayan:", edades["Brayan"])    
#Mandamos llamar variables
edades["Brayan"] = 28
print("\nDespués de añadir a Pedro:")
print(edades)                               

edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(edades)                              

del edades["José"]
print("\nDespués de eliminar a José:")
print(edades)                               
print("\nRecorriendo el diccionario:")
#Usamos for y print para ordenar variables
for nombre, edad in edades.items():         
     print(f"{nombre} tiene {edad} años")