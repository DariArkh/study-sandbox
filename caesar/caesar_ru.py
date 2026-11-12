print("Добро пожаловать в шифровальщик Цезаря")

ans_encr = input("Вы хотите зашифровать или дешифровать текст? Напечатайте ш для шифрования или д для дешифровки\n")

def ans_encr_iscorrect():
    if ans_encr == "ш" or ans_encr == "д":
        return True
    else:
        return False

while not ans_encr_iscorrect():
    ans_encr = input("Вы хотите зашифровать или дешифровать текст? Напечатайте ш для шифрования или д для дешифровки и нажмите enter\n")


ans_shift = int(input("Напишите шаг шифрования\n"))

def answer_shift_iscorrect():
    if 0 < ans_shift <= 26:
        return True
    else:
        return False

while not answer_shift_iscorrect():
    ans_shift = int(input("Напишите шаг шифрования - целое число между 1 и 26 и нажмите enter\n"))

user_text = input("Введите свой текст\n")

ans_direct = input("Какое направление шифрования? Напечатайте в для сдвига вперед или н для сдвига назад и нажмите enter\n")

def ans_direct_iscorrect():
    if ans_direct == "н" or ans_direct == "в":
        return True
    else:
        return False

while not ans_direct_iscorrect():
    ans_direct = input("Какое направление шифрования? Напечатайте в для сдвига вперед или н для сдвига назад и нажмите enter\n")

def encrypt_forward():
    seq_input = [x for x in user_text]
    seq_output = []
    for y in seq_input:
        if y.isalpha() and y.islower():
            y = chr(1072 + (ord(y) + ans_shift - 1072) % 32)
            seq_output.append(y)
        elif y.isalpha() and y.isupper():
            y = chr(1040 + (ord(y) + ans_shift - 1040) % 32)
            seq_output.append(y)
        else:
            seq_output.append(y)

    return "".join(seq_output)


def encrypt_backward():
    seq_input = [x for x in user_text]
    seq_output = []
    for y in seq_input:
        if y.isalpha() and y.islower():
            y = chr((ord(y) - ans_shift - 1072) % 32 + 1072)
            seq_output.append(y)
        elif y.isalpha() and y.isupper():
            y = chr((ord(y) - ans_shift - 1040) % 32 + 1040)
            seq_output.append(y)
        else:
            seq_output.append(y)

    return "".join(seq_output)


if (ans_encr == "ш" and ans_direct == "в") or (ans_encr == "д" and ans_direct == "н"):
    print(encrypt_forward())
elif (ans_encr == "ш" and ans_direct == "н") or (ans_encr == "д" and ans_direct == "в"):
    print(encrypt_backward())



