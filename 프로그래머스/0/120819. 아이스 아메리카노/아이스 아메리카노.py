def solution(money):
    cups = money // 5500
    left = money - cups * 5500
    
    return [cups, left]