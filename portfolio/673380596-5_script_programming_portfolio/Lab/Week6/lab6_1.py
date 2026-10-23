# lab6_1.py
# Lab 6.1: Simple Calculator Functions
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1


def add(a, b):
    """บวกเลขสองจำนวน แล้วคืนผลลัพธ์"""
    return a + b


def subtract(a, b):
    """ลบเลข a ด้วย b แล้วคืนผลลัพธ์"""
    return a - b


def multiply(a, b):
    """คูณเลขสองจำนวน แล้วคืนผลลัพธ์"""
    return a * b


def divide(a, b):
    """หาร a ด้วย b ถ้า b เป็น 0 จะคืนข้อความ error แทน"""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base, exponent=2):
    """ยกกำลัง base ด้วย exponent ถ้าไม่ใส่ exponent จะยกกำลังสอง"""
    return base ** exponent


while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")
    choice = input("Choose (1-6): ")

    if choice == "6":
        print("Bye!")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Please choose 1-6")
        continue

    try:
        num1 = float(input("Enter first number: "))
        if choice == "5":
            # ถ้าเว้นว่างไว้ ให้ใช้ค่า default (ยกกำลังสอง)
            exp = input("Enter exponent (press Enter for 2): ")
            if exp == "":
                result = power(num1)
            else:
                result = power(num1, float(exp))
        else:
            num2 = float(input("Enter second number: "))
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
    except ValueError:
        print("Please enter numbers only")
        continue

    print("Result:", result)
