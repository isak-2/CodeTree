lst = ['L','E','B','R','O','S']
ch = input()

for i in range(len(lst)):
    if lst[i] == ch:
        print(i)
        break
    if i == len(lst)-1:
        print('None')

 