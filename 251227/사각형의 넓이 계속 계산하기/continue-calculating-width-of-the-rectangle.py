lst = []
while True:
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    lst.append(a*b)
    if c == 'C':
        break


for i in lst:
    print(i)
