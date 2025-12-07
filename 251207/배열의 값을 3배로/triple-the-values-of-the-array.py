matrix = [
    [int(x) * 3 for x in input().split()]
    for _ in range(3)
]



for i in matrix:
    for j in i:
        print(j,end=' ')
    print( )