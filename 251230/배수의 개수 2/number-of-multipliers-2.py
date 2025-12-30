lst = []
for _ in range(10):
    num = int(input())
    lst.append(num)
cnt = 0
for i in lst:
    if i % 2 != 0:
        cnt +=1 

print(cnt)       