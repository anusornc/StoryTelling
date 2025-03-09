# เล่านิทานสำหรับเด็ก

นี่คือแอปพลิเคชันเว็บง่ายๆ ที่ให้คุณเขียนนิทานและให้มันอ่านออกเสียงสำหรับเด็กโดยใช้เทคโนโลยีแปลงข้อความเป็นเสียง

## คุณสมบัติ

- **การเลือกภาษา**: เลือกระหว่างภาษาอังกฤษและภาษาไทย
- **การเขียนนิทาน**: เขียนนิทานของคุณในพื้นที่ข้อความ
- **แปลงข้อความเป็นเสียง**: สร้างเสียงจากนิทานที่เขียนโดยใช้ Google Text-to-Speech (gTTS)
- **การเล่นเสียง**: เล่นเสียงที่สร้างขึ้นโดยตรงในเบราว์เซอร์
- **ตัวเลือกการดาวน์โหลด**: ดาวน์โหลดไฟล์เสียงที่สร้างขึ้น
- **การล้างข้อมูล**: ลบไฟล์เสียงชั่วคราว

## การติดตั้ง

1. โคลน repository:
    ```sh
    git clone https://github.com/yourusername/story-teller-for-kids.git
    cd story-teller-for-kids
    ```

2. ติดตั้ง dependencies ที่จำเป็น:
    ```sh
    pip install -r requirements.txt
    ```

## การใช้งาน

1. รันแอปพลิเคชัน Streamlit:
    ```sh
    streamlit run storytelling.py
    ```

2. เปิดเว็บเบราว์เซอร์ของคุณและไปที่ `http://localhost:8501`

3. เขียนนิทานของคุณ เลือกภาษา และคลิก "Read Story Aloud! / อ่านเรื่องราวออกเสียง!" เพื่อสร้างและเล่นเสียง

## Dependencies

- [`streamlit`](venv/lib/python3.11/site-packages/streamlit/__init__.py )
- [`gtts`](venv/lib/python3.11/site-packages/gtts/__init__.py )
- [`datetime`](/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/datetime.py )
- [`tempfile`](/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/tempfile.py )
- [`base64`](/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/base64.py )
- [`os`](/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/os.py )
- [`time`](/Users/anusornchaikaew/.vscode/extensions/ms-python.vscode-pylance-2025.3.1/dist/typeshed-fallback/stdlib/time.pyi )

## ใบอนุญาต

โปรเจคนี้ได้รับอนุญาตภายใต้ MIT License ดูไฟล์ LICENSE สำหรับรายละเอียดเพิ่มเติม

## ขอบคุณ

สร้างด้วย ❤️ สำหรับเด็กและผู้ปกครอง