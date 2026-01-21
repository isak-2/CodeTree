n = int(input())

# Please write your code here.
def func(n,count):
    if n == 1:
        return count
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3 
        n += 1
    count += 1
    return func(n,count)

count = func(n,0)
print(count)