def solution(rsp):
    
    ans = ''
    for l in rsp:
        if l == '2':
            ans += '0'
        elif l == '0':
            ans += '5'
        else:
            ans += '2'
    return ans