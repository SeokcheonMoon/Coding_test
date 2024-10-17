import math

def solution(arr):
    gcd_value = math.gcd(arr[1],arr[0])
    lcm_value = int(arr[1]*arr[0]/gcd_value)
    for x in range(2,len(arr)):
        gcd_value = math.gcd(arr[x],lcm_value)
        lcm_value = int(arr[x]*lcm_value/gcd_value)
        
    answer = lcm_value
    return answer