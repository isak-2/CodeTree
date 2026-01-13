N = int(input())

# Please write your code here.
def func(n):
    if n < 10:
        return n**2
    return func(n // 10) + ((n % 10)**2)


result = func(N)
print(result)