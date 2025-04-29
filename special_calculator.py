


print("Hello, this is my final project :)")
username = input("What is your name? ")
print("Hi " + username + ", nice to meet you")
print("This is a special calculator, I would need two number from you")
firstnum = input("First number ")
secondnum = input("Second number ")
print("Thank you for putting your numbers, "+firstnum+" and "+secondnum)
firstnumis = "odd" ; secondnumis = "odd" # predefine both numbers as odd
if int(firstnum) %2 == 0: #check oddness of first number
    firstnumis = "even" #define first number as even if not odd
if int(secondnum) %2 ==0: #check oddness of second number
    secondnumis = "even" #define second number as even if not odd
print("I can see that th first number is "+firstnumis)
print("And the second one is "+secondnumis)
if firstnumis == secondnumis:
    print ("So both of them are "+firstnumis)
else:
    print("So one of them is even, and one is odd")
operator = input("Operator (+, - , *, /): ")
result = ("Error: Operator "+operator+" is not supported \nAn error had occured, please try again")
if operator == "+":
    result = firstnum+" "+operator+" "+secondnum+" = "+str((int(firstnum)+int(secondnum)))
if operator == "-":
    result = firstnum+" "+operator+" "+secondnum+" = "+str((int(firstnum)-int(secondnum)))
if operator == "*":
    result = firstnum+" "+operator+" "+secondnum+" = "+str((int(firstnum)*int(secondnum)))
if operator == "/":
    choice = input("You chose division, should the result be integer? (y/n)" )
    if choice == "y":
        result = firstnum+" "+operator+" "+secondnum+" = "+str(int(int(firstnum)/int(secondnum)))
    else:
        result = firstnum+" "+operator+" "+secondnum+" = "+str((int(firstnum)/int(secondnum)))
print(result)

import time
now = (time.ctime())
print ("Thank you "+username+" for using the calculator on "+now)


