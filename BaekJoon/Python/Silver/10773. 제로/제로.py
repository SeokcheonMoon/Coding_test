import sys

cycle = int(sys.stdin.readline())
list_value = []

for x in range(cycle):
    value = int(sys.stdin.readline())
    if value == 0:
        list_value = list_value[0:-1]
    else:
        list_value.append(value)

answer = sum(list_value)
print(answer)