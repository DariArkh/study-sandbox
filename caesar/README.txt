# Caesar cipher

A simple CLI script to encrypt or decrypt the user's text. The user chooses
the shift, the direction (encryption or decryption), and enters the text.

Two versions are included, identical in logic and differing only in the alphabet
and interface language:

- `caesar_eng.py` — English alphabet
- `caesar_ru.py` — Russian alphabet

## Language

- Python

## Skills

- Functions (`def`)
- `while` loop
- Conditional statements (`if/elif/else`)
- User input handling and validation
- String methods and character arithmetic (alphabet wrap-around)

## Features

- Encrypts and decrypts text with a user-defined shift
- Supports forward and backward shift direction
- Re-asks for input if the user enters an invalid value
- Preserves letter case
- Leaves spaces and punctuation untouched
- Wraps around the alphabet (z → a, я → а)

## Limitations

- Each version works with one alphabet only (English or Russian)
- Letters outside the chosen alphabet are passed through unchanged
- Mixed-language text will be partially encrypted

## How to run

```bash
python caesar_eng.py
or
python caesar_ru.py

## Example

Welcome to Cesar encryptor
Do you want to encrypt or decrypt the text? Answer e for encryption or d for decryption
e
Write the shift
5
Input your text
Hello
What the direction of the encryption? Type f for forward or b for back direction
f
Mjqqt