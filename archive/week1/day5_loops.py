cloud_providers = ["AWS", "GCP", "Azure", "DigitalOcean"]

for index, cloud in enumerate(cloud_providers):
    print("Provider" + str(index + 1) + ": " + cloud)
    
