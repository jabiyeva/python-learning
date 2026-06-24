import string
import random


text = input("Please enter any sentence or a short text: ")
text_cleaned = text.strip()
text_upper = text_cleaned.upper()

words = text_cleaned.split()

word_count = len(words)
char_count = len(text_cleaned)

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

rd_word = random.choice(words)

contains_digits = "No"
for char in text_cleaned:
        if char.isdigit():
            contains_digits = "Yes"
            break

print("\n=== Text Analysis Report ===")
print(f"{'Original text:':<16} {text}")
print(f"{'Cleaned text:':<16} {text_cleaned}")
print(f"{'Uppercase:':<16} {text_upper}")
print(f"{'Word count:':<16} {word_count}")
print(f"{'Character count:':<16} {char_count}")
print(f"{'Words:':<16} {words}")
print(f"{'Contains Digits:':<16} {contains_digits}")
print(f"{'Random word:':<16} {rd_word}")
