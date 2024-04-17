def solution(money):
    answer = []
    a, b = divmod(money, 5500)
    answer.append(a)
    answer.append(b)
    return answer