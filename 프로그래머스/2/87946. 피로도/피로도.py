def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    
    # 현재 피로도 k
    # 아직 안 간 던전들 중 들어갈 수 있는 던전 하나 선택
    # 피로도 깎고
    # 재귀로 다음 선택
    # 매 단계마다 최대 방문 개수 갱신
    
    def dfs (k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            min_hp, need_hp = dungeons[i]
            if not visited[i] and k >= min_hp:
                visited[i] = True
                dfs(k - need_hp, count + 1)
                visited[i] = False
    
    dfs(k, 0)
    return answer