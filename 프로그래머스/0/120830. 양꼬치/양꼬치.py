def solution(n, k):
    answer = n * 12000 + k * 2000
    if n // 10 > 0: # 수정해야하는 부분
        return answer - (n // 10) * 2000
    
    return answer