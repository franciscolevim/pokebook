class PokeapiUrls:
    """
    Contiene todas las urls y end-points de la pokeapi.
    """
    def __init__(self):
        """
        """
        self.__POKEAPI_URL = 'https://pokeapi.co/api/v2'
        self.__POKEMON_END_POINT = 'pokemon'
        self.__LIMIT_ARG = 'limit'
        self.__OFFSET_ARG = 'offset'


    @property
    def POKEAPI_URL(self):
        """
        URL de la pokeapi.
        """
        return self.__POKEAPI_URL

    @property
    def POKEMON_URL(self):
        """
        URL para obtener los datos de un pokemon.
        """
        return f'{self.__POKEAPI_URL}/{self.__POKEMON_END_POINT}'

    @property
    def LIMIT_ARG(self):
        """
        Define el límite de resultados que se necesitan de una lista de datos.
        """
        return self.__LIMIT_ARG

    @property
    def OFFSET_ARG(self):
        """
        Define a partir de que elemento se presentarán la lista de datos solicitada.
        """
        return self.__OFFSET_ARG



apiurl = PokeapiUrls()