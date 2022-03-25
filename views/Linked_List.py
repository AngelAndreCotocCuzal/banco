from typing import Optional, TypeVar, Generic
from node import Node

T = TypeVar('T')


# Crea una lista que solo permita nodos de un tipo de dato (genérico)
class LinkedList(Generic[T]):
    def _init_(self):
        self.head = None
        self.tail = None
        self.size: int = 0

    # Método que utiliza la función len() de python para determinar el número de elementos en la estructura
    def _len_(self) -> int:
        return self.size

    # Atributo de lectura para acceder a la data del primer nodo
    # Si no hay elementos lanza una excepción
    @property
    def first(self) -> T:
        if self.is_empty():
            raise Exception('Linked List is empty')
        else:
            return self.head.data

    # Atributo de lectura para acceder a la data del último nodo
    # Si no hay elementos lanza una excepción
    @property
    def last(self) -> T:
        if self.is_empty():
            raise Exception('Linked List is empty')
        else:
            return self.tail.data

    # Método que verifica si la lista enlazada se encuentra vacía (no hay nodos)
    def is_empty(self):
        return self.head is None and self.tail is None

    # Método para recorrer todos los nodos de una lista, devuelve una cadena con toda la data
    def traversal(self) -> str:
        result: str = ''
        current: Optional[Node] = self.head
        while current is not None:
            if current == self.tail:
                result += str(current)
            else:
                result += str(current) + '->'
            current = current.next
        return result

    def prepend(self, numero):
        nuevo = Node(numero)
        if self.is_empty():
            self.head = nuevo
            self.tail = nuevo
        else:
            current = self.head
            self.head = nuevo
            nuevo.next = current
        self.size += 1

    def postpend(self, numero):
        nuevo = Node(numero)
        if self.is_empty():
            self.head = nuevo
            self.tail = nuevo
        else:
            current = self.tail
            self.tail = nuevo
            current.next = nuevo
        self.size += 1

    def prepend_before(self, referencia, numero):
        nuevo = Node(numero)
        current = self.search_node_value(referencia)
        if current.data == self.head.data:
            self.prepend(numero)
        else:
            # Posicionar el puntero anterior
            # Obtener la posición de la referencia
            posicion = self.search_position_node(referencia)
            anterior = self.search_node_position(posicion - 1)

            # Enlazar los nodos
            anterior.next = nuevo
            nuevo.next = current

            # Enlazar los nodos
            anterior.next = nuevo
            nuevo.next = current

    def postpend_after(self, numero, referencia):
        nuevo = Node(numero)
        current = self.search_node_value(referencia)
        if current.data == self.tail.data:
            self.postpend(numero)
        else:
            # Posicionar el puntero anterior
            # Obtener la posición de la referencia
            posicion = self.search_position_node(referencia)
            posterior = self.search_node_position(posicion + 1)

            # Enlazar los nodos
            current.next = nuevo
            nuevo.next = posterior

    # Métodos de busqueda
    def search_node_value(self, valor):
        current = self.head
        while current is not None:
            # ¿Es Ruben igual a aux.nombre?
            if valor == current.data:
                return current
            else:
                current = current.next
        raise Exception('EL ELEMENTO NO EXISTE')

    def search_node_position(self, posicion):
        iteraciones = 0
        current = self.head
        while current is not None:
            # ¿Es posicion igual a iteraciones?
            if posicion == iteraciones:
                return current
            else:
                iteraciones += 1
                current = current.next
        raise Exception('EL ELEMENTO NO EXISTE')

    def search_position_node(self, referencia):
        current = self.head
        iteraciones = 0
        while current is not None:
            # ¿Es aux.nombre igual a referencia?
            if current.data == referencia:
                return iteraciones
            else:
                current = current.next
                iteraciones += 1
        raise Exception('La referencia no existe')

    # Métodos para eliminar

    def delite_start(self):
        if self.is_empty() is True:
            raise Exception('Subdesbordamiento de lista')
        elif self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1
            return current

    def delete_end(self):
        if self.is_empty() is True:
            raise Exception('Subdesbordamiento de lista')
        elif self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current
        else:
            current = self.tail
            posicion = self.search_position_node(current.data)
            anterior = self.search_node_position(posicion - 1)
            self.tail = anterior
            anterior.next = None
            self.size -= 1
            return current

    def remove(self, referencia):
        # La referencia no existe
        # La lista esta vacia
        current = self.search_node_value(referencia)
        # solo hay un elemento en la lista
        # la referencia es el frente
        if self.head == current:
            return self.delite_start()

        # La referencia es el fondo
        elif self.tail == current:
            return self.delete_end()
        else:
            # l referencia esta en otra posicion
            posicion = self.search_position_node(referencia)
            anterior = self.search_node_position(posicion - 1)
            posterior = self.search_node_position(posicion + 1)
            anterior.next = posterior
            current.next = None
            self.size -= 1
            return current

    def remove_previous_reference(self, referencia):
        # OBTENER VALORES
        current = self.search_node_value(referencia)

        if current != self.head:
            posicion = self.search_position_node(referencia)  # 2
            anterior = self.search_node_position(posicion - 1)  # 2-1 = 1

            if anterior == self.head:
                return self.delite_start()
            else:
                anterior_2 = self.search_node_position(posicion - 2)

                # RECONSTRUIR ENLACES
                anterior_2.next = current
                anterior.next = None
                self.size -= 1
                return anterior
        else:
            raise Exception('El elemento no exite')

    def remove_later_reference(self, referencia):
        current = self.search_node_value(referencia)
        if current == self.tail:
            raise Exception('El elemento no existe')
        else:
            posicion = self.search_position_node(referencia)
            posterior = self.search_node_position(posicion + 1)
            if posterior == self.tail:
                return self.delete_end()
            else:
                current.next = posterior.next
                posterior.next = None
                self.size -= 1
                return posterior