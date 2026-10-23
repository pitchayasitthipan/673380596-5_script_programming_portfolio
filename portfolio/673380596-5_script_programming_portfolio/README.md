# รวมงานวิชา Script Programming (CP352301)

**ชื่อ-นามสกุล:** นส.พิชยา สิทธิพันธ์  **รหัสนักศึกษา:** 673380596-5  **Section:** 1


## โครงสร้างโฟลเดอร์

| โฟลเดอร์ | เนื้อหา |
| :--- | :--- |
| [`Lab/`](./Lab) | Lab ประจำสัปดาห์ |
| [`LabX-Basic/`](./LabX-Basic) | LabX Basic |
| [`LabX-Advance/`](./LabX-Advance) | LabX Advance |
| [`Mini-Project/`](./Mini-Project) | Mini Project: ระบบแจ้งเตือนเครื่องซักผ้าร้านหยอดเหรียญ (ลิงก์ไปยัง repository ของกลุ่ม) |
| [`Final-Project/`](./Final-Project) | Final Project: Virtual Pet Companion (ลิงก์ไปยัง repository ของกลุ่ม) |
| [`Certificate/`](./Certificate) | ภาพ certificate จาก https://www.netacad.com/ |

## รายละเอียดแต่ละโฟลเดอร์

### Lab (ประจำสัปดาห์)
| สัปดาห์ | โฟลเดอร์ | หัวข้อ |
| :--- | :--- | :--- |
| 1 | [`Lab/Week1`](./Lab/Week1) | พื้นฐาน Python |
| 2 | [`Lab/Week2`](./Lab/Week2) | Conditionals |
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

## สิ่งที่ได้เรียนรู้จากวิชานี้

**พื้นฐานการเขียนโปรแกรมด้วย Python**
ได้เรียนโครงสร้างข้อมูล list, tuple, dictionary และ set รวมถึงการเลือกใช้ให้เหมาะกับข้อมูล เช่น ข้อมูลที่ต้องแก้ไขบ่อยใช้ list ส่วนข้อมูลที่ไม่เปลี่ยนแปลงใช้ tuple นอกจากนี้ยังได้เรียนการแบ่งโค้ดเป็น function และ module ทำให้โค้ดอ่านง่ายและนำกลับมาใช้ซ้ำได้

ได้ฝึกใช้ Python กับงานที่ใช้จริง ได้แก่ การดึงข้อมูลจากเว็บด้วย requests และ BeautifulSoup, การอ่านเขียนไฟล์ CSV และ JSON, การสร้างรายงานใน Excel ด้วย openpyxl, การรวมไฟล์ PDF และสร้างเอกสาร Word และการใช้ Selenium ใน Lab AD1 ให้ scraper ทำงานตามไฟล์ configuration

**การเขียนโปรแกรมเชิงวัตถุและการทำงานเป็นกลุ่ม**
**Mini Project (ระบบแจ้งเตือนเครื่องซักผ้า)**
ได้ฝึกวางแผนและแบ่งงานเป็นขั้นตอนย่อยด้วย Kanban ในบทบาท Planner และได้ใช้ dictionary, set และ tuple ในการเก็บสถานะของเครื่องซักผ้า โปรแกรมเป็นเมนูให้ผู้ใช้เลือก และดักข้อมูลที่กรอกผิดไม่ให้โปรแกรมหยุดทำงาน ระหว่างทำมีการบันทึกการใช้ AI และการเปลี่ยนแปลงของงานไว้ด้วย
**Final Project (Virtual Pet)**
ได้ทำงานเป็นทีมแบบแบ่งเป็น Sprint และสลับบทบาทไปตามรอบ ทั้งตรวจสอบข้อผิดพลาด เขียนโค้ด และวางโครงสร้างระบบ โปรแกรมเล่นได้ทั้งบน CLI และเว็บ ใช้ข้อมูลชุดเดียวกัน มีการบันทึกข้อมูลลงไฟล์ ทดสอบอัตโนมัติ และเชื่อมต่อ API กับ AI ได้ ทำให้เข้าใจภาพรวมของการพัฒนาโปรแกรมตั้งแต่เขียนโค้ด ทดสอบ ไปจนถึงนำขึ้นเว็บจริง

## ลิงก์ GitHub เดิมของแต่ละงาน (ใช้อ้างอิง)
- Week 1-2: https://github.com/pitchayasitthipan/673380596-5_sec1__script_programming
- Lab 7 Basic: https://github.com/pitchayasitthipan/673380596-5_week7_sec1_script_programming
- Lab 8 Basic: https://github.com/pitchayasitthipan/673380596-5_week8_sec1_script_programming
- Lab 10 Basic: https://github.com/pitchayasitthipan/673380596-5_week10_sec1_script_programming
- Lab AD1 Advance: https://github.com/pitchayasitthipan/673380596-5_ad1_sec1_script_programming
- Final Project Development (Week 12): https://github.com/pitchayasitthipan/673380596-5_week12_sec1_script_programming
- Mini Project (กลุ่ม): https://github.com/preemphatp/Mini_Project
- Final Project (กลุ่ม): https://github.com/144P75/script_project
