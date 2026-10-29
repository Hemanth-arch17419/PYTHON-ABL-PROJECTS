#Password Validation
password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch in "!@#$%^&*":
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Password is valid")
else:
    print("Password is invalid")

    if len(password) < 8:
        print("Use at least 8 characters")
    if not upper:
        print("Include an uppercase letter")
    if not lower:
        print("Include a lowercase letter")
    if not digit:
        print("Include a number")
    if not special:
        print("Include a special character")