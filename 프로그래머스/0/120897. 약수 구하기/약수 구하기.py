def solution(n):
    def isPrime(num):
        if num == 1:
            return False
        for i in range (2, num+1):
            if num % i == 0:
                return False
        return True
    ans = []
    if isPrime(n) == True:
        return [1, n]
    for i in range (1, n+1):
        if isPrime(i) == False:
            if n % i == 0:
                ans.append(i)
    
    return ans