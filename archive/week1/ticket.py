age = int(input("How old are you? \n"))

day = input("Is it a weekday or a weekend? \n")

#I created a template for the text instead of repeating it over and over again

ticket_temp = "\nYour Ticket fee is "

#It is now time to create the if and elif statement for the conditions

if age < 12 and day == "weekday":
    print(ticket_temp + "$5.")
elif age < 12 and day != "weekday":
    print(ticket_temp + "$8.")
elif age >= 12 and age <= 17 and day == "weekday":
    print(ticket_temp + "$10.")
elif age >= 12 and age <= 17 and day != "weekday":
    print(ticket_temp + "$13.")
elif age >= 18 and age <= 64 and day == "weekday":
    print(ticket_temp + "$15.")
elif age >= 18 and age <= 64 and day != "weekday":
    print(ticket_temp + "$18.")
elif age >= 65  and day == "weekday":
    print(ticket_temp + "$7.")
elif age >= 65 and day != "weekday":
    print(ticket_temp + "$10.")


