matrix = [] #3행 3열 매트릭스를 선언 
for i in range(3): # 3행 반복 
    rows = list(map(int, input().split())) #행의 원소 3개를 입력받아서 리스트로 묶어 한행을 저장함. 
    new_rows = [] # 3배한 원소를 저장할 새로운 행 리스트를 선언 
    for j in range(3): # 3번 반복 
        new_rows.append(rows[j]*3) #리스트의 원소에 3배를 곱해서 새 리스트에 넣어줌. 
    matrix.append(new_rows) # 3배한 리스트를 매트릭스에 추가함. (행추가)

for i in matrix:
    for j in i:
        print(j,end=' ')
    print( )