def solution(lottos, win_nums):
    lucky = lottos.count(0)
    
    # 모든 로또 번호를 모를때
    
    if len(lottos) == lucky:
        return ([1, 6])
    
    count = 0
    for num in win_nums:
        if num in lottos:
            count += 1
    
    best = min(6, 7 - (count + lucky))
    worst = min(6, 7 - count)
    return [best, worst]
