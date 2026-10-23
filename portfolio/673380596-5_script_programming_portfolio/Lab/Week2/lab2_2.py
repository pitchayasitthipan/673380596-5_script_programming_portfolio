age = int(input("Enter your age: "))

if age < 5:
    print("You're too young for movies! Enjoy cartoons.")
elif 5 <= age <= 12:
    print("G-rated or PG-rated movies are recommended.")
elif 13 <= age <= 17:
    print("PG-13 or R-rated (with parental guidance).")
else:
    print("Any movie rating is suitable.")
    action = input("Do you like action movies? (yes/no): ").strip().lower()
    if action == "yes":
        print("You might enjoy the latest action blockbuster!")

        
