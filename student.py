from person import Person
import os

class Student(Person):
    def __init__(self, user_id: int, name: str, age: int, field_of_study: str, year_of_study: int, score_avg: int) -> None:
        super().__init__(user_id, name, age)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getType(self) -> str:
        return "Student"

    def getFieldOfStudy(self) -> str:
        return self._field_of_study 
    
    def getYearOfStudy(self) -> int:
        return self._year_of_study
    
    def getScoreAvg(self) -> int:
        return self._score_avg
    
    def toCsvRow(self) -> dict:
        try:
            data = super().toCsvRow()
            data.update({
                "field_of_study": self.getFieldOfStudy(),
                "year_of_study": self.getYearOfStudy(),
                "avg_score": self.getScoreAvg()
            })
            return data
        except Exception as e:
            print("Error creating CSV row: " + str(e))
            return {}

    def printMyself(self, single_line: bool = False) -> str:
        base_info = super().printMyself(single_line) 
        if single_line:
            return base_info + " | Student in " + self._field_of_study + " (Year: " + str(self._year_of_study) + ", Avg Score: " + str(self._score_avg) + ")"
        else:
            print("He is a student in the field of study of " + self.getFieldOfStudy() + ".")
            print("The year of study is " + str(self.getYearOfStudy()) + " and the average score is " + str(self.getScoreAvg()) + ".")
            return ""

if __name__ == "__main__":
    print("Error: This file should not be running. This is a class file: " + os.path.basename(__file__))