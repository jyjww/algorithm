def solution(numbers):
    s = sorted(numbers)
    
    sum_num = 0
    for i in range (1, 10):
        sum_num += i
    
    result = sum_num - sum(s)
    
    return result