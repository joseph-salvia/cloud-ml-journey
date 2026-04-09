# I even made it that if a user used more than an amount, they get a discount

print("---- CLOUD MANAGER -----")
print("Welcome to the Cloud manager cost calculator.")
hours = float(input("How many hours of compute service did you use?:\t"))
storage_gb = float(input("\nAlright, How many gb of storage did you use?:\t"))
network_gb = float(input("\nGood, And how many Gigabyte of network did you consume?:\t"))


def compute_cost(hours, compute_rate=0.05):
    compute_total = hours * compute_rate
    return compute_total

compute = compute_cost(hours)

def storage_cost(storage_gb, cost_per_gb=0.023):
    storage_total = storage_gb * cost_per_gb
    return storage_total

storage = storage_cost(storage_gb)

def network_cost(network_gb, cost_per_gb=0.09):
    network_total = network_gb * cost_per_gb
    return network_total

network = network_cost(network_gb)

def total_cost(compute, storage, network):
    total_all = compute + storage + network
    return total_all

total = total_cost(compute, storage, network)

def grand_total_cost(total, discount=0.9):
    grand_cost = total * discount
    return grand_cost

grand_total = grand_total_cost(total)

if total < 150:
    print(f"\nHere you go, your total is ${total:.2f}. Thank you")
else:
    print("\nHurray!!, You spent over $150 and you qualify for a 10% discount")
    print(f"Your Grand total after applying the discount is ${grand_total}. Thank you")
