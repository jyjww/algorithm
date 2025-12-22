def solution(quiz):
    quizes = []
    
    for q in quiz:
        qu = q.split()
        quizes.append(qu)
    
    answer = []
    
    def operator(op, a, b):
        if op == "+":
            return a + b
        else:
            return a - b
        
    for eq in quizes:
        ans = operator(eq[1], int(eq[0]), int(eq[2]))
        if ans == int(eq[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer