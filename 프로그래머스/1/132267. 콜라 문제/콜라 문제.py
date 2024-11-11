def solution(a, b, n):
    answer = 0
    while n >= a:
        # 나머지를 반환
        remain_bottle = n % a
        # 마트에서 받은 콜라의 수
        n = (n//a) * b 
        answer += n
        n += remain_bottle
        
    return answer