def solution(n):
    ans = 1
    for i in range(1, 11):
        ans *= i
        if ans == n:
            return i
        elif ans > n:
            return i-1
    