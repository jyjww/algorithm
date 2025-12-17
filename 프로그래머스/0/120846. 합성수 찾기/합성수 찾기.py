def solution(n):
    prime = 0
    if n < 4:
        return 0
    for num in range(4, n+1):
        for i in range (2, int(num**0.5) +1):
            if num % i == 0:
                prime += 1
                break
    return prime