# Week 10 Lab: Automating Spreadsheets (Excel)

ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

อ่านข้อมูลขายจาก `data/input_sales.xlsx` คำนวณราคารวมต่อรายการและ Grand Total
แล้วเขียนรายงานที่จัดรูปแบบแล้วลง `data/output_sales_report.xlsx` ด้วย `openpyxl`

## วิธีรัน
```bash
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
pip install -r requirements.txt
python main.py
```

## ผลลัพธ์ที่ได้
ไฟล์ `data/output_sales_report.xlsx` มีหัวตารางสีเขียว แถวสินค้า 5 รายการ และแถว Grand Total (3,203.97)
