# So, I mostly used nested if's to create a condition for each number

server_list = []

user_input = ()

while True: #user_input != 4:
    print("\n---- CLOUD SERVER MANAGER ----")
    user_input = int(input("\nThis is the Menu\nEnter 1 to Add a Server\nEnter 2 to Remove a server\nEnter 3 to View all servers\nEnter 4 to quit\t"))
    if user_input == 1:
        add_server = input("\nWhat is the name of the server you want to add?\t")
        server_list.append(add_server)
        print("\n" + add_server + " has been added to the list successfully.")
    elif user_input == 2:
        server_delete = input("\nWhat server do you want to delete?\t")
        if server_delete not in server_list:
            print("\nSorry, Server not found!")
        else:
            server_list.remove(server_delete)
            print("\nThe server: " + server_delete + ", has been deleted")
    elif user_input == 3:
        if len(server_list) == 0:
            print("\nNo active servers.")
        else:
            for server in server_list:
                print(server, end="    ")            
    elif user_input == 4:
        print("\nShutting down manager.......")
        break
    else:
        print("\nInvalid Choice!\nEnter either 1,2,3 or 4.")





