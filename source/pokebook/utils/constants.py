class PoekapiConstants:
    """
    Constantes para utilizar parámetros requeridos por las urls de la pokeapi.
    """
    def __init__(self):
        self.__ID = 'id'
        self.__NAME = 'name'
        self.__ABILITIES = 'abilities'
        self.__ABILITY = 'ability'
        self.__MOVES = 'moves'
        self.__MOVE = 'move'
        self.__SPRITES = 'sprites'        
        self.__TYPES = 'types'
        self.__TYPE = 'type'


        self.__BACK_DEFAULT = 'back_default'
        self.__BACK_FEMALE = 'back_female'
        self.__BACK_SHINY = 'back_shiny'
        self.__BACK_SHINY_FEMALE = 'back_shiny_female'
        self.__FRONT_DEFAULT = 'front_default'
        self.__FRONT_FEMALE = 'front_female'
        self.__FRONT_SHINY = 'front_shiny'
        self.__FRONT_SHINY_FEMALE = 'front_shiny_female'

        self.__RESULTS = 'results'
        self.__URL = 'url'


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
    def ABILITY(self):
        """
        Habilidad de un pokemon.
        """
        return self.__ABILITY

    @property
    def MOVES(self):
        """
        Movimientos que puede tener un pokemon.
        """
        return self.__MOVES

    @property
    def MOVE(self):
        """
        Movimiento que puede tener un pokemon.
        """
        return self.__MOVE

    @property
    def SPRITES(self):
        """
        Sprites de los pokemones en la pokeapi.
        """
        return self.__SPRITES

    @property
    def TYPES(self):
        """
        Tipos de pokemon.
        """
        return self.__TYPES

    @property
    def TYPE(self):
        """
        Tipo de pokemon.
        """
        return self.__TYPE


    @property
    def BACK_DEFAULT(self):
        return self.__BACK_DEFAULT

    @property
    def BACK_FEMALE(self):
        return self.__BACK_FEMALE

    @property
    def BACK_SHINY(self):
        return self.__BACK_SHINY

    @property
    def BACK_SHINY_FEMALE(self):
        return self.__BACK_SHINY_FEMALE

    @property
    def FRONT_DEFAULT(self):
        return self.__FRONT_DEFAULT

    @property
    def FRONT_FEMALE(self):
        return self.__FRONT_FEMALE

    @property
    def FRONT_SHINY(self):
        return self.__FRONT_SHINY

    @property
    def FRONT_SHINY_FEMALE(self):
        return self.__FRONT_SHINY_FEMALE

    @property
    def RESULTS(self):
        """
        Resultado de peticiones a la poekapi.
        """
        return self.__RESULTS

    @property
    def URL(self):
        """
        URL del pokemon dentro de la pokeapi.
        """
        return self.__URL


class PokemonConstants:
    """
    Constantes para dar formato a los datos de un pokemon.
    """
    def __init__(self):
        self.__ID_FILL = 4      


    @property
    def ID_FILL(self):
        """
        Cantidad de ceros necesarios para completar los dígitos del formato del id del pokemon.
        """
        return self.__ID_FILL


apiconst = PoekapiConstants()
pokconst = PokemonConstants()