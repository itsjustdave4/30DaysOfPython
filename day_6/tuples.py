# Exercises - Day 6

# Exercise: Level 1

# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Marlon", "Luke", "Baghira", "Alfred", "Oskar")
sisters = ("Lisa", "Litsa") 

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("Moni")
siblings.append("Thomas")
family_members = tuple(siblings)

# Unpack siblings and parents from family_members
family_members = list(family_members)
siblings, parents = family_members[:7], family_members[-2:]

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "apple", "orange")
vegetables = ("tomato", "carrot", "corn")
animal_products = ("meat", "milk", "egg")
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[int((len(food_stuff_tp) - 1) / 2)]) # carrot

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    # Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)    # False
    # Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)    # True
    # nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')