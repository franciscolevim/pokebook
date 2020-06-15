class PoekapiConstants:
    """
    Constantes para utilizar parámetros requeridos por las urls de la pokeapi.
    """
    def __init__(self):
        self.__ID = 'id'
        self.__NAME = 'name'
        self.__ABILITIES = 'abilities'
        self.__MOVES = 'moves'
        self.__SPRITES = 'sprites'        
        self.__TYPES = 'types'


    @property
    def ID(self):
        """
        Número con el que se identifica a un pokemon en la pokeapi.
        """
        return self.__ID

    @property
    def NAME(self):
        """
        Nombre del pokemon.
        """
        return self.__NAME

    @property
    def ABILITIES(self):
        """
        Habilidades que puede tener un pokemon.
        """
        return self.__ABILITIES

    @property
    def MOVES(self):
        """
        Movimientos que puede tener un pokemon.
        """
        return self.__MOVES

    @property
    def SPRITES(self):
        """
        Sprites del pokemon en la pokeapi.
        """
        return self.__SPRITES

    @property
    def TYPES(self):
        """
        Tipos del pokemon.
        """
        return self.__TYPES


class PokemonConstants:
    """
    Constantes para dar formato a los datos de un pokemon.
    """
    def __init__(self):
        self.__ID_FILL = 4
        self.__ID_FORMAT = '0000'        


    @property
    def ID_FORMAT(self):
        """
        Formato del id del pokemon: 0000.
        """
        return self.__ID_FORMAT

    @property
    def ID_FILL(self):
        """
        Cantidad de ceros necesarios para completar los dígitos del formato del id del pokemon.
        """
        return self.__ID_FILL


apiconst = PoekapiConstants()
pokconst = PokemonConstants()