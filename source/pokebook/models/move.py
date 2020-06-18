from pokebook.models.abstract_model import AbstractModel


class Move(AbstractModel):
    """
    Movimiento que puede tener un pokemon.
    """
    def __init__(self, name:str, url = ''):
        self.name = name
        self.accuracy = 0
        self.pp = 0
        self.power = 0
        self.url = url

    
    def __str__(self):
        return f'Move(name:{self.name}, accuracy:{self.accuracy}, pp:{self.pp}, power:{self.power})'


    def __eq__(self, right):
        return self.name == right.name


    @property
    def name(self):
        """
        Nombre del movimiento, este debe ser de tipo str y no puede ser una cadena vacía ni un valor None.
        """
        return self.__name

    @name.setter
    def name(self, name:str):
        if not name or name.strip() == '':
            raise(ValueError('El valor del movimiento no puede ser None ni una cadena en blanco o vacía.'))
        self.__name = name.strip()

    @property
    def accuracy(self):
        """
        La precisión debe deser un valor entero positivo partiendo de cero.
        """
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, accuracy:int):
        self.__accuracy = accuracy if accuracy and accuracy >= 0 else 0

    @property
    def pp(self):
        """
        El PP debe deser un valor entero positivo partiendo de cero.
        """
        return self.__pp

    @pp.setter
    def pp(self, pp:int):
        self.__pp = pp if pp and pp >=0 else 0    

    @property
    def power(self):
        """
        El poder del movimiento debe deser un valor entero positivo partiendo de cero.
        """
        return self.__power

    @power.setter
    def power(self, power:int):
        self.__power = power if power and power >= 0 else 0