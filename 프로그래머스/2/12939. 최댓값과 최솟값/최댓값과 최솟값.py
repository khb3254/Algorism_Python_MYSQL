def solution(s):
    answer = []
    s = s.split()
    
    for i in s:
        answer.append(int(i))
    min_max = "{} {}".format(min(answer), max(answer))
    return min_max