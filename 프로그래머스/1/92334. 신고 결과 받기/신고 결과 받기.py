def solution(id_list, report, k):
    report = set(report)
    reported_cnt = {}
    reporter_id = {}
    
    for r in report:
        reporter, reported = r.split()
        reported_cnt[reported] = reported_cnt.get(reported, 0) + 1
        
        if reporter not in reporter_id:
            reporter_id[reporter] = []
        reporter_id[reporter].append(reported)
    
    banned = set()
    for user, cnt in reported_cnt.items():
        if cnt >= k:
            banned.add(user)
            
    answer = []
    for user in id_list:
        mail = 0
        for target in reporter_id.get(user, []):
            if target in banned:
                mail += 1
        answer.append(mail)
    
    return answer