import os
import pandas as pd 
from person import Person
from student import Student
from employee import Employee


def fetchNumberWithin(what_is_fetched="Type input your input: ", error_to_display="Your input", min_value=0, max_value=9999999999) -> int:
    while True:
        unverified_input = input(what_is_fetched + ": ")
        if not unverified_input.isdigit():
            print("Error: " + error_to_display + " must be a number. '" + unverified_input + "' is not a number")
            continue
        number_as_integer = int(unverified_input)
        if not (min_value <= number_as_integer <= max_value):
            print("Select a number between " + str(min_value) + " and " + str(max_value))
            continue 
        return number_as_integer
            

def saveNewEntry(target_database: dict[int, Person], target_list: list[int]) -> int:
    try:
        user_id = getId(target_database)
        if user_id == -1:
            return 0
        user_name = input("Name: ")
        user_age = fetchNumberWithin("Type the age", "Age", 0, 120)

        print("Select type of person:")
        print("1. Student")
        print("2. Employee")
        print("3. Regular Person")
        user_type = fetchNumberWithin("Enter choice", "Choice", 1, 3)

        if user_type == 1:
            print("Select Field of Study:")
            print("1. Software Development")
            print("2. Electrical Engineering")
            print("3. Medicine")
            print("4. Business Administration")
            print("5. Mechanical Engineering")
            print("6. Psychology")
            field_choice = fetchNumberWithin("Enter choice", "Field of Study", 1, 6)
            field_of_study_options = [
                "Software Development", "Electrical Engineering", "Medicine",
                "Business Administration", "Mechanical Engineering", "Psychology"
            ]
            field_of_study = field_of_study_options[field_choice - 1]

            year_of_study = fetchNumberWithin("Year of Study", "Year", 1, 10)
            score_avg = fetchNumberWithin("Average Score (stored as an integer)", "Average Score", 0, 100)
            print("Note: The average score is stored without decimals.")

            try:
                target_database[user_id] = Student(user_id, user_name, user_age, field_of_study, year_of_study, score_avg)
            except KeyError as e:
                print("Error: Invalid key used in database operation:", str(e))
                return 0

        elif user_type == 2:
            print("Select Field of Work:")
            print("1. Software Engineering")
            print("2. Healthcare")
            print("3. Education")
            print("4. Finance")
            print("5. Construction")
            print("6. Retail")
            work_choice = fetchNumberWithin("Enter choice", "Field of Work", 1, 6)
            field_of_work_options = [
                "Software Engineering", "Healthcare", "Education",
                "Finance", "Construction", "Retail"
            ]
            field_of_work = field_of_work_options[work_choice - 1]

            salary = fetchNumberWithin("Salary", "Salary", 0, 1000000)
            try:
                target_database[user_id] = Employee(user_id, user_name, user_age, field_of_work, salary)
            except KeyError as e:
                print("Error: Invalid key used in database operation:", str(e))
                return 0

        else:
            try:
                target_database[user_id] = Person(user_id, user_name, user_age)
            except KeyError as e:
                print("Error: Invalid key used in database operation:", str(e))
                return 0

        target_list.append(user_id)
        print("ID [" + str(user_id) + "] saved successfully")
        return user_age
    except Exception as e:
        print("Error while saving entry:", str(e))
        return 0
    

def getId(target_database) -> int:
    user_typed_id = fetchNumberWithin(what_is_fetched="Add new ID to the database", error_to_display="ID")
    if user_typed_id in target_database:
        print("Error: ID already exists " + str(target_database[user_typed_id]))
        return -1
    return user_typed_id


def searchById(source_dict: dict[int, Person]) -> None:
    user_id = fetchNumberWithin("Type the ID you would like to search", "ID")
    if user_id not in source_dict:
        print("Error: ID " + str(user_id) + " is not saved")
        return
    source_dict[user_id].printMyself(single_line=False)
        
    
def displayUserDetailsById(person_id: int, source_dict: dict[int, Person]) -> None:
    if person_id not in source_dict:
        print("Error: ID " + str(person_id) + " is not found")
        return
    person: Person = source_dict[person_id]
    if person is not None:
        print("ID: " + str(person_id))
        print("Name: " + person.getName())
        print("Age: " + str(person.getAge()))
    else:
        print("Error: The person object is None.")


def displayAllNames(source_dict) -> None:
    for index, person_id in enumerate(source_dict):
        person: Person = source_dict[person_id]
        print(str(index) + ". " + person.getName())


def displayAllIds(source_list) -> None:
    for i, user_id in enumerate(source_list):
        print(str(i) + ". " +str(user_id)) 


def displayAllEntries(source_dict, source_list) -> None:
    for user_id in source_list:
        print(source_dict[user_id].printMyself(single_line=True))


