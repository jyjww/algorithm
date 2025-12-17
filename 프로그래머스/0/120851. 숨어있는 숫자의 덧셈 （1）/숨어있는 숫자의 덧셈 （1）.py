def solution(my_string):
    num = sum((int(n) for n in my_string if n.isdigit()))
    return num