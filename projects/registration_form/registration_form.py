import random
import string
import pyperclip

kleinbuchstaben = string.ascii_lowercase
grossbuchstaben = string.ascii_uppercase
zahlen = string.digits
zeichen = string.punctuation
zeichenpool = kleinbuchstaben + grossbuchstaben + zahlen + zeichen


firstname = input("Enter your first name: ").strip().title()
lastname = input("Enter your last name: ").strip().title()
age = int(input("Enter your age: "))
rd_numbers = random.choices(zahlen, k=4)
rd_numbers_sampled = "".join(rd_numbers)

username = f"{firstname[:3]}{lastname[:3]}{rd_numbers_sampled}".lower()
raw_passwd = random.choices(zeichenpool, k=10)
passwd = "".join(raw_passwd)
pyperclip.copy(passwd)


print("\n=== Registration Summary ===")
print(f"{'Name':<10} {firstname} {lastname}")
print(f"{'Age':<10} {age}")
print(f"{'Username:':<10} {username}")
print(f"{'Password':<10} {passwd}")
