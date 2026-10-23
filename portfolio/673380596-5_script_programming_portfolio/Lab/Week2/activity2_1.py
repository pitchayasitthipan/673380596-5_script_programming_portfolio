# Block A: Evaluation Check
temp = 25
is_raining = True
if temp > 20 and not is_raining:
    print("Perfect day for a picnic!")
elif temp <= 20 or is_raining:
    print("Stay indoors or bring an umbrella.") # Expected output matches here
else:
    print("Unsure about the weather.")
# #การทำงานทีละขั้นตอน
# กำหนดค่า: temp = 25, is_raining = True
# ตรวจ if:
#   temp > 20 -> True (25 > 20)
#   not is_raining -> False (เพราะ is_raining = True)
# ดังนั้น True and False = False -> ไม่เข้าเงื่อนไขแรก

# ตรวจ elif:
# temp <= 20 -> False
# is_raining -> True
# ดังนั้น False or True = True -> เข้าเงื่อนไขนี้ 

# โปรแกรมเลือกบล็อก elif -> แสดงผล: Stay indoors or bring an umbrella.

# Block B: Vectorized Filter
phrase = "Python 2026 Engine"
consonants = {c.lower() for c in phrase if c.isalpha() and c.lower() not in 'aeiou'}
print(f"Unique consonants: {consonants}")
# การทำงานทีละขั้นตอน
# phrase = "Python 2026 Engine"
# เงื่อนไข:
# c.isalpha() → เลือกเฉพาะตัวอักษร (ตัวเลข 2026 ถูกตัดออก)
# c.lower() not in 'aeiou' → กรองเฉพาะพยัญชนะ (ไม่ใช่สระ)
# ผลลัพธ์ที่ได้: { 'p', 'y', 't', 'h', 'n', 'g' }
# โปรแกรมแสดงผล: Unique consonants: {'p', 'y', 't', 'h', 'n', 'g'}

