def solution(s):
    stack = []

    for st in s.split(" "):
        if not stack and st == "Z":
            continue
        elif st == "Z":
            stack.pop()
        else:
            stack.append(st)
    
    nums = [int(ch) for ch in stack]
    return sum(nums)