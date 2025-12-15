def solution(sizes):
    
    w_max = 0
    h_max = 0
    
    for x, y in sizes:
        w = max(x, y)
        h = min(x, y)
        w_max = max(w_max, w)
        h_max = max(h_max, h)
    return w_max * h_max