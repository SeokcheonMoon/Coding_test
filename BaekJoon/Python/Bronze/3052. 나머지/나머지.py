list_number = []

for x in range(10) :
    str_number = input()
    number = int(str_number)
    
    result = number % 42    # result는 number를 42로 나누고 난 후의 나머지
    list_number.append(result)          # list 에 숫자가 다 담김

sorted_list = sorted(list_number)
# print(sorted_list)

answer = 1
for y in [0,1,2,3,4,5,6,7,8,9] :
    if y == 9 :
        break
    elif sorted_list[y] == sorted_list[y+1] :
        answer = answer + 0
    else :
        answer = answer + 1

print(answer)