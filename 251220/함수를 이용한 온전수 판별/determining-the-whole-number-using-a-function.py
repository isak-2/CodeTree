a, b = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(a,b+1):
    remainder = i % 10
    if i % 2 != 0 and remainder != 5 and not(i % 3 == 0 and i % 9 != 0):
        cnt += 1
print(cnt)
