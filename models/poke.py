from typing import Any, Type

"""
This receive the dataframe parameters with their respective getter and setter.

This class is a master class
"""

class Poke:

    def __init__(self: object, name: str, pic: str) -> None:
        self.__name = name
        self.__pic = pic

    @property
    def name(self: object) -> str:
        return self.__name
    '''
    Setter name
    '''
    @name.setter
    def name(self: object, name: str) -> None:
        self.__name: str = name

    @property
    def pic(self: object) -> str:
        return self.__pic

    '''
        Setter pic
    '''
    @pic.setter
    def pic(self: object, pic: str) -> None:
        self.__pic: str = pic


