from models.poke import Poke


"""
Extend class Poke for PokeAbilities
one for many
One Pokemon for many abilities.
"""
class PokeAbiliteis(Poke):
    def __init__(self: object, name: str, pic: str, name_abilities: str) -> None:
        super(PokeAbiliteis, self).__init__(name, pic)
        self.__name_abilities = name_abilities

    @property
    def name_abilities(self):
        return self.__name_abilities

    @name_abilities.setter
    def name_abilities(self, value):
        self.__name_abilities

    def __dict__(self: object) -> dict:
        return {"name": self.name, "pic": self.pic, "ability": self.name_abilities}