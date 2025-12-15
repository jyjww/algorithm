import string
def solution(age):
    dic = {i: ch for i, ch in enumerate(string.ascii_lowercase)}
    
    answer = ''
    for ch in str(age):
        answer += dic[int(ch)]
    return answer