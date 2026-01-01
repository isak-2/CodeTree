n = int(input())

# Please write your code here.
def recurr(n):
    if n == 0: return 
    print('* '*n)
    recurr(n-1)
    print('* '*n)

recurr(n)