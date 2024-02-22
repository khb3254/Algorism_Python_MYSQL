def solution(s):
    # 이진 변환 횟수와 제거된 0의 총 개수를 저장
    answer = []
    # 이진 변환 횟수를 세는 변수
    count_bin = 0
    # 제거된 0의 개수를 세는 변수
    count_zero = 0
    
    # 입력된 문자열 s가 1이 아닐때까지 루프 실행
    while s != '1':
        # 모든 0을 제거
        
        count_zero += s.count("0")
        s = s.replace("0", "")
        
        len_value = len(s)
        
        # 진법 변환
        s = bin(len_value)[2:]
        count_bin += 1
        
    answer.append(count_bin)
    answer.append(count_zero)
    return answer