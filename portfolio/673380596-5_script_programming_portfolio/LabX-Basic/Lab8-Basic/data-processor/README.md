# Week 8 Lab: Automating with CSV and JSON Data

ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

อ่านไฟล์ `data/input_sales.csv` (กรองยอดขาย >= 100 พร้อมแถวสรุป) และ `data/input_inventory.json`
(อัปเดตสต็อก + เพิ่มสินค้าใหม่) แล้วเขียนผลลงไฟล์ output ในโฟลเดอร์ `data/`

## วิธีรัน
```bash
python main.py
```
ใช้เฉพาะ standard library (csv, json, logging, os) ไม่ต้องติดตั้ง package เพิ่ม
