def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if not answer:  # answer 리스트가 비어 있으면 -1을 반환
        return [-1]
    
    answer.sort()
    return answer