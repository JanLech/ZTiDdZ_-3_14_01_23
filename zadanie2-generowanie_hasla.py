import random
import string
def generate_password():
    # wygenerowanie hasła o długości 8 znaków
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    # sprawdzanie czy hasło posiada przynajmniej jedną dużą literę, jedną małą, jedną cyfrę oraz jeden znak specjalny
    if (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
        return password
    else:
        return generate_password()
# test funkcji
print(generate_password())