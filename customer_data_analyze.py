import pandas as pd

path_to_folder = "/Users/markofir/py/"
file_name = "customer_data.csv"

df = pd.read_csv(path_to_folder + file_name)

## Biggest Purchase Ammount

biggest_so_far = 0
for index, row in df.iterrows():
    purchas_amount = row["purchase_amount"]
    if purchas_amount > biggest_so_far:
        biggest_so_far = purchas_amount
        print(str(index) + " " + str(biggest_so_far))
    
## Average Age Of All Customers

sum_of_ages = 0
number_of_columns = 100000

for index, row in df.iterrows():
    current_row_age = row["age"]
    sum_of_ages += current_row_age

average_age = sum_of_ages/number_of_columns
print("Average age is: " + str(average_age))

## Sum incomes up to id 8349

sum_income = 0

for index, row in df.iterrows():
    current_row_income = row["income"]
    if row["id"]>8349:
        break
    sum_income += current_row_income

print("Sum of incomes up to id 8349 is: :" + str(sum_income))

## Most popular product category

books = 0
clothing = 0
food = 0
electronics = 0
home = 0
beauty = 0
health = 0

for index, row in df.iterrows():
    current_product_category = row["product_category"]
    if current_product_category == "Books":
        books += 1
    elif current_product_category == "Clothing":
        clothing += 1
    elif current_product_category == "Food":
        food += 1
    elif current_product_category == "Electronics":
        electronics += 1
    elif current_product_category == "Home":
        home += 1
    elif current_product_category == "Beauty":
        beauty += 1
    elif current_product_category == "Health":
        health += 1

print("Books =" + str(books))
print("Clothing =" + str(clothing))
print("Food =" + str(food))
print("Electronics =" + str(electronics))
print("Home =" + str(home))
print("Beauty =" + str(beauty))
print("Health =" + str(health))

## Count satisfaction score > 7

sat_score_count = 0

for index, row in df.iterrows():
    current_sat_score = row["satisfaction_score"]  
    if current_sat_score >= 8:  
        sat_score_count += 1

print("Satisfaction score count above 7 is:" + str(sat_score_count))
