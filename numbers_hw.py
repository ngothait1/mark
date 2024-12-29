import json

def isEven(number) -> bool:
    return (number %2 == 0)

path_to_numbers_folder: str = "/Users/markofir/py/json_exercise/"

with open(path_to_numbers_folder+"numbers.json", "r") as numbers_file:
    numbers: list[int] = json.load(numbers_file)

with open(path_to_numbers_folder+"numbers_dictionary2.json", "w") as numbers_dict_file:
    numbers_dictionary: dict[int, bool] = {}
    for number in numbers:
        numbers_dictionary[int(number)] = isEven(int(number))
    json.dump(numbers_dictionary, numbers_dict_file, indent=4)



