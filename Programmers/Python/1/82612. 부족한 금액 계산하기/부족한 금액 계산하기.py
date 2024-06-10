def solution(price, money, count):
    list_price = []
    for x in range(1,count+1) : 
        list_price.append(x*price)
    answer = sum(list_price)-money
    if answer < 0 : 
        answer = 0

    return answer