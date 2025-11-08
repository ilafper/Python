#6. Manejo de Archivos:


# abrir el archivo txt, (solo lectura) con la "r" y luego imprimir el contenido
with open("empleados.txt", "r") as archivoEmpleados:
    contenido = archivoEmpleados.read()
    print(contenido)

print("---------------------------------------------------")
print("---------------archivo csv--------------------")



# ahora el archivo CSV, creo un archivo llamado archivoCSV.csv
import csv

#LISTA EN DONDE IRAN LOS DATOS DEL ARCHVIO
listaProducCSV=[]

# Abrimos el archivo CSV
with open("archivoCSV.csv", "r", encoding="utf-8") as archivoCSV:
    lectorCSV = csv.reader(archivoCSV)
    
    next(lectorCSV)  # Saltar la fila de encabezados

    # Recorremos cada fila
    for fila in lectorCSV:
        
        producto = {
            "nombre": fila[0],
            "precio": float(fila[1]),
            "cantidad": int(fila[2])
        }
        listaProducCSV.append(producto)

# Mostrar los datos cargados
print("Productos leídos desde CSV:\n")
for cada_dato in listaProducCSV:
    total = cada_dato["precio"] * cada_dato["cantidad"]
    print(f"{cada_dato['nombre']} - Precio: {cada_dato['precio']} - Cantidad: {cada_dato['cantidad']} ")
        
    
    
    