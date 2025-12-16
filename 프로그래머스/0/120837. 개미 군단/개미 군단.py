def solution(hp):
    a = [5, 3, 1]
    i = 0
    
    cnt = 0
    while hp != 0:
        multiply = hp // a[i]
        hp -= a[i]*multiply
        cnt += multiply
        i += 1
    return cnt