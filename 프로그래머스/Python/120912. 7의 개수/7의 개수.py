def solution(array):
    split_array = []
    for x in range(len(array)):
        split_array.append(str(array[x]))

    join_array = "".join(split_array)
    list_array = list(map(int,join_array))
    answer = list_array.count(7)
    return answer