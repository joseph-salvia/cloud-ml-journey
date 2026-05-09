import json

with open("incomplete_server.json", "r") as file:
    data = json.load(file)

print(f"Server: {data['name']}")
print(f"Region: {data['region']}")

# Safe access with fallback values
specs = data.get('specs', {})  # Returns {} if 'specs' doesn't exist
cpu = specs.get('cpu', 'Unknown')
ram = specs.get('ram', 'Unknown')

print(f"CPU: {cpu}")
print(f"RAM: {ram}")
