from pokebook.models.abstract_model import AbstractModel
from pokebook.models.sprites import Sprites
from pokebook.utils.constants import apiconst, pokconst


class Pokemon(AbstractModel):
    """
    Contiene la información de un pokemon. 

    Todos los datos de un pokemon deben relacionarse y cumplir las caracterísitcas de la pokeapi. 
    
    Solo __id y __name son escenciales para poder identificar a un pokemon, de hecho el operador _eq__() utiliza 
    estas propiedades para comparar dos objetos de tipo Pokemon.

    Propiedades:
        
        sprites   - Sprites del pokemon con los que cuenta la pokeapi.
    """
    def __init__(self, id:int, name = '', url  = ''):
        """
        Genera el modelo con los datos mínimos de un pokemon. Es necesario un id de tipo entero para poder obtener un 
        objeto de tipo Pokemon.

        Parámetros:

            id   - Es el número con el que se identifica al pokemon, este debe ser un número entero.
            name - Nombre con el que se identifica al pokemon.
            url  - URL con la que se puede recuparar al pokemon desde la pokeapi.
        """
        self.id = id
        self.name = name
        self.abilities = None
        self.moves = None
        self.sprites = None
        self.types = None
        self.url = url


    def __eq__(self, right):
        """        
        Retorna: True si __id y __name son iguales, de lo contrario False.
        """
        return self.id == right.id and self.name == right.name


    def __str__(self):
        return f'Pokemon(id:{self.id}, name:{self.name})'


    @property
    def id(self):
        """        
        Número con el que se identifica al pokemon en la pokeapi, este es guardado como un str con formato de 4 
        dígitos, por lo que los números con menos de 4 dígitos se rellena con ceros a la izquierda. Este número siempre 
        debe ser mayor o igual que 0, en caso de ser 0 se debe considerar como un valor indefinido.

        Puede usarse un str, siempre y cuando este sea un número. Se recomienda usar un valor int para tener 
        consitencia con el código.

        Un valor None será tomado como un valor cero (indefinido).
        """
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = str(id) if id else '0' 
        if not self.__id.isnumeric():
            raise(ValueError('El valor del id debe ser un número mayor o igual a 0.'))
        elif int(self.__id) < 0:
            raise(ValueError('El valor del id debe ser mayor o igual a 0.'))
        else:
            self.__id = self.__id.zfill(pokconst.ID_FILL)


    @property
    def name(self):
        """
        Nombre del pokemon, este se guarda en minúsculas y en caso de ser un valor None se guarda como una cadena 
        vacía.
        """
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name.strip().lower() if name else ''

    @property
    def abilities(self):
        """
        Un pokemon tiene una o varias habilidades.

        Los habilidades se guardan como una lista, en caso de darle un valor None se guarda como una lista vacía.
        """
        return self.__abilities

    @abilities.setter
    def abilities(self, abilities:list):
        self.__abilities = abilities if abilities else []   

    @property
    def moves(self):
        """
        Todos los movimientos con los que puede contar un pokemon. 

        Los movimientos se guardan como una lista, en caso de darle un valor None se guarda como una lista vacía.
        """
        return self.__moves

    @moves.setter
    def moves(self, moves:list):
        self.__moves = moves if moves else []

    @property
    def types(self):
        """
        Tipos a los que pertenece el pokemon.

        Los tipos se guardan como una lista, en caso de darle un valor None se guarda como una lista vacía.
        """
        return self.__types

    @types.setter
    def types(self, types:list):
        self.__types = types if types else []