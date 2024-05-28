def solution(n):
    number = str(n)
    list_number = list(number)
    list_number.sort(reverse=True)
    answer = int("".join(list_number))
    return answer