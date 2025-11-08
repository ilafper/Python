#EJER1

#Repasar los conceptos fundamentales de Python para preparar a los alumnos en el desarrollo
#de módulos Odoo.

#1. Variables y Tipos de Datos:


#Crea una variable llamada nombre_empresa y asígnale el valor
#"TechSolutions".

nombre_empresa ="TechSolutions"

print(nombre_empresa)

#Crea una variable llamada año_fundacion y asígnale el valor 2010.

año_fundacion=2010

print(año_fundacion)

#Imprime el tipo de dato de ambas variables.

print(type(nombre_empresa))
print(type(año_fundacion))

#-----------------------------------------------------------------------------
print("--------------------------------------------------------------------")

#2. Estructuras de Control:

#Escribe un programa que pida al usuario ingresar un número y determine si es
#positivo, negativo o cero.

numero=-1

if numero> 0:
    print("es positivo")
elif numero<0:
    print("es negativo")
elif numero == 0:
    print("es cero")

#Crea un bucle for que imprima los números del 1 al 10.

for i in range(10):
    print(i+1)
    
    
    
    
#-----------------------------------------------------------------------------
print("--------------------------------------------------------------------")


#3. Funciones

#Define una función llamada calcular_iva que tome como parámetro el precio
numero=100

def funcion_iva(numero):
    operacion=(numero*21)/100
    print("el resultado es: " + str(operacion+numero))

funcion_iva(numero)



#-----------------------------------------------------------------------------
print("--------------------------------------------------------------------")



#4. Listas y Diccionarios:

#Crea una lista llamada empleados con los nombres "Ana", "Carlos", "María" y
#"Luis".

empleados=["ana","carlos", "maria", "luis"]


# Añade un nuevo empleado llamado "Pedro" a la lista.

empleados.append("pedrito")

print(empleados)



#Crea un diccionario llamado info_empleado con las
#claves nombre, edad y departamento, y asígnales valores correspondientes.

dicc_lleno = {"nombre": "yo", "edad": 999999, "departamento": "departamentodejemplo"}


print(dicc_lleno['departamento'])
#-----------------------------------------------------------------------------
print("--------------------------------------------------------------------")




#5. Programación Orientada a Objetos

#Define una clase llamada Producto con los atributos nombre, precio y cantidad.

class Producto:
    
    def __init__(self, nombre,precio,cantidad):
        #valores
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_total(self):
        total = self.precio * self.cantidad
        return total

    def aumentar_cantidad(self, cantidad):
        
        if cantidad < 0:
            raise ValueError("no peude ser negativo")
        self.cantidad += cantidad
        return self.cantidad

    def disminuir_cantidad(self, cantidad):
        
        if cantidad < 0:
            print("no peude ser negativo")
        if cantidad > self.cantidad:
            print("no peude ser mayor que la cantidad actual")
        self.cantidad -= cantidad
        return self.cantidad



# Crear una instancia y llamar a calcular_total
producto1 = Producto("produc1", 2.5, 10)
print("ProductoPrueba:", producto1.nombre)

#cantiad total
print("Total (precio * cantidad):", producto1.calcular_total())

# Crear una instancia y llamar a aumentar_cantidad

producto2 = Producto("product2", 4, 5)
print("\nAntes de aumentar", producto2.cantidad)
print("se aumenta en 3")
producto2.aumentar_cantidad(3)
print("Después aumentar - cantidad:", producto2.cantidad)

# Crear una instancia y llamar a disminuir_cantidad
producto3 = Producto("product3", 16, 8)
print("\nAntes de disminuir", producto3.cantidad)
print("se desminuye en 2")
producto3.disminuir_cantidad(2)
print("Después disminuir - cantidad:", producto3.cantidad)
#-----------------------------------------------------------------------------
print("--------------------------------------------------------------------")





#-----------------------------------------------------------------------------
print("--------------------------------------------------------------------")




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
        
    
    
    

