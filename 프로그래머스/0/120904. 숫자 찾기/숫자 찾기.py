def solution(num, k):
    
    string = list(map(int, str(num)))
    
    if k in string:
        return string.index(k) + 1
    else:
        return -1