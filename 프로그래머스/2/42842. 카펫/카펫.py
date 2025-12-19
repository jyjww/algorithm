def solution(brown, yellow):
    sqr = brown + yellow
    check = []
    for i in range(1, sqr//2 + 1):
        if sqr % i == 0:
            if sqr // i > i:
                check.append([sqr//i, i])
            else:
                check.append([i, sqr//i])
                
    chk = []
    for w, h in check:
        if w>=h and (w, h) not in chk:
            if (w-2)*(h-2) == yellow:
                chk.append((w, h))
    return chk[0]
    