def solution(my_string):
    stack = []
    
    for s in my_string:
        if s not in stack:
            stack.append(s)
    
    return "".join(stack)