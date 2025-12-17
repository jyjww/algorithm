def solution(n):
    answer = []
    i = 2
    
    def isPrime(num):
        if num == 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    for i in range(2, n+1):
        if isPrime(i) == False:
            continue
        while n % i == 0:
            answer.append(i)
            n //= i
    return sorted(list(set(answer)))