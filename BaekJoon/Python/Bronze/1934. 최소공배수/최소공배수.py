import math

cycle = int(input())
for x in range(cycle):
    a,b = map(int,input().split())
    gcd_value = math.gcd(a,b)
    answer = int(a*b/gcd_value)
    print(answer)