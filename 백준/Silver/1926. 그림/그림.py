import sys
from collections import deque
input = sys.stdin.readline

n, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * h for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(iy, ix):
  q = deque()
  q.append((iy, ix))
  visited[iy][ix] = True
  area = 1
  
  while q:
    y, x = q.popleft()
    
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      
      if 0 <= ny < n and 0 <= nx < h:
        if arr[ny][nx] == 1 and not visited[ny][nx]:
          visited[ny][nx] = True
          q.append((ny, nx))
          area += 1
  return area

picture = 0
max_area = 0
for i in range (n):
  for j in range (h):
    if arr[i][j] == 1 and not visited[i][j]:
      picture += 1
      max_area = max(bfs(i, j), max_area)
    
        
print(picture, max_area, sep="\n")