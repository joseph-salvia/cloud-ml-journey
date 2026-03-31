secret_no = 7


print("Welcome to the guessing game")

user_no = "" 

for trial in range(3):
    if user_no != secret_no:
        user_no = int(input("Guess a number between 1 and 10\n"))
        if user_no < secret_no:
            print("Too Low, Try again")
        elif user_no > secret_no:
            print("Too high, Try again")    
        else:
            print("Congratulations, You guessed it right!")
            break
else:
    print("Game over! The Secret number is " + str(secret_no) + ".")
