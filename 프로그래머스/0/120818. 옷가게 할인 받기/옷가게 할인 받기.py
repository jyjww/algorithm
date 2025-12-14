import math
def solution(price):
    n = 100000
    if price < n*1:
        return price
    elif n <= price < 3*n:
        return math.floor(price*0.95)
    elif 3*n <= price < 5*n:
        return math.floor(price*0.9)
    elif price >= 5*n:
        return math.floor(price*0.8)
    else:
        return -1