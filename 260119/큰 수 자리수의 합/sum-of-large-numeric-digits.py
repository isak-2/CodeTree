a, b, c = map(int, input().split())

# Please write your code here.
def func(mul):
    if mul < 10:
        return mul
    remainder = mul % 10
    mul = mul // 10
    return remainder + func(mul) 






mul = a * b * c 
print(func(mul))
    