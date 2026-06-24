# 🔍 Text Analyzer

A beginner Python program that analyzes a string based on user input.

## 📋 What it does

- Asks the user to enter a short text
- Cleans and formats the input automatically
- Analyzes important details such as word count and character length
- Detects whether the text contains digits
- Picks a random word from the text
- Displays a neatly formatted analysis report

## 🧠 Concepts used

| Concept | Details |
|---|---|
| Input & Output | `input()`, `print()`, f-strings |
| String methods | `strip()`, `upper()`, `split()` |
| `string` module | `digits` for digit detection |
| `random` module | `choice()` for random word selection |
| Loop | `for` loop to check each character |
| Alignment | f-string `:<16` formatting |

## ▶️ How to run

1. No installation needed — only built-in modules used
2. Run the script: python text_analyzer.py

## 📁 Files

| File | Description |
|---|---|
| `text_analyzer.py` | Main script |
| `README.md` | Project documentation |

## 📊 Example output

=== Text Analysis Report ===

Original text:   Hello World, this is Python!

Cleaned text:    Hello World, this is Python!

Uppercase:       HELLO WORLD, THIS IS PYTHON!

Word count:      5

Character count: 27

Words:           ['Hello', 'World,', 'this', 'is', 'Python!']

Contains Digits: No

Random word:     this
