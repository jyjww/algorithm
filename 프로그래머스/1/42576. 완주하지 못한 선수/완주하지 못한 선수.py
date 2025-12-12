def solution(participant, completion):
    dic = {}
    
    # 참가자 카운팅
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    # 완주자 감소
    for c in completion:
        dic[c] -= 1
    
    for name, count in dic.items():
        if count > 0:
            return name
            