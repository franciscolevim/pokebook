from pokebook.models.abstract_model import AbstractModel


class Move(AbstractModel):
    """
    Movimiento que puede tener un pokemon.
    """
    def __init__(self, name:str, url = ''):
        self.name = name
        self.url = url

    
    def __str__(self):
        return f'Move(name:{self.name})'


    def __eq__(self, right):
        return self.name == right.name


    @property
    def name(self):
        """
        Nombre del movimiento, este debe ser de tipo str y no puede ser una cadena vacía ni un valor None.
        """
        return self.__name

    @name.setter
    def name(self, name:str):
        if not name or name.strip() == '':
            raise(ValueError('El valor del movimiento no puede ser None ni una cadena en blanco o vacía.'))
        self.__name = name.strip()