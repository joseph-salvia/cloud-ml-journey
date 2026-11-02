import json

with open("server_config.json", "r") as file:
    data = json.load(file)  # Converts JSON to Python dict

print(type(data))
print(data)
print()

# Access nested data (remember Day 6!)
print(f"Server Name: {data['name']}")
print(f"Region: {data['region']}")
print(f"CPU: {data['specs']['cpu']}")
print(f"RAM: {data['specs']['ram']}")
print(f"Tags: {data['tags']}")
