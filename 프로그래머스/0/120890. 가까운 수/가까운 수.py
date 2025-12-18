def solution(array, n):
    dic = {}
    for i in range(len(array)):
        dic[i] = abs(n - array[i])
    
    min_val = min(dic.values())
    key = [k for k, v in dic.items() if v == min_val]
    
    if len(key) < 2:
        return array[key[0]]
    else:
        return min(array[k] for k in key)