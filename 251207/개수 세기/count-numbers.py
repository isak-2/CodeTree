N,M = map(int, input().split())
lst = [int(i) for i in input().split()]
cnt = 0
for i in lst:
    if i == M:
       cnt += 1
print(cnt)