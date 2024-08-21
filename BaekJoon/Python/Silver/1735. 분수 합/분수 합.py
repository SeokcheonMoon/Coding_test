import math

top_a, bottom_a = map(int, input().split())
top_b, bottom_b = map(int, input().split())

if top_a <= 30000 and top_b <= 30000 and bottom_a <= 30000 and bottom_b <= 30000:
    # 분수 덧셈: (top_a/bottom_a) + (top_b/bottom_b)
    top = top_a * bottom_b + top_b * bottom_a
    bottom = bottom_a * bottom_b

    # GCD 계산
    gcd_value = math.gcd(top, bottom)

    # 기약분수로 나누기
    top_answer = top // gcd_value
    bottom_answer = bottom // gcd_value

    print(f"{top_answer} {bottom_answer}")