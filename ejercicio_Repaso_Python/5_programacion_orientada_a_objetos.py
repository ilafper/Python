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
            raise ValueError("La cantidad a aumentar debe ser positiva")
        self.cantidad += cantidad
        return self.cantidad

    def disminuir_cantidad(self, cantidad):
        """Disminuye la cantidad del producto. No permite dejar cantidad negativa."""
        if cantidad < 0:
            raise ValueError("La cantidad a disminuir debe ser positiva")
        if cantidad > self.cantidad:
            raise ValueError("No se puede disminuir más de la cantidad disponible")
        self.cantidad -= cantidad
        return self.cantidad



# 1. Crear una instancia y llamar a calcular_total
producto1 = Producto("Manzana", 2.5, 10)
print("ProductoPrueba:", producto1.nombre)

#cantiad total
print("Total (precio * cantidad):", producto1.calcular_total())

# 2) Crear una instancia y llamar a aumentar_cantidad

producto2 = Producto("product1", 4, 5)
print("\nAntes aumentar - cantidad:", producto2.cantidad)
print("se aumenta en 3")
producto2.aumentar_cantidad(3)
print("Después aumentar - cantidad:", producto2.cantidad)

# 3) Crear una instancia y llamar a disminuir_cantidad
producto3 = Producto("Plátano", 1.2, 8)
print("\nAntes disminuir - cantidad:", producto3.cantidad)
print("se desminuye en 2")
producto3.disminuir_cantidad(2)
print("Después disminuir - cantidad:", producto3.cantidad)
