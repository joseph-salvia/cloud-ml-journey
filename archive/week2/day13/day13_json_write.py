import json

# Python dictionary
server = {
    "name": "db-server-02",
    "region": "eu-west-1",
    "specs": {
    "cpu": 8,
    "ram": 32
    },
    "tags": ["production", "database", "postgresql"]
}

# Write to JSON file
with open("new_server.json", "w") as file:
    json.dump(server, file, indent=2)  # indent=2 makes it pretty

print("JSON file created!")
