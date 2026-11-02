import json

with open("incomplete_server.json", "r") as file:
    data = json.load(file)

print(f"Server: {data['name']}")
print(f"Region: {data['region']}")
print(f"CPU: {data['specs']['cpu']}")  # This will CRASH")")")
