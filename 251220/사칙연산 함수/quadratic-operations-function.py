a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cal(a,o,c):
    if o == '*':
        return a * c 
    elif o == '-':
        return a - c
    elif o == '+':
        return a + c 
    elif o == '/':
        return int(a / c)
    else:
        return 

flag = False
for i in ['+','-','*','/','None']:
    if o in i: 
         print(f'{a} {o} {c} = {cal(a,o,c)}')
         break
    elif i == 'None':
        flag = True
    

if flag:
    print(False)
