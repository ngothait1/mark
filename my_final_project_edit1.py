# Print the menu of 8 options and fetch 
def selectFromMenu():
    print("1. Save new entry\n"+
          "2. Search by ID\n"+
          "3. Print ages average\n"+
          "4. Print all name\n"
          "5. Print all IDs\n"
          "6. Print all entries\n"
          "7. Print entry by index\n"
          "8. Exit")
    return fetchNumberWithin("Please enter your choice", 1, 8)

# Verify that a number is within a range an return an integer
def fetchNumberWithin(what_is_fetched, min_value=0, max_value=9999999999): 
    unverified_input = input(what_is_fetched + ": ")
    while True:
        if unverified_input.isdigit():
            number_as_integer = int(unverified_input)
            if min_value <= number_as_integer <= max_value:
                return number_as_integer
            else:
                unverified_input = input("Select a number between " + str(min_value) + " and " + str(max_value)+ ": ")
        else:
            print("Error: " + what_is_fetched + " must be a number. '" + unverified_input + "' is not a number")
            unverified_input = input("Type your choice again or hit Enter to go back to the menu ")
            if unverified_input == "":
                return False

# Save a new entry to the Database, option 1            
def saveNewEntry(target_database, target_list):  
    user_typed_id = fetchNumberWithin(what_is_fetched="ID")
    if user_typed_id is False:
        return 0
    if user_typed_id in target_database:
        print("Error: ID already exists " + str(target_database[user_typed_id]))
        return 0
    user_typed_name = input("Name: ")
    user_typed_age = fetchNumberWithin("Age", 0, 120)
    if user_typed_age is False:
        return 0
    target_database[user_typed_id] = { "NAME" : user_typed_name , "AGE" : user_typed_age }
    target_list.append(user_typed_id)
    print("ID [" + str(user_typed_id) + "] saved succesfully")
    return user_typed_age

def searchById(id_in_question, source_dict, source_list):
    if id_in_question in source_list:
        index_of_id = source_list.index(id_in_question)
        printUsers(index_of_id, source_dict, source_list, print_as_list=False)
        return
    print(str(id_in_question) + " could not be found in the database")
    
def printUsers(indexed_entry, source_dict, source_list, print_as_list=True): 
    if indexed_entry < len(source_dict):
        key = source_list[indexed_entry]
        spacer = ""
        if print_as_list:
            spacer = "    "
            print(str(indexed_entry)+ ". " + str(key))
        else:
            print("ID: " + str(key))
            print(spacer + "Name: " + source_dict[key]["NAME"])
            print(spacer + "Age: " + str(source_dict[key]["AGE"]))      
    else:
        return 
    
def printAllNames(source_db):
    iterating_index = 0
    for key in source_db:
        name_to_print = source_db[key]["NAME"]
        print(str(iterating_index) + ". " + name_to_print)
        iterating_index += 1

#Print all ID's in indexed order
def printAllIds(source_list):
    for i, id in enumerate(source_list):
        print(str(i) + ". " +str(id)) 

def printAllEntries(source_dict, source_list):
    for i, index in enumerate(source_dict):
        printUsers(i, source_dict, source_list, print_as_list=True)
 
def requestToExit():
    while True:
        y_or_n = input("Are you sure? (y/n) ")
        if y_or_n == "y":
            print("Goodbye!")
            return True
        elif y_or_n == "n":
            return False

def printAgesAverage():
        average_age = sum_of_ages/len(user_database)
        print(average_age)

def checkDatabaseEmpty():
    if len(user_database) == 0:
        print("Error: Can't perform operation - Database is empty")
    else:
        return False 

user_database = {}
user_ids = []
sum_of_ages = 0 

while True:
    choice = selectFromMenu()
    if choice == 1:
        sum_of_ages = sum_of_ages + saveNewEntry(user_database, user_ids)
    elif choice == 2:
        if checkDatabaseEmpty() == False:
            entered_id = fetchNumberWithin(what_is_fetched="ID")
            if entered_id in user_database:
                searchById(entered_id, user_database, user_ids)
            else: print("Error: ID " + str(entered_id) + " is not saved")
    elif choice == 3:
        if checkDatabaseEmpty() == False:
            printAgesAverage()
    elif choice == 4:
        if checkDatabaseEmpty() == False:
            printAllNames(user_database)
    elif choice == 5:
        if checkDatabaseEmpty() == False:
            printAllIds(user_ids)
    elif choice == 6:
        if checkDatabaseEmpty() == False:
            printAllEntries(user_database, user_ids)   
    elif choice == 7:
        if checkDatabaseEmpty() == False:
            typed_index = fetchNumberWithin(what_is_fetched="Index")
            if typed_index < len(user_database):
                printUsers(typed_index, user_database, user_ids, print_as_list=False)
            else:
                print("Index out of range. The maximum index allowed is " + str((len(user_database)-1)))        
    elif choice == 8:
        if requestToExit():
            break
    input("Press Enter to continue ")    
