class Person:
    def __init__(self, user_id: int, name: str, age: int) -> None:
        self._user_id = user_id
        self._name = name
        self._age = age


    def getName(self) -> str:
        return self._name


    def getAge(self) -> int:
        return self._age
    
    

