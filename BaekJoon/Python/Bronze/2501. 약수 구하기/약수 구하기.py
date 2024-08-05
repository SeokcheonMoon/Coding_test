str_first, str_second = input().split()
first = int(str_first)
second = int(str_second)

list_value = []
for x in range(1,first+1):
    if first % x == 0:
        list_value.append(x)

if len(list_value) < second:
    print(0)
else:
    print(list_value[second-1])