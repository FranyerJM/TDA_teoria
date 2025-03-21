class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def eliminar(self, dato):
        if not self.cabeza:
            return
        
        actual = self.cabeza
        anterior = None

        while True:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    # Eliminar el nodo cabeza
                    if actual.siguiente == self.cabeza:
                        self.cabeza = None
                    else:
                        ultimo = self.cabeza
                        while ultimo.siguiente != self.cabeza:
                            ultimo = ultimo.siguiente
                        self.cabeza = actual.siguiente
                        ultimo.siguiente = self.cabeza
                return
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def recorrer(self):
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=' ')
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print()

# Ejemplo de uso
lista = ListaCircular()
lista.insertar_al_final(10)
lista.insertar_al_final(20)
lista.insertar_al_final(30)

print("Lista circular después de inserciones al final:")
lista.recorrer()

lista.insertar_al_inicio(5)
print("Lista circular después de insertar 5 al inicio:")
lista.recorrer()

lista.eliminar(20)
print("Lista circular después de eliminar 20:")
lista.recorrer()

lista.eliminar(10)
print("Lista circular después de eliminar 10:")
lista.recorrer()
