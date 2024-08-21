import math
def solution(n, m):
    gcd_value = math.gcd(n,m)
    lcm_value = int(n*m/gcd_value)
    answer = [gcd_value,lcm_value]
    return answer