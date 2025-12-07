matrix1 = [[int(i) for i in input().split()] for _ in range(3)] #행렬 1
input() #줄간격을 사이에 두고 
matrix2 = [[int(j) for j in input().split()] for _ in range(3)] #행렬 2

#행렬간 같은인덱스 곱 행렬 형태로 출력 
for i in range(3):
    for j in range(3):
        print(matrix1[i][j] * matrix2[i][j], end=' ')
    print( )