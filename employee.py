from person import Person
import os

class Employee(Person):
    def __init__(self, user_id: int, name: str, age: int, field_of_work: str, salary: int) -> None:
        super().__init__(user_id, name, age)
        self._field_of_work = field_of_work
        self._salary = salary

    def getType(self) -> str:
        return "Employee"

    def getFieldOfWork(self) -> str:
        return self._field_of_work
    
    def getSalary(self) -> int:
        return self._salary
    
    def toCsvRow(self) -> dict:
        try:
            data = super().toCsvRow()
            data.update({
                "field_of_work": self.getFieldOfWork(),
                "salary": self.getSalary()
            })
            return data
        except Exception as e:
            print("Error creating CSV row: " + str(e))
            return {}
    
    def printMyself(self, single_line: bool = False) -> str:
        base_info = super().printMyself(single_line)  
        if single_line:
            return base_info + " | Employee in " + self._field_of_work + " with a salary of $" + str(self._salary)
        else:
            print("He is an employee in the field of work of " + self.getFieldOfWork() + ".")
            print("His salary is $" + str(self.getSalary()) + ".")
            return ""
        
if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))