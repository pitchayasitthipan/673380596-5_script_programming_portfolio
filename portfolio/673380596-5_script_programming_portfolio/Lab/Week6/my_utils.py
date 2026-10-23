# my_utils.py
# Custom module สำหรับ Lab 6.2
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1


def greet(name):
    """แสดงข้อความทักทาย"""
    print(f"Hello, {name}!")


def is_prime(number):
    """คืน True ถ้า number เป็นจำนวนเฉพาะ ไม่ใช่คืน False"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
