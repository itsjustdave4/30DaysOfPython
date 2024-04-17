# Exercises - Day 4

# Exercise: Level 1

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty" + " " + "Days" + " " + "Of" + " " + "Python")

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding" + " " + "For" + " " + "All")

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))     # 14

# Change all the characters to uppercase letters using upper() method.
print(company.upper())  # CODING FOR ALL

# Change all the characters to lowercase letters using lower() method.
print(company.lower())  # coding for all

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize()) # Coding for all
print(company.title())      # Coding For All
print(company.swapcase())   # cODING fOR aLL

# Cut(slice) out the first word of Coding For All string.
print(company[7:])  # FOR All

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))  # with index returns 0

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))  # Python For All

# Change Python for Everyone to Python for All using the replace method or other methods.
print("Python for Everyone".replace("for Everyone", "for All")) # Python for All

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))   # ['Coding', 'For', 'All']

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# What is the character at index 0 in the string Coding For All.
print(company[0])   # C

# What is the last index of the string Coding For All.
print(company[-1])  # l

# What character is at index 10 in "Coding For All" string.
print(company[10])  # space

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
print("".join([l for l in string if l.isupper()]))  # PFE

# Create an acronym or an abbreviation for the name 'Coding For All'.
string = "Coding Fro All"
print("".join([l for l in string if l.isupper()]))  # CFA

# Use index to determine the position of the first occurrence of C in Coding For All.
print("Coding For All".index("C"))  # 0

# Use index to determine the position of the first occurrence of F in Coding For All.
print("Coding For All".index("F"))  # 7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))   # 19

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".find("because"))    # 31

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".rfind("because"))   # 47

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction"[31:54]) # because because because

# Does 'Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))    # True

# Does 'Coding For All' end with a substring coding?
print("Coding For All".startswith("coding"))    # False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("   Coding For All      ".strip(" "))

# Which one of the following variables return True when we use the method isidentifier():
#   - 30DaysOfPython
print("30DaysOfPython".isidentifier())  # False
#   - thirty_days_of_python
print("thirty_days_of_python".isidentifier())   # True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_libraries))

# Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
radius = 10
area = int(3.14 * radius ** 2)
print(f"radius = {radius}")
print(f"area = 3.14 * radius ** 2")
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Make the following using string formatting methods:
a = 8
b = 6
# 8 + 6 = 14
print(f"{a} + {b} = {a + b}")
# 8 - 6 = 2
print(f"{a} - {b} = {a - b}")
# 8 * 6 = 48
print(f"{a} * {b} = {a * b}")
# 8 / 6 = 1.33
print(f"{a} / {b} = {a / b}")
# 8 % 6 = 2
print(f"{a} % {b} = {a % b}")
# 8 // 6 = 1
print(f"{a} // {b} = {a // b}")
# 8 ** 6 = 262144
print(f"{a} ** {b} = {a ** b}")