print("Привет! Я могу отсортировать doi в лексикографическом порядке и удалить дубли! Скопируй список в диалоговое окно (каждая запись doi на отдельной строке) и нажми enter")
seq = []
while True:
    user_input = input()
    if user_input == "":
        break
    seq.append(user_input)

seq1 = list(set(seq))
seq1.sort()
print()
print(*seq1, sep='\n')