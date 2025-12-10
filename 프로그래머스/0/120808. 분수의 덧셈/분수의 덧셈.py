def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1 * denom2
    
    # 최대 공약수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    g = gcd(numer, denom)
     
    numer //= g
    denom //= g
    
    return [numer, denom]