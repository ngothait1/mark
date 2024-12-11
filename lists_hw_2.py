my_list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]

#Print after sorting
my_list.sort()
print(my_list)

# Print in reverse (casual method)

# my_list.sort(reverse=True)
# print(my_list)

# Print in reverse using "sorted" function

print(sorted(my_list, reverse=True))

#Print max
max_value = max(my_list)
print(max_value)

#Print min (another method)

print(min(my_list))

### ---- ###

my_list.sort(reverse=True)

first_five_items = my_list[:5]
print(first_five_items)

