from pokebook.models.abstract_model import AbstractModel


class Sprites(AbstractModel):
    """
    Guarda las URLs que almacenan los sprites de un pokemon.
    """
    def __init__(self):
        """
        Un pokemon puede no contar con todos los sprites.

        Attributes:

            back_default
            back_female
            back_shiny
            back_shiny_female
            front_default
            front_female
            front_shiny
            front_shiny_female
        """
        self.back_default = None
        self.back_female = None
        self.back_shiny = None
        self.back_shiny_female = None
        self.front_default = None
        self.front_female = None
        self.front_shiny = None
        self.front_shiny_female = None