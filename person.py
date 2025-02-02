import os 

class Person:
    def __init__(self, user_id: int, name: str, age: int) -> None:
        self._user_id = user_id
        self._name = name
        self._age = age

    def getType(self) -> str:
        return "Person"

    def getName(self) -> str:
        return self._name

    def getAge(self) -> int:
        return self._age
    
    def toCsvRow(self) -> dict:
        try:
            data = {
                "user_id": self._user_id,
                "name": self._name,
                "age": self._age,
                "type": self.getType(),
                "field_of_study": "",
                "year_of_study": "",
                "avg_score": "",
                "field_of_work": "",
                "salary": ""
            }
            return data
        except Exception as e:
            print("Error creating CSV row: " + str(e))
            return {}
    

    def printMyself(self, single_line: bool = False) -> str:
        if single_line:
            return "ID: " + str(self._user_id) + " | Name: " + self._name + " | Age: " + str(self._age)
        else:
            print("ID: " + str(self._user_id))
            print("Name: " + self._name)
            print("Age: " + str(self._age))
        return ""
    
if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))