n = int(input())
lst = []

for _ in range(n):
  a, b =input().split()
  lst.append([int(a), b])

lst.sort(key=lambda x: x[0])

for age, name in lst:
  print(age, name)