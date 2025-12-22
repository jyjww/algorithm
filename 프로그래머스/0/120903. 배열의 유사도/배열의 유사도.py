def solution(s1, s2):
    answer = 0
    
    for st in s2:
        if st in s1:
            answer += 1
    return answer