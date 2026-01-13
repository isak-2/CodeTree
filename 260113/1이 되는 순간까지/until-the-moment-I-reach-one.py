N = int(input())

# Please write your code here.

def func(n,cnt):
    if n == 1:
        return cnt
    cnt += 1
    if n % 2 == 0:
        return func(n // 2,cnt)
    if n % 2 == 1:
        return func(n // 3,cnt) 
        

cnt = 0
result = func(N,cnt)
print(result)