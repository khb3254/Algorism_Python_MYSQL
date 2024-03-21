def solution(n):
    if n >= 1 and n <= 100:
        answer = 0
        a, b = divmod(n, 7)
        if n % 7 == 0:
            answer += a
        else:
            answer += a + 1
    return answer
        