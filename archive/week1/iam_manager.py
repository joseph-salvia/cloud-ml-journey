
# The unique thing about the dict is that it has a function to print out if the list is empty

iam_db  = {}


while True:
    print("\n---- Cloud Manager ----")
    print("1. Add User\n2. Update User Role\n3. Delete User\n4. View All User\n5. Exit")
    choice = int(input("Enter 1,2,3,4 or 5 to choose:\t"))
    if choice == 1:
        username = input("\nWhat is your username?:\t")
        iam_db[username] = {}
        print("The username: " + username +  ", has been saved")
        print("\nWhat role do you hold?")
        role = input("Are  you an Admin, a Dev, or a Guest:\t")
        iam_db[username] = {"role":role}
        print("Your role as: " + role + ", has been recorded")
    elif choice == 2:
        user_name = input("\nWhat is your username?:" + "\t")
        if user_name in iam_db:
            print("\nAlright " + user_name + ", what role will you want to update to?")
            new_role = input("Do you want to change to an Admin, a Dev, or a Guest?:\t")
            iam_db[user_name] = {"role": new_role}
            print(user_name + ", Your role as: " + new_role + " has been updated sucessfully.")
        else:
            print("\nError!!, The username is not in the database")
    elif choice == 3:
        name_delete = input("\nWhat is your username?:" + "\t")
        if name_delete in iam_db:
            deleted = iam_db.pop(name_delete)
            print("The user: " + name_delete + ", has been deleted.")
        else:
            print("There is no such user in the Database!!")
    elif choice == 4:
        if len(iam_db) == 0:
            print("The User list is empty")
        else:
            for k, v in iam_db.items():
                print(k, v)
    elif choice == 5:
        print("\nShutting down Manager.......")
        break
    else:
        print("Invalid input, enter either 1, 2, 3, 4, or 5.")

