# n = int(input())
# m = [[0]*n for _ in range(n)]
# for i in range(n):
#   f, t = map(int, input().split())
#   m[f-1][t-1], m[t-1][f-1]=1, 1
# print(m)


n = int(input())
m = [tuple(map(int, input().split())) for _ in range(n)]
linked = [[]*n for _ in range(n)]
for i in range(n):
  for f, t in m:
    if i==f-1:
      linked[i].append(t)
print(linked)