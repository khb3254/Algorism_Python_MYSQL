def solution(sides):
    sides.sort() # 오름차순으로 정렬
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2
        
    