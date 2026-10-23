# activity 1.2
# Calculate the area of a rectangle
length = 5
width = 3

area = length * width
print("Area of rectangle:", area)

# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: ")) # use input()
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit) # use print()

# Puzzler 1
x = 10
y = 3.5
z = x + y
print(z)
print(type(z))
# ผลลัพธ์ที่ได้: z = 13.5
# type(z) = float
# เหตุผล เนื่องจาก x เป็น int (จำนวนเต็ม) และ y เป็น float (ทศนิยม) 
# เมื่อบวกกัน Python จะให้ผลการคำนวณค่าเป็น float เพื่อไม่ให้ข้อมูลทศนิยมผิดพลาดหรือหายไป

# Puzzler 2
name = "Alice"
age = "30" # Note: This is a string
message = name + " is " + age + " years old."
print(message)
print(type(age))
# ผลลัพธ์ที่ได้: "Alice is 30 years old."
# type(age) = String
# เหตุผล เนื่องจากตัวแปร age ถูกเก็บเป็น "30" (ไม่ใช่ตัวเลข)การใช้ + ระหว่าง string จะเป็นการต่อข้อความ
# จึงได้ข้อความรวมกัน และ age ยังคงเป็น string เพราะไม่ได้แปลงเป็นตัวเลข

# Puzzler 3
is_sunny = True
is_raining = False
print(is_sunny and is_raining)
print(type(is_sunny))
# ผลลัพธ์ที่ได้: False
# type(is_sunny) = boolean
# ใน boolean เงื่อนไข AND ต้องเป็นจริงทั้งคู่ แต่ที่นี่มี False ผลลัพธ์จึงเป็น False

# Puzzler 4
num_str = input("Enter a number: ")
result = num_str + 5
print(result)
# ผลลัพธ์ที่ได้: error
# input() ใน Python จะคืนค่าเป็น String เสมอ แต่เมื่อ input ตัวเลข Python จะคำนวณ "10" + 5
# แต่ "10" เป็น str และ 5 เป็น int จึงไม่สามารถบวกกันได้ และเกิด error
# 