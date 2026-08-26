print("Привет, это генератор паролей!")
length = int(input("Какой длины нужен пароль? "))


def is_valid(l):   #проверка длины пароля
    if l < 8:
        return False
    else:
        return True
        

while not is_valid(length):
    print("Безопасным считается пароль, в котором не менее 8 символов")
    length = int(input("Какой длины нужен пароль? "))


import random

def is_strong(passw):   #проверка соответствия пароля правилам
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    for c in passw:
        if c in "0123456789":
            flag1 = True
    for c in passw:
        if c in "abcdefghijklmnopqrstuvwxyz":
            flag2 = True
    for c in passw:
        if c in "abcdefghijklmnopqrstuvwxyz".upper():
            flag3 = True
    for c in passw:
        if c in "!@#$%&*()//":
            flag4 = True
    if flag1 and flag2 and flag3 and flag4:
        return True
    else:
        return False 

def password_generator():    #генератор паролей
    letters = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    digits = "0123456789"
    punctuation = "!@#$%&*()//"
    passw = "".join(random.choice(letters + digits + punctuation) for _ in range(length))
    return passw

passw = password_generator()

while not is_strong(passw):   #генерация пароля пока он не будет соответствовать правилам
    passw = password_generator()    
    
print(passw)


