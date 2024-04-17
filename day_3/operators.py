# Exercises - Day 3

# Exercise: Level 1

# Declare your age as integer variable
my_age = 27

# Declare your height as a float variable
my_height = 1.78

# Declare a variable that store a complex number
my_complex_num = 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print(f"The area of the triangle is {int(area_of_triangle)}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c 
print(f"The perimeter of the triangle is {int(perimeter_of_triangle)}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rectangle_length = float(input("Enter length: "))
rectangle_width = float(input("Enter width: "))
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
print(f"area is {rectangle_area}")
print(f"perimeter is {rectangle_perimeter}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
circle_radius = float(input("Enter radius: "))
circle_area = pi * circle_radius * circle_radius
circle_circumference = 2 * pi * circle_radius
print(f"area of the circle is {circle_area}")
print(f"circumference of the circle is {circle_circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope
slope_1 = -2
# x-intercept when y = 0 
x = -2 / -2
# y-intercept when x = 0
y = 2 * 0 - 2

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
euclidean_distance = (((x2 - x1) ** 2) + (y2 - y1) ** 2) ** 0.5
print(f"Slope is {slope_2}")
print(f"Euclidean distance is {euclidean_distance}")

# Compare the slopes in tasks 8 and 9.
print(slope_1 is slope_2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3  # x needs to be -3 for y = 0 
print(0 is x ** 2 + 6 * x + 9 )

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") != len("dragon"))   # False

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")    # True

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon.")  # True

# There is no 'on' in both dragon and python
print("on" not in "dragon" and "on" not in "python")    # False

# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("python"))))    # 6.0

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a Number: "))
print(number % 2 == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7)) # True

# Check if type of '10' is equal to type of 10
print(type("10") is 10) # False

# Check if int('9.8') is equal to 10
print(int(9.8) is 10)   # False

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate_per_hour}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = int(input("Enter number of years have lived: "))
print(f"You have lived for {years_lived * 365 * 24 * 60 * 60} seconds.")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
i = 1
while i <= 5:
    print(i, i**0, i**1, i**2, i**3)
    i += 1
