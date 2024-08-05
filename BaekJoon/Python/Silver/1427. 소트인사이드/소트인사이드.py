str_num = input()
list_str_num = list(str_num)
list_num = []
for x in range(len(list_str_num)):
    list_num.append(list_str_num[x])
list_num.sort(reverse=True)

list_answer = []
for y in range(len(list_num)):
    list_answer.append(str(list_num[y]))
answer = "".join(list_answer)
print(answer)