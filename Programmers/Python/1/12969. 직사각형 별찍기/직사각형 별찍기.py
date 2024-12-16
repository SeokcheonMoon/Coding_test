n,m = input().split()
n = int(n)
m = int(m)
for b in range(m):
    list_x = []
    for a in range(n):
        list_x.append("*")
    answer = "".join(list_x)
    print(answer)