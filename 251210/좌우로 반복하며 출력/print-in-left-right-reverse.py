N = int(input())

for i in range(N):
      
    
    if i % 2 == 0:
        cnt = 1
        for _ in range(N):
            print(cnt, end='')
            cnt += 1
    else:
        cnt = N
        for _ in range(N):
            print(cnt, end='')
            cnt -= 1
    print( )