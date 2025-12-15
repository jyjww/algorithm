from functools import cmp_to_key
def solution(n):
    N = []
    for ch in str(n):
        N.append(ch)
    
    def cmp(x, y):
        if x+y>y+x:
            return -1
        if x+y<y+x:
            return 1
        return 0
    
    N.sort(key=cmp_to_key(cmp))

    ans = ''
    for num in N:
        ans += num
    return int(ans)
    