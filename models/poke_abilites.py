from models.poke import Poke


"""
Extend class Poke for PokeAbilities
one for many
One Pokemon for many abilities.

This class inherits the name and photo attributes from the master class.

This class returns a dictionary
"""

class PokeAbiliteis(Poke): # Extend the Poke class
    def __init__(self: object, name: str, pic: str, name_abilities: str) -> None:
        super(PokeAbiliteis, self).__init__(name, pic) # Atribution class Poke
        self.__name_abilities = name_abilities

    @property
    def name_abilities(self):
        return self.__name_abilities

    '''
    Setter name_abilities
    '''

    @name_abilities.setter
    def name_abilities(self, value):
        self.__name_abilities

    """
    Returns a dictionary
    """
    def __dict__(self: object) -> dict:
        return {"name": self.name, "pic": self.pic, "ability": self.name_abilities}