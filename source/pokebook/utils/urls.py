class PokeapiUrls:
    """
    Contiene todas las urls y end-points de la pokeapi.
    """
    def __init__(self):
        """
        """
        self.__POKEAPI_URL = 'https://pokeapi.co/api/v2'
        self.__POKEMON_END_POINT = 'pokemon'


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



apiurl = PokeapiUrls()