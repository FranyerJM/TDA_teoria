class NodoDoble:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class IPhone:
    def __init__(self, modelo, capacidad, precio, bateria):
        self.modelo = modelo
        self.capacidad = capacidad
        self.precio = precio
        self.bateria = bateria  # Porcentaje de salud de batería
    
    def __str__(self):
        return f"{self.modelo} {self.capacidad}GB - ${self.precio} ({self.bateria}% batería)"

class ListaDobleTelefonos:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def agregar(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.longitud += 1

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

    def buscar_por_precio(self, max_precio):
        resultados = []
        actual = self.cabeza
        while actual:
            if actual.valor.precio <= max_precio:
                resultados.append(actual.valor)
            actual = actual.siguiente
        return resultados
    
    def eliminar_por_modelo(self, modelo):
        actual = self.cabeza
        while actual:
            if actual.valor.modelo == modelo:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False

# Creacióon de 5 iPhones usados
iphones = ListaDobleTelefonos()
iphones.agregar(IPhone("13 Pro", 128, 380, 88))
iphones.agregar(IPhone("14", 256, 390, 90))
iphones.agregar(IPhone("12 Mini", 64, 300, 85))
iphones.agregar(IPhone("15 Pro Max", 512, 850, 95))
iphones.agregar(IPhone("SE 2022", 128, 250, 92))

print("=== Lista completa de iPhones ===")
iphones.mostrar()

print("\n=== Busqueda por precio (max $350) ===")
for telefono in iphones.buscar_por_precio(350):
    print(f"- {telefono}")

# Operacion de insercion en medio de la lista
nuevo_iphone = IPhone("Xr", 64, 200, 80)
iphones.agregar(nuevo_iphone)

print("\n=== Despues de agregar iPhone XR ===")
iphones.mostrar()

# Eliminar un elemento específico
def eliminar_por_modelo(lista, modelo):
    actual = lista.cabeza
    while actual:
        if actual.valor.modelo == modelo:
            if actual.anterior:
                actual.anterior.siguiente = actual.siguiente
            else:
                lista.cabeza = actual.siguiente
            
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            else:
                lista.cola = actual.anterior
            
            lista.longitud -= 1
            return True
        actual = actual.siguiente
    return False

iphones.eliminar_por_modelo("12 Mini")
print("\n=== Despues de eliminar iPhone 12 Mini ===")
iphones.mostrar()
