from pokebook.models.abstract_model import AbstractModel
from pokebook.utils.constants import apiconst, pokconst


class Pokemon(AbstractModel):
    """
    Contiene la información de un pokemon. 

    Todos los datos de un pokemon deben relacionarse y cumplir las caracterísitcas de la pokeapi. 
    
    Solo __id y __name son escenciales para poder identificar a un pokemon, de hecho el operador _eq__() utiliza 
    estas propiedades para comparar dos objetos de tipo Pokemon.

    Propiedades:
        
        abilities - Habilidades del pokemon.       
        moves     - Movimientos del pokemon.
        sprites   - Sprites del pokemon con los que cuenta la pokeapi.
        types     - Tipos del pokemon.
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


    def fill(self, json:dict):
        """
        Llena las propiedades del modelo con información de un JSON obtenido de la pokeapi.

        Parámetros:

            json - Contiene la información del pokemon obtenida de la pokeapi como un tipo de diccionario.
        """
        if json:
            self.name = json[apiconst.NAME]
            self.abilities = json[apiconst.ABILITIES]
            self.moves = json[apiconst.MOVES]
            self.sprites = json[apiconst.SPRITES]
            self.types = json[apiconst.TYPES]


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

        Puede usarse un str, siempre y cuando este sea un número. Se recoienda usar un entero para tener consitencia 
        con el código.

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