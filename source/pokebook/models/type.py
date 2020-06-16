from pokebook.models.abstract_model import AbstractModel
from pokebook.utils.constants import apiconst


class Type(AbstractModel):
    """
    Tipo al que puede pertenecer un pokemon.

    Propiedades:
        
        name - Habilidades del pokemon.       
    """
    def __init__(self, name:str, url = ''):
        self.name = name
        self.url = url


    def __str__(self):
        return f'Type(name:{self.name})'


    def __eq__(self, right):
        """
        Un tipo será igual a otro tan solo por su nombre.
        """
        return self.name == right.name


    def fill(self, json:map):
        """
        Parámetros:

            json - Contiene la información del tipo obtenida de la pokeapi como un tipo de diccionario.
        """
        if json:
            self.name = json[apiconst.NAME]


    @property
    def name(self):
        """
        Nombre del tipo, este debe ser de tipo str y no puede ser una cadena vacía ni un valor None.
        """
        return self.__name

    @name.setter
    def name(self, name:str):
        if not name or name.strip() == '':
            raise(ValueError('El valor del nombre no puede se None ni una cadena en blanco o vacía.'))
        self.__name = name.strip()