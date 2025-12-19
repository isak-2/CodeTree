y = int(input())

# Please write your code here.
def func(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return 'false'
        return 'true'
    else:
        return 'false'


print(func(y))