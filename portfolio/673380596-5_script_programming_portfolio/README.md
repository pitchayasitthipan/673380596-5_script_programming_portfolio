# รวมงานวิชา Script Programming (CP352301)

**ชื่อ-นามสกุล:** นส.พิชยา สิทธิพันธ์  **รหัสนักศึกษา:** 673380596-5  **Section:** 1

Repository นี้รวมงานทั้งหมดที่ทำตลอดภาคเรียน แบ่งโฟลเดอร์ตามโครงสร้างที่อาจารย์กำหนด

## โครงสร้างโฟลเดอร์

| โฟลเดอร์ | เนื้อหา |
| :--- | :--- |
| [`Lab/`](./Lab) | Lab ประจำสัปดาห์ (Week 1, 2, 4, 5, 6, 12) |
| [`LabX-Basic/`](./LabX-Basic) | LabX Basic: Lab7 (Web Scraping), Lab8 (CSV/JSON), Lab10 (Excel), Lab11 (PDF/Word) |
| [`LabX-Advance/`](./LabX-Advance) | LabX Advance: Lab AD1 (Agentic Web Scraper) |
| [`Mini-Project/`](./Mini-Project) | Mini Project: ระบบแจ้งเตือนเครื่องซักผ้าร้านหยอดเหรียญ (ลิงก์ไปยัง repository ของกลุ่ม) |
| [`Final-Project/`](./Final-Project) | Final Project: Virtual Pet Companion (ลิงก์ไปยัง repository ของกลุ่ม) |
| [`Certificate/`](./Certificate) | ภาพ certificate จาก https://www.netacad.com/ (Python Essentials 1) |

## รายละเอียดแต่ละโฟลเดอร์

### Lab (ประจำสัปดาห์)
| สัปดาห์ | โฟลเดอร์ | หัวข้อ |
| :--- | :--- | :--- |
| 1 | [`Lab/Week1`](./Lab/Week1) | พื้นฐาน Python |
| 2 | [`Lab/Week2`](./Lab/Week2) | Conditionals |
| 3 | - | ดูหมายเหตุด้านล่าง |
| 4 | [`Lab/Week4`](./Lab/Week4) | Lists & Tuples |
| 5 | [`Lab/Week5`](./Lab/Week5) | Dictionaries & Sets |
| 6 | [`Lab/Week6`](./Lab/Week6) | Functions & Modules |
| 12 | [`Lab/Week12`](./Lab/Week12) | Final Project Development: Enhanced Task Manager CLI |

### LabX Basic
| Lab | โฟลเดอร์ | หัวข้อ |
| :--- | :--- | :--- |
| Lab 7 Basic | [`LabX-Basic/Lab7-Basic`](./LabX-Basic/Lab7-Basic) | Introduction to Web Scraping (requests + BeautifulSoup) |
| Lab 8 Basic | [`LabX-Basic/Lab8-Basic`](./LabX-Basic/Lab8-Basic) | Automating with CSV and JSON Data |
| Lab 10 Basic | [`LabX-Basic/Lab10-Basic`](./LabX-Basic/Lab10-Basic) | Automating Spreadsheets (Excel, openpyxl) |
| Lab 11 Basic | [`LabX-Basic/Lab11-Basic`](./LabX-Basic/Lab11-Basic) | Automating PDFs & Word Documents |

### LabX Advance
| Lab | โฟลเดอร์ | หัวข้อ |
| :--- | :--- | :--- |
| Lab AD1 Advance | [`LabX-Advance/Lab-AD1-Advance`](./LabX-Advance/Lab-AD1-Advance) | Advanced Web Scraping: Agentic Web Scraper (Selenium) |

### Mini Project
[`Mini-Project/`](./Mini-Project): ระบบแจ้งเตือนเครื่องซักผ้าร้านหยอดเหรียญ งานกลุ่ม ลิงก์: https://github.com/preemphatp/Mini_Project

### Final Project
[`Final-Project/`](./Final-Project): Virtual Pet Companion (CLI + Web) งานกลุ่ม ลิงก์: https://github.com/144P75/script_project

(งาน Lab Week 12 Final Project Development: Enhanced Task Manager CLI อยู่ใน [`Lab/Week12`](./Lab/Week12))

