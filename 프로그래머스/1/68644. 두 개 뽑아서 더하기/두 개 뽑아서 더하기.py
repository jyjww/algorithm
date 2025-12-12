from itertools import combinations
def solution(numbers):
    s = set()
    
    for a, b in combinations(numbers, 2):
        sum = a + b
        s.add(sum)
    
    return list(sorted(s))