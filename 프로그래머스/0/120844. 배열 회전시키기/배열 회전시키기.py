from collections import deque
def solution(numbers, direction):
    num = deque(numbers)
    
    if direction == "right":
        num.rotate(1)
    else:
        n = num.popleft()
        num.append(n)
    return list(num)