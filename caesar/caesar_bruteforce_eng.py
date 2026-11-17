print("Welcome to Cesar decryptor. Want to decrypt text but don't know the shift? This script will help you!")


user_text = input("Input your text\n")


def decrypt():
    seq_input = [x for x in user_text]

    for i in range(1, 26):
        seq_output = []
        for y in seq_input:
            if y.isalpha() and y.islower():
                y = chr((ord(y) - i - 97) % 26 + 97)
                seq_output.append(y)
            elif y.isalpha() and y.isupper():
                y = chr((ord(y) - i - 65) % 26 + 65)
                seq_output.append(y)
            else:
                seq_output.append(y)

        print(i, "".join(seq_output))

print("The shifts and decrypted text are given below in sequence. Choose needed string!")
decrypt()