## หมายเหตุเกี่ยวกับโครงสร้างและงานที่ไม่ได้ย้ายมา
- **Lab Week 3 และ Week 9** ยังไม่มีไฟล์งานใน repository นี้
- **Mini Project และ Final Project** เป็นงานกลุ่มที่อยู่ใน GitHub ของกลุ่ม จึงใส่เป็นลิงก์ (ไฟล์ `.md`) ตามที่อาจารย์อนุญาต
- โฟลเดอร์ Lab ประจำสัปดาห์ใช้ชื่อ `WeekN` ส่วน LabX ใช้ชื่อ `LabN-Basic` / `Lab-AD1-Advance` เพื่อให้ตรงกับชื่อ Lab ที่อาจารย์กำหนด
- งานแต่ละชิ้นรันได้ด้วย `python main.py` ในโฟลเดอร์ของงานนั้น (งานที่ใช้ไลบรารีเพิ่มมีไฟล์ `requirements.txt` ให้ติดตั้งด้วย `pip install -r requirements.txt`)

## สิ่งที่ได้เรียนรู้จากวิชานี้

**พื้นฐานการเขียนโปรแกรมด้วย Python**
ได้เรียนโครงสร้างข้อมูล list, tuple, dictionary และ set รวมถึงการเลือกใช้ให้เหมาะกับข้อมูล เช่น ข้อมูลที่ต้องแก้ไขบ่อยใช้ list ส่วนข้อมูลที่ไม่เปลี่ยนแปลงใช้ tuple นอกจากนี้ยังได้เรียนการแบ่งโค้ดเป็น function และ module ทำให้โค้ดอ่านง่ายและนำกลับมาใช้ซ้ำได้

**การนำ Python ไปทำงานอัตโนมัติ (LabX)**
ได้ฝึกใช้ Python กับงานที่ใช้จริง ได้แก่ การดึงข้อมูลจากเว็บด้วย requests และ BeautifulSoup, การอ่านเขียนไฟล์ CSV และ JSON, การสร้างรายงานใน Excel ด้วย openpyxl, การรวมไฟล์ PDF และสร้างเอกสาร Word และการใช้ Selenium ใน Lab AD1 ให้ scraper ทำงานตามไฟล์ configuration

**การเขียนโปรแกรมเชิงวัตถุและการทำงานเป็นกลุ่ม**
ใน Mini Project และ Final Project ได้ใช้หลัก OOP แบ่งโค้ดเป็นโมดูลตามหน้าที่ และทำงานร่วมกับสมาชิกกลุ่มผ่าน GitHub ส่วน Final Project Development ใน Week 12 ได้ฝึกเขียน unit test เพื่อตรวจสอบการทำงานของโปรแกรม

**เครื่องมือและการจัดการโปรเจกต์**
ได้ใช้ virtual environment เพื่อแยกไลบรารีของแต่ละงาน ใช้ Git และ GitHub ในการส่งงาน รวมถึงการใช้ `.gitignore` เพื่อไม่ให้ไฟล์ที่ไม่จำเป็น เช่น `venv` และ `__pycache__` ถูกอัปโหลดขึ้นไปด้วย และได้ฝึกอ่านข้อความ error เพื่อหาสาเหตุของปัญหา เช่น การตรวจสอบโฟลเดอร์ที่ใช้รันโปรแกรมและการติดตั้งไลบรารีที่ขาด

## ลิงก์ GitHub เดิมของแต่ละงาน (ใช้อ้างอิง)
- Week 1-2: https://github.com/pitchayasitthipan/673380596-5_sec1__script_programming
- Lab 7 Basic: https://github.com/pitchayasitthipan/673380596-5_week7_sec1_script_programming
- Lab 8 Basic: https://github.com/pitchayasitthipan/673380596-5_week8_sec1_script_programming
- Lab 10 Basic: https://github.com/pitchayasitthipan/673380596-5_week10_sec1_script_programming
- Lab AD1 Advance: https://github.com/pitchayasitthipan/673380596-5_ad1_sec1_script_programming
- Final Project Development (Week 12): https://github.com/pitchayasitthipan/673380596-5_week12_sec1_script_programming
- Mini Project (กลุ่ม): https://github.com/preemphatp/Mini_Project
- Final Project (กลุ่ม): https://github.com/144P75/script_project
