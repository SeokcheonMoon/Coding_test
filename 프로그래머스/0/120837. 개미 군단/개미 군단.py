def solution(hp):
    if hp % 5 == 0 :    # 5의 배수일 경우
        answer = hp // 5   # 5의 배수일 경우 몫만 추출

    elif hp % 5 != 0 :  # 5의 배수가 아닐경우

        if hp % 5 % 3 == 0: # 5로 나눈 나머지가 3의 배수일 경우
            answer = hp // 5 + hp % 5 // 3 # 5로 나눈 몫 + 5로나눈 나머지를 3으로 나눈 몫

        elif hp % 5 % 3 != 0: # 5로 나눈 나머지가 3의 배수 아닐 경우  

            if hp % 5 % 3 % 1 == 0 :
                answer = hp // 5 + hp % 5 // 3 + hp % 5 % 3 // 1
    return answer