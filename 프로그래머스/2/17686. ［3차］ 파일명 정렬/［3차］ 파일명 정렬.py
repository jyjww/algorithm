import re
def solution(files):
    answer = []
    pattern = r"([^\d]+)(\d+)(.*)"
    
    for file in files:
        m = re.match(pattern, file)
        head, num, tail = m.group(1), m.group(2), m.group(3)
        answer.append([head, num, tail])
    
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    result = []
    for x in answer:
        result.append("".join(x))
    return result