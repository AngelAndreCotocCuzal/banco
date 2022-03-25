import random
from typing import Optional, TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, correo: str, password: str, puesto: str, nombre: str, estado: bool):
        self.nombre: Optional[str] = None
        self.correo: Optional[str] = None
        self.codigo: Optional[int] = None
        self.password: Optional[str] = None
        self.puesto: Optional[str] = None
        self.estado: bool = False
        self.next: Optional[Node] = None

    def get_codigo(self):
        self.codigo = random.randint(0, 1000)

