print("Welcome to Cesar encryptor")

ans_encr = input("Do you want to encrypt or decrypt the text? Answer e for encryption or d for decryption\n")

def ans_encr_iscorrect():
    if ans_encr == "e" or ans_encr == "d":
        return True
    else:
        return False

while not ans_encr_iscorrect():
    ans_encr = input("Do you want to encrypt or decrypt the text? Answer e for encryption or d for decryption\n")


ans_shift = int(input("Write the shift\n"))

def answer_shift_iscorrect():
    if 0 < ans_shift <= 26:
        return True
    else:
        return False

while not answer_shift_iscorrect():
    ans_shift = int(input("Write the shift - an integer between 1 and 26\n"))

user_text = input("Input your text\n")

ans_direct = input("What the direction of the encryption? Type f for forward or b for back direction\n")

def ans_direct_iscorrect():
    if ans_direct == "b" or ans_direct == "f":
        return True
    else:
        return False

while not ans_direct_iscorrect():
    ans_direct = input("What the direction of the encryption? Type f for forward or b for back direction\n")

def encrypt_forward():
    seq_input = [x for x in user_text]
    seq_output = []
    for y in seq_input:
        if y.isalpha() and y.islower():
            y = chr(97 + (ord(y) + ans_shift - 97) % 26)
            seq_output.append(y)
        elif y.isalpha() and y.isupper():
            y = chr(65 + (ord(y) + ans_shift - 65) % 26)
            seq_output.append(y)
        else:
            seq_output.append(y)

    return "".join(seq_output)


def encrypt_backward():
    seq_input = [x for x in user_text]
    seq_output = []
    for y in seq_input:
        if y.isalpha() and y.islower():
            y = chr((ord(y) - ans_shift - 97) % 26 + 97)
            seq_output.append(y)
        elif y.isalpha() and y.isupper():
            y = chr((ord(y) - ans_shift - 65) % 26 + 65)
            seq_output.append(y)
        else:
            seq_output.append(y)

    return "".join(seq_output)


if (ans_encr == "e" and ans_direct == "f") or (ans_encr == "d" and ans_direct == "b"):
    print(encrypt_forward())
elif (ans_encr == "e" and ans_direct == "b") or (ans_encr == "d" and ans_direct == "f"):
    print(encrypt_backward())



