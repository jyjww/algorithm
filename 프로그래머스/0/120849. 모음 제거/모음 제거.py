def solution(my_string):
    answer = ['a', 'e', 'i', 'o', 'u']
    str = ''
    
    for s in my_string:
        if s not in answer:
            str += s
    return str