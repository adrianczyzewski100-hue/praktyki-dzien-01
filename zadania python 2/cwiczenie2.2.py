def validate_password(password):
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

password = input("Wprowadź hasło: ")
if validate_password(password):
    print("Hasło jest poprawne.")
else:
    print("Hasło jest niepoprawne.")