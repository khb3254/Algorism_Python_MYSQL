def solution(k, score):
    answer = []
    
    hall = [] # 점수 저장 리스트
    for i in score:
        if (len(hall) < k):
            hall.append(i)
        else:
            if (i > min(hall)):
                hall.remove(min(hall))
                hall.append(i)
                
        hall.sort()
        answer.append(hall[0])
        
    return answer