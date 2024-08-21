def solution(A,B):
    A.sort(reverse=True)
    B.sort(reverse=False)

    answer = 0
    for x in range(len(A)):
        answer = answer + A[x]*B[x]

    return answer