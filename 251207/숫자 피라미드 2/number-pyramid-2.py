N = int(input()) #수를 입력받는다. 
total = 0 #출력할 총합을 초기화 
for i in range(1,N+1): #1부터 입력받은 수까지 반복한다. (행의 개수) 
    for j in range(1,i+1): #행의 개수만큼 반복한다. (열의 개수)
        total += 1 #총합을 1씩 더한다. 
        print(total, end=' ') #총합과 빈칸을 한칸 출력한다. 
    print() #줄바꿈을 한다. 
