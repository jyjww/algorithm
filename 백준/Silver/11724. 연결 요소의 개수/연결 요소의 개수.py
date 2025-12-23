import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

# 인접 리스트 만들기
graph = [[] for _ in range (n+1)]

# 간선 정보 입력
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 재귀로 dfs 인접 노드 탐색 : x에서 출발해서 갈 수 있는 모든 노드를 다 방문
visited = [False] * (n+1)
def dfs(x):
  visited[x] = True
  for nxt in graph[x]:
    if not visited[nxt]:
      dfs(nxt)

# 노드 1부터 n까지 확인. 아직 방문 안 한 노드를 발견하면 그 노드에서 DFS 시작
cnt = 0
for i in range(1, n+1):
  if not visited[i]:
    dfs(i)
    cnt += 1 

print(cnt)  