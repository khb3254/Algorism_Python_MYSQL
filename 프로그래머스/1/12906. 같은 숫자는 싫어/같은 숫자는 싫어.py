def solution(arr):
    answer = []
    for idx, item in enumerate(arr):
        if idx == 0 or item != arr[idx-1]:
            answer.append(item)
    return answer