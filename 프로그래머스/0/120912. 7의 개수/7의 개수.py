def solution(array):
    cnt = 0
    for a in array:
        cnt += str(a).count("7")
    return cnt