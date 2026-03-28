#Building a fully functional calculator 
#I will firstly create the variables of the first and second number so they can be used later

first_number = input("What is your first number? \n")
second_number = input("Alright, And what is your second number? \n")

# Now I combine the two variables to make arithmetic

addition = float(first_number) + float(second_number)
subtraction = float(first_number) - float(second_number)
division = float(first_number) / float(second_number)
multiplication = float(first_number) * float(second_number)

# Now I print the output of those solutions to the user

print("The addition of these numbers is " + str(addition))
print("The subtraction of these numbers is " + str(subtraction))
print("The division of these numbers is " + str(division))
print("The multiplication  of these numbers is " + str(multiplication))
