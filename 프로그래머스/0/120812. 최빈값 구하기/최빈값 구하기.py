def solution(array):
    dict = {}
    
    for x in array:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
    max_val = max(dict.values())
    keys = [k for k, v in dict.items() if v == max_val]
    
    if len(keys) > 1:
        return -1
    else:
        return keys[0]