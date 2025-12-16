def solution(numbers, k):
    cnt = 0
    i = 0
    while cnt < k-1:
        i = (2 * (k - 1)) % len(numbers)
        cnt += 1
    return numbers[i]