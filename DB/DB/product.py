class Product:
    def _int_(self, nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

def toDBCollection(self):
    return{
        'nombre':str (self.nombre),
        'precio':float(self.precio),
        'cantidad':int(self.cantidad)
    }