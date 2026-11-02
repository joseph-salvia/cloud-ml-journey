#Test project to build a robot barista, an assignment by Networkchuck
#The goal is for the robot barista to recieve the input and give an output

#This is the initial greeting and asking of the customer's name
print("Hello, Welcome to the LALSA coffee shop")
name1 = input("What should we call you\n\n")

#Greeting the customer in their name
print("\nThank you for coming in today "+ name1 + ".")

menu = ("Mocha\nGreen Tea\nCappucino")

#Presenting to the customer, the menu available for themto choose from and the response of getting it to them shortly
request = input("What can we get you from our Menu Today\n \n" + menu + "\n\n")

#The tip function of the bot
#The bot asks how much tip they want to give and then thanks them for the tip

tip_list = ("$10 \n$15 \n$25")

tip = input("\nAlright " + name1 + "." + "We'll get you your " + request + " shorty.\nThank you for your purchase and how much tip will you like to give?\n" + tip_list + "\n\n" )

print("\nThank you " + name1 + ", for the the $" + str(tip) + " tip.")


