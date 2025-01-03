import sys

cycle = int(sys.stdin.readline())

list_answer = []
for x in range(cycle):
    value = int(sys.stdin.readline())
    list_answer.append(value)
list_answer.sort()
for y in range(cycle):
    print(list_answer[y])