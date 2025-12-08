N,M = map(int,input().split())
matrix1 = [[int(x) for x in input().split()] for _ in range(N)]
matrix2 = [[int(x) for x in input().split()] for _ in range(N)]
matrix3 = []
for i in range(N):
    rows = []
    for j in range(M):
        if matrix1[i][j] == matrix2[i][j]:
            rows.append(0)
        else:
            rows.append(1)   
    matrix3.append(rows)

for i in matrix3:
    for j in i:
        print(j, end=' ')
    print( )