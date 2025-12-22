def solution(n):
    answer = 0
    
    numbers = list(map(int, str(n)))
    
    for num in numbers:
        answer += num
    
    return answer