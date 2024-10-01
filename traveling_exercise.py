cities = {
    "New York": ["Tokyo", "Paris", "London"],
    "Poznan": ["London", "Berlin"],
    "London": ["New York", "Poznan"],  
    "Berlin": ["Tokyo", "Poznan"],
    "Tokyo": ["New York", "Berlin"],
    "Paris": ["Katmandu"]
}

print("\nYour task: fly to Katmandu\n")

location = input("Where are you currently located? (New York, Poznan, London, Berlin, Tokyo, Paris)\n")

while location != 'Katmandu':
    if location in cities:
        print(f"You are in {location}")
        print("There are flights to", cities[location])
        destination = input("Where would you like to travel?")
        if destination in cities[location]:
            location = destination
        else:
            print(f"There is no flight to {destination}")
    else:
        print(f"There is no flight to {location}")
    
print("You have reached your destination")