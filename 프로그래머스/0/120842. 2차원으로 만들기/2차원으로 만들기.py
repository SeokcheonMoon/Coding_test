def solution(num_list, n):
    list_split = []
    k = 0

    for x in range(int(len(num_list)/n)):

        list_split.append(num_list[k:k+n])
        k = k + n
    answer = list_split
    return answer