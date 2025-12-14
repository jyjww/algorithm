def solution(array, commands):
    # i번째 숫자부터 j번째 숫자까지에서, 정렬 후 k번째 수를 구해라
    answer = []
    
    for c in commands:
        a = []
        
        a = sorted(array[c[0]-1:c[1]])
        k = c[-1]
        answer.append(a[k-1])
    
    return answer