def getYesImSure() -> bool:
    while True:
        y_or_n = input("Are you sure? (y/n)")
        if y_or_n == "y":
            return True
        elif y_or_n == "n":
            return False
        

def requestToExit() -> bool:
    if getYesImSure() is True:
        print("Goodbye!")
        return True
    else:
        return False


def printAgesAverage() -> None:
    try:
        average_age = sum_of_ages / len(list_of_ids)
        print("Average age: {0}".format(average_age))
    except ZeroDivisionError:
        print("Cannot calculate average: No entries in database")


def checkDatabaseExists(source_dict) -> bool:
    if not source_dict: 
        print("Error: Can't perform operation - Database is empty")
        return False 
    return True 

def displayEntryByIndex(source_list: list[int], source_dict: dict[int, Person], print_as_list: bool = False) -> None:
    typed_index = fetchNumberWithin("Which index would you like to display", "Index")
    
    if not (0 <= typed_index < len(source_list)):
        print("Index out of range. The maximum index allowed is " + str(len(source_list) - 1))
        return
    
    person_id = source_list[typed_index]
    person: Person = source_dict[person_id]

    if print_as_list:
        print(str(typed_index) + ". " + str(person_id))
    else:
        person.printMyself(single_line=False)


def getFileName(current_path: str) -> str:
    file_name = input("Type a name for the CSV file: ")
    
    if not file_name.endswith(".csv"):
        if file_name.endswith((".", ".c", ".cs")):
            file_name = file_name[:file_name.rfind(".")]
        file_name += ".csv"

    if fileExists(current_path, file_name):
        print(file_name + " already exists. If you proceed all previous data will be permanently lost.")
        if getYesImSure() is True:
            return file_name
        else:
            return getFileName(current_path) 
    return file_name


def writeToFile(user_database: dict[int, Person], current_path: str) -> bool:
    try:
        file_name = getFileName(current_path)
        data = []
        for person in user_database.values():
            data.append(person.toCsvRow())

        df = pd.DataFrame(data)

        output_path = os.path.join(current_path, file_name)
        
        directory = os.path.dirname(output_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(output_path, index=False)
        print("File saved successfully to " + output_path)
        return True
    except FileNotFoundError as e:
        print("FileNotFoundError: " + str(e))
        return False
    except PermissionError as e:
        print("PermissionError: " + str(e))
        print("Please check your permissions for the directory: " + directory)
        return False
    except Exception as e:
        print("Couldn't write data to csv file: " + str(e))
        return False


def fileExists(current_path: str, file_name: str) -> bool:
    full_path = os.path.join(current_path, file_name)
    return os.path.exists(full_path)

    
def selectFromMenu() -> int:
    print("1. Save new entry\n"+
          "2. Search by ID\n"+
          "3. Print ages average\n"+
          "4. Print all name\n"
          "5. Print all IDs\n"
          "6. Print all entries\n"
          "7. Print entry by index\n"
          "8. Save all data\n"
          "9. Exit")
    return fetchNumberWithin(what_is_fetched="Please enter your choice", error_to_display="Choice", min_value=1, max_value=9)


user_database = {}
list_of_ids = []
sum_of_ages = 0 
current_path: str = os.path.join(os.getcwd(), "")


try:
    while True:
        choice = selectFromMenu()
        if choice == 1:
            sum_of_ages = sum_of_ages + saveNewEntry(user_database, list_of_ids)
        elif choice == 2:
            if checkDatabaseExists(user_database) == True:
                searchById(user_database)
        elif choice == 3:
            if checkDatabaseExists(user_database) == True:
                printAgesAverage()
        elif choice == 4:
            if checkDatabaseExists(user_database) == True:
                displayAllNames(user_database)
        elif choice == 5:
            if checkDatabaseExists(user_database) == True:
                displayAllIds(list_of_ids)
        elif choice == 6:
            if checkDatabaseExists(user_database) == True:
                displayAllEntries(user_database, list_of_ids)   
        elif choice == 7:
            if checkDatabaseExists(user_database) == True:
                displayEntryByIndex(list_of_ids, user_database, print_as_list=False)
        elif choice == 8:
            if not writeToFile(user_database, current_path):
                print("Operation ednded without writing to file")
        elif choice == 9:
            if requestToExit() == True:
                break
        input("Press Enter to continue ")
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt. Exiting...")
    exit()
except ValueError as e:
    print("Invalid input! Please enter a valid number.")
except KeyError:
    print("Error: ID not found in the database.")
except IndexError:
    print("Error: Index out of range.")
except ZeroDivisionError:
    print("Error: Cannot calculate average age (no entries).")
except Exception as e:
    print("An unexpected error occurred:", str(e))
      

