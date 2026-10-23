# Codecademy Core Challenge: Number Classifier

num = int(input("Enter an integer: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
elif num > 0 and num % 2 != 0:
    print("The number is positive and odd.")
elif num < 0 and num % 2 == 0:
    print("The number is negative and even.")
elif num < 0 and num % 2 != 0:
    print("The number is negative and odd.")
else:
    # กรณี num == 0
    print("The number is zero and even.")
