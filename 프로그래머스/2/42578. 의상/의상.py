def solution(clothes):
    dic = {}
    
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = []
        dic[kind].append(name)
    
    answer = 1
    for count in dic.values():
        answer *= (len(count) + 1)

    return answer - 1