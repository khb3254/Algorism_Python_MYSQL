def solution(s):
    answer = ''
    list = sorted(s, reverse = True)
    
    for i in list:
        answer += i
    return answer