def solution(citations):
    citations.sort()
    n = len(citations)
    ans = 0
    
    for i in range(n):
        h = min(citations[i], n-i)
        ans = max(ans, h)
    return ans