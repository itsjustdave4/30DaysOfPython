# Exercises - Day 7

# Exercise: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))    # 7

# Add 'Twitter' to it_companies
it_companies.add("Twitter")

# Insert multiple IT companies at once to the set it_companies
it_companies.update("Accenture", "SAP")

# Remove one of the companies from the set it_companies
it_companies.remove("Facebook")

# What is the difference between remove and discard
# .discard() will not raise an error if the item isn't found

# Exercise: Level 2

# Join A and B
AB = A.union(B)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))    #  True

# Are A and B disjoint sets
print(A.isdisjoint(B))  # False

# Join A with B and B with A
AB = A.union(B)
BA = B.union(A)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))    # {27, 28}

# Delete the sets completely
del A
del B

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_list = list(age)
print(len(age_list))    # 8
print(len(age))         # 8
print(len(age) is len(age_list))    # True

# Explain the difference between the following data types: string, list, tuple and set
# string: collection of chars
# list: ordered and changeable collection of elements
# tuple: ordered and unchangeable collection of elements 
# set: unindexed and unordered collection of elements

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
sentence_words = sentence.split()
sentence_words_first_half = sentence_words[0:int((len(sentence_words) -1) / 2)]
sentence_words_second_half = sentence_words[int((len(sentence_words) -1) / 2):-1]
sentence_words_first_half = set(sentence_words_first_half)
sentence_words_second_half = set(sentence_words_second_half)
unique_words = sentence_words_second_half.symmetric_difference(sentence_words_first_half)
print(len(unique_words))    # 7 {'love', 'teacher', 'inspire', 'a', 'teach', 'am', 'to'}