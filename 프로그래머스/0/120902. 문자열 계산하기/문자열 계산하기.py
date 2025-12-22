def solution(my_string):
    
    string = my_string.split()
    num = int(string[0])
    
    for i in range (1, len(string), 2):
        ch = string[i]
        num2 = int(string[i+1])
        
        if ch == "+":
            num += num2
        else:
            num -= num2
    return num