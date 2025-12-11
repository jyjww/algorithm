def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range (len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    
    # 끝까지 갔는데도 스택에 남아있는것 처리 
    # -> 한번도 가격이 떨어지지 않음 = 마지막 인덱스
    n = len(prices)
    while stack:
        top = stack.pop()
        answer[top] = (n-1) - top
    return answer