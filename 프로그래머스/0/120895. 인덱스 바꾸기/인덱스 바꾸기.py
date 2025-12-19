def solution(my_string, num1, num2):
    answer = [ch for ch in my_string]
    a, b = answer[num1], answer[num2]
    answer[num1] = b
    answer[num2] = a
    
    return "".join(answer)