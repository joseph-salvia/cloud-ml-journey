age = int(input("What is your age?  "))
had_id = input("Do you have an ID?  yes/no \n")

if age >= 18 and had_id == "yes":
    print("You may enter the building")
elif age >= 18 and had_id != "yes":
    print("Sorry, you are old enough but you need an ID")
else:
    print("You are not old enough to enter")
