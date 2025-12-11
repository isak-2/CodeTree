N = int(input())
arr = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    cnt = 1
    if i % 2 == 0: 
        for j in range(N):
            arr[j][i] = cnt
            cnt += 1 
    else:
        for j in range(N-1,-1,-1):
            arr[j][i] = cnt
            cnt += 1 
    cnt = 0 



for i in arr:
    for j in i:
        print(j, end='')
    print( )
