def solution(box, n):
    answer = 0 
    for i in range(len(box)):
        if i == 0:
            answer += (box[i] // n)
        elif i == 1:
            answer *= (box[i] // n)
        if i == 2:
            answer *= (box[i] // n)
    return answer