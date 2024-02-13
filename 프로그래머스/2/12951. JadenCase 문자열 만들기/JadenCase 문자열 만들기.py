def solution(s):
    answer = []
    words = s.split(" ")
    for i in words:
        if i:
            answer.append(i[0].upper() + i[1:].lower())
        else:
            answer.append(i)
    return " ".join(answer)