with open("notes.txt", "r") as file:
    content = file.read()


print(content)
print("\nFile automatically closed after 'with' block")
