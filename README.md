Repository นี้จัดทำขึ้นเพื่อส่งการบ้านหัวข้อ Software Testing โดยมีวัตถุประสงค์เพื่อทดสอบฟังก์ชันอัลกอริทึมจากโจทย์ HackerRank จำนวน 5 ข้อ [cite: 196, 198, 199, 201, 202] โดยยึดหลักการเขียนโปรแกรมและทดสอบตามเกณฑ์มาตรฐานดังนี้:

**Separation of Concerns:** 
แยก Production code (`src/`) ออกจาก Test code (`tests/`) อย่างชัดเจน 
**Test Design:** 
ออกแบบ Test case อย่างเหมาะสมและมีความหลากหลาย โดยใช้รูปแบบ Arrange-Act-Assert (AAA)
**100% Code Coverage:** 
เขียนชุดทดสอบครอบคลุมทุกบรรทัดของโค้ดที่ทำงานจริง
**Extra Credit (Stub):** 
มีการประยุกต์ใช้ Test Double ประเภท Stub (`StubStringProvider`) เพื่อจำลองข้อมูล (Indirect input) จากระบบภายนอก

## โครงสร้างโฟลเดอร์ (Project Structure)
UnitTestHw/
├── src/
│   └── challenges.py        # Production code (HackerRank logic & Service classes)
├── tests/
│   └── test_challenges.py   # Test code (Unit tests & Stub implementation)
└── README.md
## 
6810110098 ณัฐพัชร์ ปิยกาญจน์