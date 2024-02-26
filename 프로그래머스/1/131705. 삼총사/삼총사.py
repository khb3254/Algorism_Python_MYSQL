def solution(number):
    answer = 0
    len_number = len(number)
    for i in range(len_number):
        for x in range(i+1, len_number):
            for y in range(x+1, len_number):
                if number[i]+number[x]+number[y] == 0:
                    answer += 1
    return answer