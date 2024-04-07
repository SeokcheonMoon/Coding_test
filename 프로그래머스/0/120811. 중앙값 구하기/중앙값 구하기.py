def solution(array):
    array.sort(reverse = False)
    center_index = len(array)//2 + 1
    answer = array[center_index-1]
    return answer