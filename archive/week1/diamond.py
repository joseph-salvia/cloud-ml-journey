# I thought it was going to be a nested loop until the iterations got so much
#But this is the end result
size = int(input("How much number of star rows do you want?:\t"))



for i in range(1 ,size + 1):
    space = size - i
    star = i
    
    print(" " * space, end="")  
    print("* " * star, end=" ")
    print()

for j in range(1 ,size):
    spaces = j
    stars = size - j

    print(" " * spaces, end="")  
    print("* " * stars, end=" ")
    print()
