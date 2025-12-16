n, m = map(int, input().split())
no_hear = [input() for _ in range(n)]
no_see = [input() for _ in range (n+1, n+m+1)]

both = sorted(list(set(no_hear) & set(no_see)))

print(len(both))
for b in both:
  print(b)