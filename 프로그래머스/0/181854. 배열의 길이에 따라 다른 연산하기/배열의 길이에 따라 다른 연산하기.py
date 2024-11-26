def solution(arr, n):
    if len(arr) % 2 == 1:
        arr = [x+ n if i % 2 == 0 else x for i,x  in enumerate(arr)]
    else:
        arr=[x+ n if i % 2 == 1 else x for i,x  in enumerate(arr)]
    return arr