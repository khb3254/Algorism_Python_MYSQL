def solution(sizes):
    w, h = 0,0
    for size in sizes:
        max_size = max(size)
        min_size = min(size)
        if max_size >= h:
            h = max_size
        if min_size >= w:
            w = min_size
    return w * h 