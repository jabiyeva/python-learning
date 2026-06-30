import string
import random
import pyperclip

# --- Setup ---
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
num = string.digits
char = string.punctuation

char_types = ["lowercase letters", "uppercase letters", "numbers", "special characters"]
answers = ["yes", "no"]
char_pool = [lowercase, uppercase, num, char]

# --- Ask user preferences ---
user_answer = []
for c in char_types:
    answer = input(f"Should generated password contain {c}?\n").lower()
    if answer not in answers:
        print("You have to answer questions by 'Yes' or 'No'. Password is not generated. Try again.")
        exit()
    else:
        user_answer.append(answer)

# --- Ask amount and length ---
try:
    amount = int(input("How many passwords would you like to generate?\n"))
    length = int(input("How many characters would you like to generate?\n"))
except ValueError:
    print("You have to enter an integer. Password is not generated.")
    exit()

# --- Build character pool based on preferences ---
pref_char_pool = ""
for p, c in zip(user_answer, char_pool):
    if p == answers[0]:
        pref_char_pool += c

if not pref_char_pool:
    print("You didn't choose any preference. Password is not generated.")
    exit()

# --- Generate passwords ---
pswd_list = []
for i in range(1,amount+1):
    pswd = "".join(random.choices(pref_char_pool, k=length))
    pswd_list.append(pswd)

# --- Output ---
for i, pswd in enumerate(pswd_list, 1):
    print(f"{i}: {pswd}")

# --- Ask which password to copy ---
try:
    num_chosen_pswd = int(input("\nChoose the password you want to copy: "))
    if num_chosen_pswd > amount or num_chosen_pswd <= 0:
        print(f"You have to choose a number between 1 and {amount}. Password is not generated.")
        exit()
    else:
        chosen_pswd = pswd_list[num_chosen_pswd-1]
        pyperclip.copy(chosen_pswd)
        print(f"You chose password #{num_chosen_pswd}: {chosen_pswd}. Password is copied to clipboard!")
except ValueError:
    print("You have to enter an integer. Password is not generated.")
    exit()
