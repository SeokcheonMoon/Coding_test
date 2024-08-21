alphabet_N, alphabet_M = map(int,input().split())

list_a = []
for x in range(alphabet_N):
    list_a.append(list(map(int, input().split())))

list_b = []
for y in range(alphabet_N):
    list_b.append(list(map(int, input().split())))

list_answer = []
for z in range(alphabet_N):
    list_value = []
    for a in range(alphabet_M):
        list_value.append(list_a[z][a]+list_b[z][a])
    list_answer.append(list_value)

for cycle in range(len(list_answer)):
    answer = list_answer[cycle]
    output = ' '.join(map(str, answer))
    print(output)