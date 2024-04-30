# Exercises - Day 9

# Exercise: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years
age = int(input("Enter your age: "))
if age >= 18 :
    print("You are old enough to drive")
else: 
    print(f"You need {18 - age} more years to learn to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age
my_age = 27
your_age = int(input("Enter your age: "))
if my_age < your_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me")
    else:
        print(f"You are {your_age - my_age} years older than me")
else:
    print("Im older than you")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_one} is smaller than {number_two}")
else:
    print(f"{number_one} is equal to {number_two}")

# Exercise: Level 2

# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score = int(input("Enter your score: "))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter a month: ")
if month == "December" or month == "January" or month == "February":
    print("Season is Winter")
elif month == "March" or  month == "April" or month == "May":
    print("Season is Spring")
elif month == "June" or month == "July" or month == "August":
    print("Season is Summer")
elif month == "September" or month == "October" or month == "November":
    print("Season is Autumn")
else:
    print("No valid month")

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit_to_add = input("Enter a fruit to add in the list: ")

if fruit_to_add in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit_to_add)

# Exercise: Level 3

# Here we have a person dictionary.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print(person["skills"][int((len(person["skills"]) - 1) / 2 )])
else:
    print("No attribute skills found")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person and "Python" in person["skills"]:
    print("Found Python in skills!")
else:
    print("Didnt found Pythin in skills!")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if "JavaScript" in person["skills"] and "Ready" in person["skills"]:
    print("He is a front end developer")
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a backend developer")
elif "React" in person["skills"]  and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print["He is a fullstack developer"]
else:
    print("unknown title")
# If the person is married and if he lives in Finland, print the information in the following format:
#       Asabeneh Yetayeh lives in Finland. He is married.

if person["is_marred"] is True and person["country"] is "Finland":
    print(f"{person['first_name']} {person['first_name']} lives in {person['country']}. He is married.")
