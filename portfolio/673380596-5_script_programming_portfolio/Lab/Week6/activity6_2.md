# Activity 6.2: Benefits of Modular Programming & Standard Library

**ชื่อ:** นส.พิชยา สิทธิพันธ์  **รหัสนักศึกษา:** 673380596-5  **sec.1**

## 1. ประโยชน์ของการแบ่งโค้ดเป็น function และ module
- **โปรเจกต์ใหญ่**: แบ่งงานเป็นส่วนเล็กๆ อ่านและหาโค้ดง่ายกว่าเขียนยาวไฟล์เดียว
- **ทำงานเป็นทีม**: แต่ละคนรับผิดชอบคนละ module ไม่ต้องแก้ไฟล์เดียวกัน ลดโอกาสโค้ดชนกัน
- **หา bug ง่าย**: ถ้าผลผิด รู้ได้ว่าให้ไปดู function ไหน
- **ทดสอบง่าย**: ทดสอบทีละ function ได้ เช่น `is_prime(7)` ควรได้ `True`
- **ใช้ซ้ำได้**: เขียนครั้งเดียวเรียกใช้ได้หลายที่ เช่น `my_utils.py` import ไปใช้ในโปรแกรมอื่นได้

## 2. สำรวจ Standard Library (https://docs.python.org/3/library/)

**datetime**: ใช้จัดการวันที่และเวลา เช่น แสดงวันที่วันนี้ หรือนับว่าเหลืออีกกี่วันถึงกำหนดส่งงาน
```python
from datetime import date
print(date.today())
```

**os**: ใช้ทำงานกับไฟล์และโฟลเดอร์ เช่น ดูรายชื่อไฟล์ในโฟลเดอร์ หรือเช็กว่ามีไฟล์อยู่หรือไม่
```python
import os
print(os.listdir("."))
```

**collections**: มีโครงสร้างข้อมูลเพิ่มเติม เช่น `Counter` นับจำนวนซ้ำได้สั้นกว่าเขียน dict เอง (ใช้แทน Activity 5.2 ได้)
```python
from collections import Counter
print(Counter("hello world".split()))
```
