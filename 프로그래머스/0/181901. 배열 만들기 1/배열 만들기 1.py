def solution(n, k):
    answer = []
    for i in range(1,1000000):
        if i * k <= n:
            answer.append(i * k)
    return answer