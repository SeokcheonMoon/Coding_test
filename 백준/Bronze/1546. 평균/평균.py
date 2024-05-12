str_count = input()
count = int(str_count)

pre_list = list(map(int,input().split()))

sum = 0
for y in range(count) :
    after_score = (pre_list[y]/max(pre_list)) * 100
    sum = sum + after_score
average = sum/count
print(average)