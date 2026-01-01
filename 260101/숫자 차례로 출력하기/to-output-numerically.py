n = int(input())

# Please write your code here.
def reccur(n):
    if n == 0:
        return
    reccur(n-1) 
    print(n, end=' ')
    
def reccur_(n):
    if n == 0:
        return
    print(n, end=' ') 
    reccur_(n-1)

reccur(n)
print()
reccur_(n)