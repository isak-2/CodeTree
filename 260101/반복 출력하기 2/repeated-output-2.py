n = int(input())

# Please write your code here.
def H_print(n):
    if n == 0:
        return 
    H_print(n-1)
    print('HelloWorld')

H_print(n)