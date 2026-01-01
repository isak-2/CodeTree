n = int(input())

# Please write your code here.
def reccur(n):
    if n == 0:
        return 
    reccur(n-1)
    print('*' * n, end='')
    print()

reccur(n)