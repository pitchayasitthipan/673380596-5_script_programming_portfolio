# main_program.py
# Lab 6.2: ใช้ custom module และ standard library
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1
import my_utils
import math
import random

my_utils.greet("Alice")

for n in [7, 10, 1, 13]:
    print(n, "is prime?", my_utils.is_prime(n))

print("sqrt(144) =", math.sqrt(144))
print("Random number (1-100):", random.randint(1, 100))
