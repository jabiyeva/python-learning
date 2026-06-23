# 🔐 User Registration Form

A beginner Python project that generates a username and secure password based on user input.

## 📋 What it does

- Asks the user for first name, last name, and age
- Cleans and formats the input automatically
- Generates a unique username (name initials + 4 random digits)
- Generates a random 10-character password using letters, digits, and special characters
- Copies the password to the clipboard automatically

## 🧠 Concepts used

| Concept | Details |
|---|---|
| Input & Output | `input()`, `print()`, f-strings |
| String methods | `strip()`, `title()`, `lower()` |
| `string` module | Character sets (letters, digits, punctuation) |
| `random` module | `sample()` and `choices()` |
| List to string | `"".join()` |
| Clipboard | `pyperclip` |

## ▶️ How to run

1. Install the required library: pip install pyperclip
2. Run the script: python registration_form.py

## 📁 Files

| File | Description |
|---|---|
| `registration_form.py` | Main script |
| `README.md` | Project documentation |
