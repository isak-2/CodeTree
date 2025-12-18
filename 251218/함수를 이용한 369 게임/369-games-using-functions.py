a, b = map(int, input().split())
cnt = 0
# Please write your code here.

def multiple3(number2):
    if number2 % 3 == 0:
        return True



def magic_func(number):
    value = str(number)
    # 튜플 컴프리헨션 및 any 처음활용 
    if any(x in value for x in ['3','6','9']) or multiple3(number):
        return True


for i in range(a,b+1):
    if magic_func(i):
       cnt += 1 

print(cnt)