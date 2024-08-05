str_m = input()
str_n = input()
num_m = int(str_m)
num_n = int(str_n)

list_answer = []
for x in range(num_m, num_n+1):
    list_value =[]
    for y in range(1,x):
        if x % y == 0:
            list_value.append(y)
    if len(list_value) == 1:
        list_answer.append(x)

if sum(list_answer) == 0:
    print(-1)
else:
    print(sum(list_answer))
    print(min(list_answer))