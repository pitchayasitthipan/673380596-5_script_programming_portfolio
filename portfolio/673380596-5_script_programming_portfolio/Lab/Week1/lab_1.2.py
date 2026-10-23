# lab 1.2

age = 21    # integer
gpa = 3.5  # float
favorite_color = "blue" # string
is_student = True   # boolean

print("Age: ", age)
print("GPA: ", gpa)
print("Favorite Color: ", favorite_color)
print(is_student)

num1 = 10  # integer
num2 = 3.5 # float
name = "Pitchaya"   # string

# operations
sum_result = num1 + num2  
product_result = num1 * num2
difference_result = num1 - num2
division_result = num1 / num2

print("Sum result:", sum_result)
print("Product result:", product_result)
print("Difference result:", difference_result)
print("Division result:", division_result)

# use input()
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# use print()
print("Sum:", num1 + num2)
print("Product:", num1 * num2)
print("Difference:", num1 - num2)
print("Division:", num1 / num2)
print(name)

# ---2---
first_name = "Pitchaya"
last_name = "Sitthipan"

full_name = first_name + " " + last_name

# Print greeting with f-string
print(f"Hello, {full_name}!")

# ---3---
# Ask for a favorite number
fav_num = input("Enter your favorite number: ")

# Store it in a variable & Print the type of the input variable using type()
print("Type before conversion:", type(fav_num))

# Convert to integer
fav_num_int = int(fav_num)

# Add 5 and print result
print("After adding 5:", fav_num_int + 5)



