def solution(order):
    string = str(order)
    num = ['3', '6', '9']
    cnt = 0
    for s in string:
        if s in num:
            cnt += 1
    return cnt