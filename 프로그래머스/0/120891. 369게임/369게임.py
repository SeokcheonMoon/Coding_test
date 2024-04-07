def solution(order):
    str_order = str(order)
    list_order = list(map(int,str_order))

    answer = list_order.count(3)+list_order.count(6)+list_order.count(9)
    return answer