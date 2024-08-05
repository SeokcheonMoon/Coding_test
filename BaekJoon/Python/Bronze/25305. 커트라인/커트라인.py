total, prized = map(int, input().split())
list_score = list(map(int,input().split()))

list_score.sort(reverse=True)
print(list_score[prized-1])