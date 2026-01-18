N = int(input())

# Please write your code here.
def func(n,k):
    if n == 2 and k == 0:
        return 2
    elif n == 1 and k == 1:
        return 1 
    return n + func(n-2,k)

if N % 2 == 0:
    k = 0
else:
    k = 1
print(func(N,k))

