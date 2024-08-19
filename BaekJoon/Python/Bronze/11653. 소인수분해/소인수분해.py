str_num = input()
number = int(str_num)

value = 2
list_answer = []
for x in range(number):

    if number % value == 0:
        list_answer.append(value)
        number = number / value
    else:
        value = value+1

    if number / value == 1:
        list_answer.append(value)
        break

for y in range(len(list_answer)):
    print(list_answer[y])