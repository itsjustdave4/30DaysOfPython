# Exercises - Day 8

# Exercise: Level 1

# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Marlon"
dog["color"] = "Yellow"
dog["breed"] = "mixed breed"
dog["legs"] = 4
dog["age"] = 12
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Dave", 
    "last_name": "Se", 
    "gender": "male", 
    "age": 27, 
    "martial_status": "married", 
    "skills": ["Pyton","SQL","Java","OOP"], 
    "country": "Germany",
    "city": "Heidelberg",
    "adress": "@home"
    }
# Get the length of the student dictionary
print(len(student)) # 9

# Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))  # list

# Modify the skills values by adding one or two skills
student["skills"].append("HTML")
student["skills"].append("CSS")

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop("adress")

# Delete one of the dictionaries
del student