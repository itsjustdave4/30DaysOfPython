# Exercises - Day 2

# Exercise: Level 1

# 1. Declare a first name variable and assign a value to it
first_name = "Dave"
# 2. Declare a last name variable and assign a value to it
last_name = "Se"
# 3. Declare a full name variable and assign a value to it
full_name = "Dave Se"
# 4. Declare a country variable and assign a value to it
country = "Germany"
# 5. Declare a city variable and assign a value to it
city = "Heidelberg"
# 6. Declare an age variable and assign a value to it
age = 27
# 7. Declare a year variable and assign a value to it
year = 1997
# 8. Declare a variable is_married and assign a value to it
is_married = False
# 10. Declare a variable is_true and assign a value to it
is_true = True
# 11. Declare a variable is_light_on and assign a value to it
is_light_on = False
# 12. Declare multiple variable on one line
query_language, coding_language, os, want_to_learn_it = "SQL", "Python", "Linux", True

# Exercise Level 2

# Check the data type of all your variables using type() built-in function
print(type(first_name))         # str
print(type(last_name))          # str
print(type(country))            # str
print(type(city))               # str
print(type(age))                # int
print(type(year))               # int
print(type(is_married))         # bool
print(type(is_true))            # bool
print(type(is_light_on))        # bool
print(type(query_language))     # str
print(type(coding_language))    # str
print(type(os))                 # str
print(type(want_to_learn_it))   # bool

# Using the len() built-in function, find the length of your first name
print(len(first_name)) # 5

# Compare the length of your first name and your last name
print(f"your first name has {len(first_name)} characters and your lastname has {len(last_name)} characters")

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14159265 * (30 ** 2)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 3.14159265 * (30 * 2)

# Take radius as user input and calculate the area.
radius = input("Enter radius: ")
area_of_circle = 3.14159265 * (int(radius) * 2)
print(area_of_circle)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name= input("Enter firstname: ")
last_name = input("Enter lastname: ")
country = input("Enter age: ")
age = input("Enter your age: ")
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
