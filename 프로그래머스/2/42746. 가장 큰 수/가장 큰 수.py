from functools import cmp_to_key
def solution(numbers):
    num = list(map(str, numbers))

    # 비교 함수 : x가 앞이면 음수, y가 앞이면 양수
    def cmp(x, y):
        if x+y > y+x:
            return -1
        if x+y < y+x:
            return 1
        return 0
    
    num.sort(key=cmp_to_key(cmp))
    
    # 0 으로만된 배열은 0으로 리턴
    if num[0] == "0":
        return "0"
    
    return "".join(num)