n = int(input())
lst = []

for _ in range(n):
  x, y = input().split()
  lst.append([int(x), int(y)])
  
lst.sort(key=lambda x: (x[0], x[1]))

for x, y in lst:
  print (x, y)