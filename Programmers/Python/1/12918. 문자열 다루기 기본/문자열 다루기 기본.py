def solution(s):
    try :
        if (len(s) == 4 or len(s) == 6) and  bool(list(map(int,s))) == True :
            answer = True
        else : 
            answer = False
    except : 
        answer = False

    return answer