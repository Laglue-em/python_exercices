import random

# Correcting the dictionary format
countries = {
    "France": "Paris",
    "Belgium": "Brussels",
    "Denmark": "Copenhagen"
}

messages = ["Love", "Hate", "Enjoy", "Good French Fries"]

# Randomly selecting a country and its capital
country, capital = random.choice(list(countries.items()))

# Randomly selecting a message
message = random.choice(messages)

# Corrected print statement
print(f"I was in {capital}, {country} for the holiday. My impression is '{message}'.")
