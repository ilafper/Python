#5. Programación Orientada a Objetos

#Define una clase llamada Producto con los atributos nombre, precio y cantidad.

class Producto:
    
    def __init__(self, nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    #Crea un método llamado calcular_total que devuelva el precio total del
    #producto (precio * cantidad).
    def calcular_total(precio, cantidad):
        total=precio*cantidad
        print("cantidad total "+ str(total))


nuevo_producto2=Producto("hola",10,20)
print(nuevo_producto2.calcular_total(20,10))
