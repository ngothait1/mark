import os
import pandas as pd 
from person_class import Person


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
            

def saveNewEntry(target_database, target_list) -> int:
    user_id = getId(target_database)
    if user_id == -1:
        return 0
    user_name = input("Name: ")
    user_age = getAge()
    if user_age == -1:
        return 0
    addUser(target_database, target_list, user_id, user_name, user_age)
    return user_age


def addUser(target_database, target_list, user_id, user_name, user_age) -> None:
    target_database[user_id] = Person(user_id, user_name, user_age)
    target_list.append(user_id)
    print("ID [" + str(user_id) + "] saved succesfully")  


def getId(target_database) -> int:
    user_typed_id = fetchNumberWithin(what_is_fetched="Add new ID to the database", error_to_display="ID")
    if user_typed_id is False:
        return -1
    if user_typed_id in target_database:
        print("Error: ID already exists " + str(target_database[user_typed_id]))
        return -1
    return user_typed_id


def getAge() -> int:
    user_typed_age = fetchNumberWithin("Type the age", "Age", 0, 120)
    if user_typed_age is False:
        return -1
    return user_typed_age


def searchById(source_dict, source_list) -> None:
    id_in_question = fetchNumberWithin(what_is_fetched="Type the ID you would like to search", error_to_display="ID")
    if id_in_question in source_list:
        index_of_id = source_list.index(id_in_question)
        printUserDetailsByIndex(index_of_id, source_dict, source_list, False)
    else:
        print("Error: ID " + str(id_in_question) + " is not saved")
        return    
    

def printUserDetailsByIndex(indexed_entry, source_dict, source_list, print_as_list=True) -> None:
    if not (0 <= indexed_entry < len(source_list)):
        return
    person_id = source_list[indexed_entry]
    person: Person = source_dict[person_id]
    spacer = ""
    if print_as_list:
        spacer = "    "
        print(str(indexed_entry)+ ". " + str(source_list[indexed_entry]))
    else:
        print("ID: " + str(source_list[indexed_entry]))
    print(spacer + "Name: " + person.getName())
    print(spacer + "Age: " + str(person.getAge()))   
    return
    

def printAllNames(source_dict) -> None:
    for index, person_id in enumerate(source_dict):
        person: Person = source_dict[person_id]
        print(str(index) + ". " + person.getName())


def printAllIds(source_list) -> None:
    for i, user_id in enumerate(source_list):
        print(str(i) + ". " +str(user_id)) 


def printAllEntries(source_dict, source_list) -> None:
    for user_index in range(len(source_list)):
        printUserDetailsByIndex(user_index, source_dict, source_list, print_as_list=True)
 

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
        average_age = sum_of_ages/len(list_of_ids)
        print(average_age)


def checkDatabaseExists(source_dict) -> bool:
    if not source_dict: 
        print("Error: Can't perform operation - Database is empty")
        return False 
    return True 


def printEntryByIndex(source_list, source_dict) -> None:
    typed_index = fetchNumberWithin(what_is_fetched="Which index would you like to display", error_to_display="Index")
    if not typed_index < len(source_list):
        print("Index out of range. The maximum index allowed is " + str((len(user_database)-1)))
    printUserDetailsByIndex(typed_index, source_dict, source_list, print_as_list=False)


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


def writeToFile(user_database: dict[int, 'Person'], current_path: str) -> bool:

    file_name = getFileName(current_path)
    data = []

    for person_id, person in user_database.items():
        row = {
        "id": person_id,          
        "name": person.getName(),
        "age": person.getAge()
    }
        data.append(row)
    
    df = pd.DataFrame(data)

    output_path = os.path.join(current_path, file_name)
    df.to_csv(output_path, index=False)
    print("File saved succsfully to " + current_path + file_name)
    return True


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


while True:
    choice = selectFromMenu()
    if choice == 1:
        sum_of_ages = sum_of_ages + saveNewEntry(user_database, list_of_ids)
    elif choice == 2:
        if checkDatabaseExists(user_database) == True:
            searchById(user_database, list_of_ids)
    elif choice == 3:
        if checkDatabaseExists(user_database) == True:
            printAgesAverage()
    elif choice == 4:
        if checkDatabaseExists(user_database) == True:
            printAllNames(user_database)
    elif choice == 5:
        if checkDatabaseExists(user_database) == True:
            printAllIds(list_of_ids)
    elif choice == 6:
        if checkDatabaseExists(user_database) == True:
            printAllEntries(user_database, list_of_ids)   
    elif choice == 7:
        if checkDatabaseExists(user_database) == True:
            printEntryByIndex(list_of_ids, user_database)
    elif choice == 8:
        if checkDatabaseExists(user_database) == True:
            if not writeToFile(user_database, current_path):
                print("Couldn't write data to csv file")
    elif choice == 9:
        if requestToExit() == True:
            break
    input("Press Enter to continue ")    
