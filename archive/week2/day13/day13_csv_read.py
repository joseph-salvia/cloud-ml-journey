#import csv

#with open("servers.csv", "r") as file:
    #csv_reader = csv.reader(file)

    #for row in csv_reader:
        #print(row)

import csv

with open("servers.csv", "r") as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)  # Skip the header row
    print(f"Header: {header}\n")

    for row in csv_reader:
        name = row[0]
        region = row[1]
        cpu = row[2]
        ram = row[3]
        print(f"{name} in {region}: {cpu} CPUs, {ram}GB RAM")
