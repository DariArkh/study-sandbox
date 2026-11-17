print("Добро пожаловать в дешифровальщик Цезаря. Вы хотите дешифровать текст, но не знаете размер сдвиг? Этот скрипт вам поможет!")


user_text = input("Введите свой текст\n")


def decrypt():
    seq_input = [x for x in user_text]

    for i in range(1, 32):
        seq_output = []
        for y in seq_input:
            if y.isalpha() and y.islower():
                y = chr((ord(y) - i - 1072) % 32 + 1072)
                seq_output.append(y)
            elif y.isalpha() and y.isupper():
                y = chr((ord(y) - i - 1040) % 32 + 1040)
                seq_output.append(y)
            else:
                seq_output.append(y)

        print(i, "".join(seq_output))

print("Ниже последовательно приведены сдвиги и дешифрованный текст. Выбери нужную строку!")
decrypt()