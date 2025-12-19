def solution(numbers):
    dic = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    ans = ''
    i = 0
    while i < len(numbers):
        if numbers[i:i+3] in dic:
            ans += str(dic[numbers[i:i+3]])
            i += 3
        elif numbers[i:i+4] in dic:
            ans += str(dic[numbers[i:i+4]])
            i += 4
        elif numbers[i:i+5] in dic:
            ans += str(dic[numbers[i:i+5]])
            i += 5
        else:
            return 0
    return int(ans)