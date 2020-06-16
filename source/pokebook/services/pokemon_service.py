"""
Servicios para recuperar la información de un pokemón.
"""
import requests
from pokebook.models.pokemon import Pokemon
from pokebook.models.type import Type
from pokebook.utils.urls import apiurl
from pokebook.utils.constants import apiconst


def get_pokemon_by_name(value:str):
    """
    Recupera la información de un pokemón por medio de su nombre.

    Parámetro:

        value - Nombre del pokemón.
    """
    if value and value.strip().lower() != '':
        return get_pokemon(f'{apiurl.POKEMON_URL}/{value.strip().lower()}')
    else:
        raise(ValueError('The name value must be a valid name.'))


def get_pokemon_by_id(value:int):
    """
    Recupera la información de un pokemón por medio de su id.

    Parámetro:

        value - Número que identifica al pokemón.
    """
    if value and value > 0:
        return get_pokemon(f'{apiurl.POKEMON_URL}/{value}')
    else:
        raise(ValueError('The id value must be major to zero.'))


def get_pokemon(pokemon_url:str):
    """
    Recupera la información de un pokemón por medio de la pokeapi.

    Parámetros:

        url - Url para realizar la petición get y obtener un pokemon.
    """    
    response = requests.get(pokemon_url)
    if response.ok:
        response_json = response.json()
        pokemon = Pokemon(response_json[apiconst.ID], response_json[apiconst.NAME] , pokemon_url)
        pokemon.types = []

        for type_slot in response_json[apiconst.TYPES]:
            pokemon_type = type_slot[apiconst.TYPE]
            pokemon.types.append(Type(pokemon_type[apiconst.NAME], pokemon_type[apiconst.URL]))
        
        return pokemon
    else:
        print(f'[{response.status_code}]: {response.reason}')