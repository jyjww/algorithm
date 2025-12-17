import re
def solution(my_string):
    answer = []
    str = "".join(ch for ch in my_string if not ch.isalpha())
    for s in str:
        answer.append(int(s))
    return sorted(answer)
        