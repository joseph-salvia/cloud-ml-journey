import csv

servers = [
    ["name", "region", "cpu", "ram"],
    ["cache-server-01", "us-west-2", "2", "4"],
    ["ml-server-02", "us-east-1", "16", "64"]
]

with open("new_servers.csv", "w") as file:
    csv_writer = csv.writer(file)

    for row in servers:
        csv_writer.writerow(row)

    print("CSV file created!")
