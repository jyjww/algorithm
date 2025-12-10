def solution(sides):
    sum_sides = sum(sides) - max(sides)
    
    if sum_sides > max(sides):
        return 1
    else:
        return 2