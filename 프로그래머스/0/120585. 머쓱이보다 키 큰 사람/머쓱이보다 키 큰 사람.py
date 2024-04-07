def solution(array, height):
    sum = 0
    for x in range(len(array)) :
        if array[x-1] < height :
            sum = sum + 0
        elif array[x-1] > height :
            sum = sum + 1
    return sum