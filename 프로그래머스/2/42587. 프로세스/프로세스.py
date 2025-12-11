from collections import deque
def solution(priorities, location):
    queue = deque()
    for i, v in enumerate(priorities):
        queue.append((v, i))
        
    cnt = 0
    
    while queue:
        value, idx = queue.popleft()
        
        if any(value < q[0] for q in queue):
            queue.append((value, idx))
        else:
            cnt += 1
            if idx == location :
                return cnt