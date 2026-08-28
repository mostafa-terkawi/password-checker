password = input("Enter a password: ")

if len(password) < 8:
    print("Weak password! It should be at least 8 characters.")
else:
    print("Strong password length!")
