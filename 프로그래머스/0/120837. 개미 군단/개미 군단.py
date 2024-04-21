def solution(hp):
    count = 0
    count += hp // 5 # 장군을 최대한 사용
    hp %= 5 # 장군을 사용한 후 남은 hp
    
    count += hp // 3 # 병정개미를 최대한 사용
    hp %= 3 # 병정개미를 사용한 후 남은 hp
    
    count += hp
        
    return count