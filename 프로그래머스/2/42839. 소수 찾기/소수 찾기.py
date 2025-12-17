import itertools as it
def solution(numbers):
    
    def isPrime(num):
        if num == 1 or num == 0:
            return False
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True
    
    num_lst = [ch for ch in numbers]
    candidate = []
    
    ans = set()
    cnt = 0 

    for i in range(1, len(num_lst)+1):
        # 숫자의 조합을 만듬
        for tup in it.permutations(num_lst, i):
            candidate.append(tup)
        
        # 후보가 될 숫자들을 조인하고, set로 중복을 제거
        for j in candidate:
            a = int("".join(x for x in j))
            ans.add(a)
            
    for a in ans:
        if isPrime(a) == True:
            cnt +=1 
    return cnt