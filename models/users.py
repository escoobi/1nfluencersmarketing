"""
User class where it receives the parameters email, name and password.
The getter and setter was generated and has a dictionary return
"""
class Users:

    def __init__(self: object, email: str, name: str, password: str):
        self.__email: str = email
        self.__name: str = name
        self.__password: str = password

    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, name: str) -> None:
        self.__name: str = name

    @property
    def email(self: object) -> str:
        return self.__email

    @email.setter
    def email(self: object, email: str) -> None:
        self.__email: str = email

    @property
    def password(self: object) -> str:
        return self.__password

    @password.setter
    def password(self: object, password: str) -> None:
        self.__password: str = password

    # return a dict with name, email and password
    def __dict__(self: object) -> dict:
        return {"name": self.name, "email": self.email, "password": self.password}


