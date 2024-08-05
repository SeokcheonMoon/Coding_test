num_count = input()

list_value = input().split()
list_new_value = []
for x in range(len(list_value)):
    list_new_value.append(int(list_value[x]))

answer = []
for y in range(len(list_new_value)):
    list_answer = []
    for z in range(1,list_new_value[y]):
        if list_new_value[y] % z == 0:
            list_answer.append(list_new_value[y])
    if len(list_answer) == 1:
        answer.append(list_new_value[y])
print(len(answer))