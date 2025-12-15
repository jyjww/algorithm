def solution(s):
    S = sorted(str(s), reverse=True)
    return "".join(S)