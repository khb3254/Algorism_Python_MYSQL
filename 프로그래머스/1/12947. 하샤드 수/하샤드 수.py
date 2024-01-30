def solution(x):
    a = [int(a) for a in str(x)]
    if x % sum(a) == 0:
        return True
    else:
        return False