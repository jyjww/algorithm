def solution(arr):
    answer = []
    seen = -1
    for num in arr:
        if num == seen:
            continue
        else:
            answer.append(num)
            seen = num
    return answer