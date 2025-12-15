
def solution(emergency):
    rank = {v: i+1 for i, v in enumerate(sorted(emergency, reverse=True))}
    answer = [rank[v] for v in emergency]
    
    return answer