# activity5_2.py
# Activity 5.2: Word Frequency Counter (Dictionary)
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()

word_counts = {}

for word in words:
    # ตัดเครื่องหมายวรรคตอนที่ติดหน้า/หลังคำออก (Challenge)
    word = word.strip('.,!?"\'')
    if word == "":
        continue
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
