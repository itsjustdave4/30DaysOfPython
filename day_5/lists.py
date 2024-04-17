# Exercises - Day 5

# Exercise: Level 1

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
list=[1, 2, 3, 4, 5, 6, 7]

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
print(list[0])  # first item - 1
print(list[int((len(list) - 1) / 2)])   # middle item - 4
print(list[-1]) # last item - 7

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ("Dave", 27, 1.79, "married", "@home")

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])  # Facebook
print(it_companies[int((len(list) - 1) / 2)])   # Apple
print(it_companies[-1]) # Amazon

# Print the list after modifying one of the companies
it_companies[-1] = "SAP"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Amazon")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(int((len(list) - 1) / 2), "Accenture")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = str(it_companies[1].upper())
print(it_companies)

# Join the it_companies with a string '#;  '
print("#;   ".join(it_companies))

# Check if a certain company exists in the it_companies list.
print("Oracle" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[int((len(list) - 1) / 2)])   # IBM

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(int((len(list) - 1) / 2))
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies) # []

# Destroy the IT companies list
# del it_companies
print(it_companies) # leads to an error

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
index_redux = full_stack.index("Redux")
full_stack.insert(index_redux + 1, "SQL")
full_stack.insert(index_redux + 1, "Python")

# Exercise: Level 2

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
print(ages[0])  # min age: 19
max_age = ages[-1]
print(ages[-1]) # max age: 26
# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
# Find the median age (one middle item or two middle items divided by two)
median_age = ages[int(len(ages) - 1 / 2)] / 2   # 13
# Find the average age (sum of all items divided by their number)
average = sum(ages) / len(ages) # 22.75
# Find the range of the ages (max minus min)
ages.sort()
max = ages[-1]
min = ages[0]
range = max - min   # 7
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min - average) == abs(max - average)) # False

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Find the middle country(ies) in the countries list
print(countries[int((len(countries) - 1) / 2)]) # Lesotho

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_first_half = []
countries_second_half = []

countries_first_half = countries[0:int((len(countries) - 1) / 2)]
countries_second_half = countries[int((len(countries) - 1) / 2):-1]
print(countries_first_half)
print(countries_second_half)
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries
