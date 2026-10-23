# lab5_2.py
# Lab 5.2: Course Enrollment & Collaboration (Set)
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

python_students = {"S001", "S003", "S005", "S007", "S009"}
java_students = {"S002", "S003", "S006", "S007", "S010"}

# นักเรียนที่เรียนทั้งสองวิชา
both = python_students.intersection(java_students)
print("Students in both courses:", sorted(both))

# นักเรียนทั้งหมด (ไม่ซ้ำ)
all_students = python_students.union(java_students)
print("All unique students:", sorted(all_students))

# เรียน Python อย่างเดียว
only_python = python_students.difference(java_students)
print("Only in Python:", sorted(only_python))

# เรียนแค่วิชาเดียว (ไม่ได้เรียนทั้งคู่)
only_one = python_students.symmetric_difference(java_students)
print("Only in one course:", sorted(only_one))

# ลบค่าซ้ำออกจาก list
all_students_list = ["S001", "S003", "S005", "S001", "S002"]
unique_list = list(set(all_students_list))
print("Original list:", all_students_list)
print("Unique list:", unique_list)
