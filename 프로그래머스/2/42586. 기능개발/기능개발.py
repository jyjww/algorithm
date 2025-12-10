def solution(progresses, speeds):
    answer = []
    a = 0
    for i in range(len(progresses)):
        a = 100 - progresses[i]
        cnt = 0
        while a > 0:
            a -= speeds[i]
            cnt += 1
        answer.append(cnt)
    deploy = []
    current = answer[0]
    cnt = 1
    
    for a in answer[1:]:
        if a <= current:
            # 기준일보다 빨리 끝나거나 같은 날 끝나면 배포
            cnt += 1
        else:
            # 더 오래걸리는 기능은 새로운 배포 묶음 초기화
            deploy.append(cnt)
            current = a
            cnt = 1
    deploy.append(cnt)
    
    return deploy