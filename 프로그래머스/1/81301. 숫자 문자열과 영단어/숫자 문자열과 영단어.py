def solution(s):
    try:
        s = s.replace("zero","0")
    except:
        pass
    try:
        s = s.replace("one","1")
    except:
        pass
    try:
        s = s.replace("two","2")
    except:
        pass
    try:
        s = s.replace("three","3")
    except:
        pass
    try:
        s = s.replace("four","4")
    except:
        pass
    try:
        s = s.replace("five","5")
    except:
        pass
    try:
        s = s.replace("six","6")
    except:
        pass
    try:
        s = s.replace("seven","7")
    except:
        pass
    try:
        s = s.replace("eight","8")
    except:
        pass
    try:
        s = s.replace("nine","9")
    except:
        pass
    answer = int(s)
    return answer