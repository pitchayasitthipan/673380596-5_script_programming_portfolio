# activity6_1.py
# Activity 6.1: Refactoring a Previous Lab (Week 2: lab2_1 Number Classifier)
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

# ---------- โค้ดเดิม (Week 2) ----------
# num = int(input("Enter an integer: "))
#
# if num > 0 and num % 2 == 0:
#     print("The number is positive and even.")
# elif num > 0 and num % 2 != 0:
#     print("The number is positive and odd.")
# elif num < 0 and num % 2 == 0:
#     print("The number is negative and even.")
# elif num < 0 and num % 2 != 0:
#     print("The number is negative and odd.")
# else:
#     # กรณี num == 0
#     print("The number is zero and even.")
#
# ปัญหาของโค้ดเดิม: เช็กบวก/ลบ และคู่/คี่ ปนกันในทุก elif เลยต้องเขียนซ้ำ 4 แบบ
# และถ้าอยากใช้เช็กแค่คู่/คี่ ก็เอาไปใช้ซ้ำไม่ได้

# ---------- หลัง refactor ----------


def get_sign(num):
    """คืนค่า 'positive', 'negative' หรือ 'zero' ตามเครื่องหมายของ num"""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    return "zero"


def get_parity(num):
    """คืนค่า 'even' ถ้า num เป็นเลขคู่ ไม่งั้นคืน 'odd'"""
    if num % 2 == 0:
        return "even"
    return "odd"


def classify_number(num):
    """คืนข้อความบอกว่า num เป็นบวก/ลบ/ศูนย์ และคู่/คี่"""
    return "The number is " + get_sign(num) + " and " + get_parity(num) + "."


num = int(input("Enter an integer: "))
print(classify_number(num))
