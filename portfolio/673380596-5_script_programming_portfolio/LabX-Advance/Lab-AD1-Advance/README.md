# AD1 Lab Advanced: Agentic Web Scraper

ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

Scraper ที่ทำงานตามไฟล์ config (`configs/example_site_config.json`) ด้วย Selenium
ดึงรายการหนังสือจาก https://books.toscrape.com/ (เว็บสำหรับฝึก scraping) 2 หน้า แล้วบันทึกเป็น `data/scraped_products.json`

## วิธีรัน
```bash
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
pip install -r requirements.txt
python main.py
```
