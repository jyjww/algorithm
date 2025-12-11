def solution(s):
    stack = []
    
    for ch in s:
        # 스택이 비어있을 때
        if not stack:
            stack.append(ch)
            continue
        
        # 괄호 짝이 맞을 때 스택에서 팝
        if stack[-1] == "(" and ch == ")":
            stack.pop()
        else:
            stack.append(ch)
            
    if stack:
        return False
    else: 
        return True