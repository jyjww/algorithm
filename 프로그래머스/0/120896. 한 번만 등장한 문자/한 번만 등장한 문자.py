def solution(s):
    dic = {}
    
    for ch in s:
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1
    
    ans = ''
    min_val = min(dic.values())
    answer = [k for k, v in dic.items() if v == min_val]
    return "".join(sorted(answer))
    
    