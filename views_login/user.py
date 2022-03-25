from node import Node


class Asociado:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    # Lista Vacia
    def is_empty(self) -> bool:
        return self._head is None and self._tail is None

    # Se agregarn cuentas, PENDIENTE REVISAR SI ESTA YA UTILIZADO EL CORREO
    def crear_cuenta(self, correo: str, password: str, puesto: str, nombre: str):
        new = Node(correo, password, puesto, nombre, True)
        new.get_codigo()
        while new.codigo == self.search(new.codigo):
            new.get_codigo()

        if self.is_empty():
            self._head = new
            self._tail = new

            self._head.next = self._tail
            self._tail.prev = self._head

        else:
            new.prev = self._tail
            self._tail.next = new
            self._tail = new

        self._size += 1
        return new

    def cambiar_password(self, codigo: int, new_password: str):
        aux = self._head

        while aux is not None:
            if aux.codigo is codigo:
                aux.password = new_password
                return f"La contraseña ha sido actualizada"

            else:
                aux = aux.next

        raise Exception('El numero de usuario no se encontró')

    def deshabilitar(self, codigo: int):
        aux = self._head

        while aux is not None:
            if aux.codigo is codigo:
                aux.estado = False
                return f"El usuario: {aux.nombre} - {aux.codigo} ha sido deshabilitado"

            else:
                aux = aux.next

    raise Exception('El numero de usuario no se encontró')

    def actualizar(self, codigo: int):
        pass

    # Recorrer - Ver usuarios existentes
    def traverse_forward(self) -> str:
        output = ''
        aux = self._head

        while aux is not self._tail:
            output += str(aux.nombre) + " " + str(aux.codigo) + ' -> '
            aux = aux.next

        output += str(self._tail.nombre) + " " + str(aux.codigo)
        return output
