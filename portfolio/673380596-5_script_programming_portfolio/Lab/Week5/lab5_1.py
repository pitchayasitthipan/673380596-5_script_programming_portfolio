# lab5_1.py
# Lab 5.1: Simple Contact Book Manager (Dictionary)
# ชื่อ: นส.พิชยา สิทธิพันธ์  รหัสนักศึกษา: 673380596-5  sec.1

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add/Update Contact")
    print("2. View Contact Details")
    print("3. List All Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        # ใช้ .title() ให้ชื่อเป็นแบบเดียวกันเสมอ (case-insensitive)
        name = input("Enter name: ").strip().title()
        if name == "":
            print("Name cannot be empty")
        else:
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            if name in contacts:
                print("Updated", name)
            else:
                print("Added", name)
            contacts[name] = {"phone": phone, "email": email}

    elif choice == "2":
        name = input("Enter name to view: ").strip().title()
        details = contacts.get(name)
        if details is None:
            print("Contact not found.")
        else:
            print(name, "->", details)

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts yet")
        else:
            for name, details in contacts.items():
                print(name, ":", details)

    elif choice == "4":
        name = input("Enter name to delete: ").strip().title()
        if name in contacts:
            contacts.pop(name)
            print("Deleted", name)
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Please choose 1-5")
