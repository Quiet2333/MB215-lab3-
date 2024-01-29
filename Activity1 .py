# Function to convert kilometers to miles and round the result to 2 decimal places
def convert_km_to_miles(km):
    # Conversion factor: 1 kilometer is approximately 0.621371 miles
    miles = km * 0.621371
    return round(miles, 2)

# Taking input from the user
kilometers = float(input("Enter distance in kilometers: "))
miles = convert_km_to_miles(kilometers)

# Printing the result
print(f"{kilometers} kilometers is equal to {miles} miles.")
