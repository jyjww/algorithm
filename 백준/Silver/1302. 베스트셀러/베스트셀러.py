n = int(input())
lst = [input() for _ in range(n)]

lst.sort(key=lambda x: x)

dic = {}

for l in lst:
  if l in dic:
    dic[l] += 1
  else:
    dic[l] = 1

max_val = max(dic.values())
max_key = [k for k, v in dic.items() if v == max_val]

print(max_key[0])