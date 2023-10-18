import random

# Lists of sample first and last names of cricketers
first_names = ["Virat", "Sachin", "Rohit", "MS", "Kane", "Joe", "Steve", "AB", "David", "Chris"]
last_names = ["Kohli", "Tendulkar", "Sharma", "Dhoni", "Williamson", "Root", "Smith", "de Villiers", "Warner", "Gayle"]

# Generate a random cricketer name
random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

random_cricketer_name = f"{random_first_name} {random_last_name}"

print(random_cricketer_name)
