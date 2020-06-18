"""
Servicios para recuperar la información de un pokemón.
"""
import requests
from pokebook.models.pokemon import Pokemon
from pokebook.models.type import Type
from pokebook.models.move import Move
from pokebook.models.sprites import Sprites
from pokebook.models.ability import Ability
from pokebook.utils.urls import apiurl
from pokebook.utils.constants import apiconst


def get_pokemons(limit = 10, offset = 0):
    """
    Parametters:

        limit - Cantidad de pokemones que se desean listar.
        offset - A partir de cual pokemon que se desplegará la lista.
    """
    pokemons = []

    pokemon_params = {
                        apiurl.LIMIT_ARG:limit if limit and limit > 1 else 10, 
                        apiurl.OFFSET_ARG:offset if offset and offset > 1 else 10
                    }
    response = requests.get(apiurl.POKEMON_URL, params = pokemon_params)

    if response.ok:
        response_json = response.json()    
        for pokemon_json in response_json[apiconst.RESULTS]:
            pokemons.append(get_pokemon(pokemon_json[apiconst.URL]))
            
    return pokemons

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

        for type_slot in response_json[apiconst.TYPES]:
            pokemon_type = type_slot[apiconst.TYPE]
            pokemon.types.append(Type(pokemon_type[apiconst.NAME], pokemon_type[apiconst.URL]))

        for move_slot in response_json[apiconst.MOVES]:
            pokemon_move = move_slot[apiconst.MOVE]
            pokemon.moves.append(Move(pokemon_move[apiconst.NAME], pokemon_move[apiconst.URL])) 

        for ability_slot in response_json[apiconst.ABILITIES]:
            pokemon_ability = ability_slot[apiconst.ABILITY]
            pokemon.abilities.append(Ability(pokemon_ability[apiconst.NAME], pokemon_ability[apiconst.URL])) 

        sprites = response_json[apiconst.SPRITES]
        pokemon_sprites = Sprites()
        pokemon_sprites.back_default = sprites[apiconst.BACK_DEFAULT]
        pokemon_sprites.back_female = sprites[apiconst.BACK_FEMALE]
        pokemon_sprites.back_shiny = sprites[apiconst.BACK_SHINY]
        pokemon_sprites.back_shiny_female = sprites[apiconst.BACK_SHINY_FEMALE]
        pokemon_sprites.front_default = sprites[apiconst.BACK_DEFAULT]
        pokemon_sprites.front_female = sprites[apiconst.FRONT_FEMALE]
        pokemon_sprites.front_shiny = sprites[apiconst.FRONT_SHINY]
        pokemon_sprites.front_shiny_female = sprites[apiconst.FRONT_SHINY_FEMALE]
        pokemon.sprites = pokemon_sprites

        return pokemon
    else:
        print(f'[{response.status_code}]: {response.reason}')