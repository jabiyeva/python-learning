# 🔑 Custom Password Generator

A Python program that generates multiple secure passwords based on user preferences, and lets the user copy a chosen one to the clipboard.

## 📋 What it does

- Asks the user which character types to include (lowercase, uppercase, numbers, special characters)
- Asks how many passwords to generate and how long each should be
- Validates all user input (yes/no answers and number inputs)
- Generates the requested passwords and prints them numbered
- Lets the user choose one password by number
- Copies the chosen password to the clipboard

## 🧠 Concepts used

| Concept | Details |
|---|---|
| Input & Output | `input()`, `print()`, f-strings |
| `string` module | Character sets (lowercase, uppercase, digits, punctuation) |
| `random` module | `random.choices()` for password generation |
| Lists | Storing preferences, character pools, and generated passwords |
| `zip()` | Pairing preferences with their matching character sets |
| `enumerate()` | Numbering the printed passwords |
| Exception handling | `try` / `except ValueError` for safe number input |
| Input validation | Checking yes/no answers and valid number ranges |
| `pyperclip` | Copying the chosen password to the clipboard |

## ▶️ How to run

1. Install the required library:

   ```
   pip install pyperclip
   ```

2. Open a terminal (or use the integrated terminal in VS Code)
3. Navigate to the project folder:

   ```
   cd path/to/password_generator
   ```

4. Run the script:

   ```
   python password_generator.py
   ```

## 📁 Files

| File | Description |
|---|---|
| `password_generator.py` | Main script |
| `README.md` | Project documentation |

## 📊 Example output

```
Should generated password contain lowercase letters?
yes
Should generated password contain uppercase letters?
yes
Should generated password contain numbers?
yes
Should generated password contain special characters?
no
How many passwords would you like to generate?
3
How many characters would you like to generate?
10

1: aB3dEfGh2K
2: ZqW8eRtY1u
3: pL9oI3uYtR

Choose the password you want to copy: 2
You chose password #2: ZqW8eRtY1u. Password is copied to clipboard!
```
